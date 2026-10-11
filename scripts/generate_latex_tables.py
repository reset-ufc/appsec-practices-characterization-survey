"""
Generates the LaTeX (Overleaf) tables of RQ1 and RQ2.

RQ1, from the spreadsheets saved by RQ1.ipynb, using the same colors
as the notebook Stylers:

- comparison_categories.xlsx -> comparison_categories.tex
  RdYlGn gradient per column (low=0.3, high=0.4)
- correlations.xlsx -> correlations.tex
  RdYlGn on a fixed scale from -1 to 1; * marks Holm p-value < 0.05

RQ2, from the spreadsheet saved by RQ2.ipynb:

- analysis_results_raw.xlsx -> analysis_results.tex
  Group means, two-sided p-value, Holm p-value and Cliff's delta; significant
  results (Holm p-value <= 0.05) have the p-value in bold and the higher
  group mean in gray

Usage (from the repository root, after running the notebooks):
    venv/bin/python scripts/generate_latex_tables.py
"""

import ast
from pathlib import Path

import matplotlib
import pandas as pd
from matplotlib import colors

RQ1_PATH = Path(__file__).resolve().parent.parent / 'results' / 'RQ1'
RQ2_PATH = Path(__file__).resolve().parent.parent / 'results' / 'RQ2'

CMAP = matplotlib.colormaps['RdYlGn']

# Same threshold pandas' background_gradient uses to switch to light text
TEXT_COLOR_THRESHOLD = 0.408
LIGHT_TEXT_COLOR = 'F1F1F1'

SIGNIFICANCE_LEVEL = 0.05

# (column in the spreadsheet, header in the table)
COMPARISON_COLUMNS = [
    ('Ease of use', 'Ease of use'),
    ('Effectiveness', 'Effectiveness'),
    ('Frequency of use', 'Frequency of use'),
    ('Essentiality', 'Essentiality'),
]

CORRELATION_COLUMNS = [
    ('Frequency x Effectiveness', 'Freq $\\times$ Eff (H1)'),
    ('Frequency x Ease of use', 'Freq $\\times$ Ease (H2)'),
    ('Frequency x Essentiality', 'Freq $\\times$ Ess (H3)'),
    ('Effectiveness x Ease of use', 'Eff $\\times$ Ease (H4)'),
    ('Effectiveness x Essentiality', 'Eff $\\times$ Ess (H5)'),
    ('Ease of use x Essentiality', 'Ease $\\times$ Ess (H6)'),
]

# Practice order of the RQ2 table in the paper
RQ2_PRACTICE_ORDER = [
    'Architectural Risk Analysis',
    'Undergoing External Security Audits',
    'Secure Coding',
    'Security Configuration and Management',
    'Security Requirements Engineering',
    'Performing Fuzz Testing',
    'Risk Management',
    'Vulnerability Management',
    'Identifying Abuse/Misuse Cases',
    'Threat Modeling',
    'Monitoring for Security Events',
    'Emergency Codebase Response',
    'Code Review',
    'Software Supply Chain Security',
    'Penetration Testing',
    'Manual/Automated Security Testing',
]

# (group 1 mean column, group 2 mean column, comparison suffix)
RQ2_COMPARISONS = [
    ('Mean Direct', 'Mean Indirect', 'Direct/Indirect'),
    ('Mean Large', 'Mean Small', 'Big/Small'),
    ('Mean Specialist', 'Mean Non-Specialist', 'Specialist/Non-Specialist'),
]

RQ2_HIGHLIGHT_COLOR = 'D9D9D9'


def latex_text(text):
    """Escapes the characters of the practice names that are special in LaTeX."""
    return text.replace('&', '\\&')


def relative_luminance(rgba):
    """Relative luminance (W3C), the same formula used by pandas."""
    r, g, b = (
        x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4
        for x in rgba[:3]
    )
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def colored_cell(value, norm, text):
    """Returns a cell with background color and, on dark colors, light text."""
    rgba = CMAP(norm(value))
    background = colors.rgb2hex(rgba)[1:].upper()

    if relative_luminance(rgba) < TEXT_COLOR_THRESHOLD:
        text = f'{{\\color[HTML]{{{LIGHT_TEXT_COLOR}}} {text}}}'

    return f'\\cellcolor[HTML]{{{background}}}{text}'


def column_norm(series, low=0.3, high=0.4):
    """Same normalization as Styler.background_gradient(low=..., high=...)."""
    value_range = series.max() - series.min()
    return colors.Normalize(
        series.min() - value_range * low,
        series.max() + value_range * high
    )


def comparison_table(xlsx_path):
    df = pd.read_excel(xlsx_path, index_col=0).set_index('Practice')
    norms = {col: column_norm(df[col]) for col, _ in COMPARISON_COLUMNS}

    white = '\\cellcolor[HTML]{FFFFFF}'
    headers = [
        f'\\multicolumn{{1}}{{c}}{{{white}\\textbf{{AppSec practice}}}}',
        f'\\multicolumn{{1}}{{c}}{{{white}\\textbf{{Ease of use}}}}',
        f'\\multicolumn{{1}}{{c}}{{{white}\\textbf{{Effectiveness}}}}',
        '\\multicolumn{1}{c}{\\textbf{Frequency of use}}',
        '\\multicolumn{1}{c}{\\textbf{Essentiality}}',
    ]

    rows = []
    for practice, values in df.iterrows():
        cells = [f'{white}{latex_text(practice)}']
        cells += [
            colored_cell(values[col], norms[col], f'{values[col]:.2f}')
            for col, _ in COMPARISON_COLUMNS
        ]
        rows.append(' & '.join(cells) + ' \\\\')
    rows[-1] += ' \\hline'

    lines = [
        '\\begin{table}[ht!]',
        '%\\caption{Comparison of the frequency of use, ease of use, effectiveness, and essentiality of AppSec practices.}',
        '\\caption{Comparison of AppSec practices across perception dimensions.}',
        '',
        '\\label{tab:comparacao_atributos}',
        '\\resizebox{\\textwidth}{!}{',
        '\\begin{tabular}{lrrrr}',
        '\\hline',
        ' & '.join(headers) + ' \\\\ \\hline',
        *rows,
        '\\end{tabular}',
        '}',
        '\\end{table}',
    ]
    return '\n'.join(lines) + '\n'


def correlation_table(xlsx_path):
    correlations = pd.read_excel(xlsx_path, sheet_name='Correlation', index_col=0)
    p_holm = pd.read_excel(xlsx_path, sheet_name='p-value (Holm)', index_col=0)
    norm = colors.Normalize(-1, 1)

    header_cells = ['\\textbf{AppSec Practice}'] + [
        f'\\textbf{{{header}}}' for _, header in CORRELATION_COLUMNS
    ]

    blocks = []
    for practice in correlations.index:
        cells = []
        for col, _ in CORRELATION_COLUMNS:
            value = correlations.loc[practice, col]
            mark = '*' if p_holm.loc[practice, col] < SIGNIFICANCE_LEVEL else ''
            cells.append(colored_cell(value, norm, f'{value:.3f}{mark}'))
        blocks.append(
            f'{latex_text(practice)} &\n' + ' &\n'.join(cells) + ' \\\\'
        )

    lines = [
        '\\begin{table*}[ht!]',
        '\\centering',
        '\\caption{Spearman rank correlations among perception dimensions. Cell colors indicate correlation magnitude; * denotes associations that remain statistically significant after Holm correction ($\\alpha = 0.05$).}',
        '\\label{tab:correlacao_atributos_revised}',
        '\\resizebox{\\textwidth}{!}{',
        '\\begin{tabular}{lcccccc}',
        '\\toprule',
        ' &\n'.join(header_cells) + ' \\\\',
        '\\midrule',
        '\n\n'.join(blocks),
        '\\bottomrule',
        '\\end{tabular}',
        '}',
        '\\end{table*}',
    ]
    return '\n'.join(lines) + '\n'


def effect_size_text(value):
    """Cliff's delta with sign and magnitude, e.g. '+0.52 (large)'."""
    delta, magnitude = ast.literal_eval(value)
    # Values that round to zero are shown without sign
    text = '0.00' if round(delta, 2) == 0 else f'{delta:+.2f}'
    return f'{text} ({magnitude})'


def comparison_cells(row, mean1_col, mean2_col, comparison):
    """G1, G2, p-value, Holm p-value and delta of one group comparison."""
    mean1, mean2 = row[mean1_col], row[mean2_col]
    p_value = row[f'P-value {comparison}']
    p_holm = row[f'P-value Holm {comparison}']

    group1, group2, p_holm_text = f'{mean1:.2f}', f'{mean2:.2f}', f'{p_holm:.3f}'

    if p_holm <= SIGNIFICANCE_LEVEL:
        p_holm_text = f'\\textbf{{{p_holm_text}}}'
        gray = f'\\cellcolor[HTML]{{{RQ2_HIGHLIGHT_COLOR}}}'
        if mean1 > mean2:
            group1 = f'{gray}{{{group1}}}'
        elif mean2 > mean1:
            group2 = f'{gray}{{{group2}}}'

    effect_size = effect_size_text(row[f'Effect Size {comparison}'])
    return [group1, group2, f'{p_value:.3f}', p_holm_text, effect_size]


def rq2_table(xlsx_path):
    df = pd.read_excel(xlsx_path)

    header = [
        '\\toprule',
        ' &  & \\multicolumn{5}{c}{\\textbf{Direct vs. Indirect}} & '
        '\\multicolumn{5}{c}{\\textbf{Large vs. Small}} & '
        '\\multicolumn{5}{c}{\\textbf{Spec. vs. Non-spec}} \\\\ \\cmidrule(lr){3-7}',
        '\\cmidrule(lr){8-12}',
        '\\cmidrule(lr){13-17}',
        '\\textbf{Dimension} & \\textbf{Mean} &',
        *['\\textbf{G1} & \\textbf{G2} & \\textbf{$p$} & \\textbf{$p_{Holm}$} & '
          '\\textbf{$\\delta$}' + (' &' if i < 2 else '') for i in range(3)],
        '\\\\',
        '\\midrule',
    ]

    # Practices in the same order as the table in the paper
    groups = dict(list(df.groupby('Practice')))
    assert set(groups) == set(RQ2_PRACTICE_ORDER), set(groups) ^ set(RQ2_PRACTICE_ORDER)
    practices = [(practice, groups[practice]) for practice in RQ2_PRACTICE_ORDER]
    body = []
    for p, (practice, group) in enumerate(practices):
        body.append(f'\\multicolumn{{17}}{{c}}{{\\textbf{{{latex_text(practice)}}}}} \\\\ \\midrule')

        for i, (_, row) in enumerate(group.iterrows()):
            cells = [
                f'\\textbf{{{row["Attribute"]}}}',
                f'{row["Overall Mean"]:.2f}',
            ]
            for k, (mean1_col, mean2_col, comparison) in enumerate(RQ2_COMPARISONS):
                comparison_values = comparison_cells(row, mean1_col, mean2_col, comparison)
                # Vertical line after the first two comparisons
                if k < 2:
                    comparison_values[-1] = f'\\multicolumn{{1}}{{c|}}{{{comparison_values[-1]}}}'
                cells += comparison_values

            last_row = p == len(practices) - 1 and i == len(group) - 1
            body.append(' & '.join(cells) + (' \\\\' if last_row else ' \\\\ \\midrule'))

    lines = [
        '\\begin{tiny}',
        '',
        '\\fontsize{6.1pt}{7.2pt}\\selectfont',
        '\\setlength\\LTcapwidth{\\textwidth}',
        '\\setlength{\\tabcolsep}{2.2pt}',
        '\\setlength{\\LTleft}{\\fill}',
        '\\setlength{\\LTright}{\\fill}',
        '\\centering',
        '\\begin{longtable}{@{}lcccccccccccccccc@{}}',
        '',
        '\\caption{Results of the influence of experience, organizational size and role on perceptions of AppSec practices}',
        '\\label{tab:rq2-praticas-appsec}\\\\',
        '',
        *header,
        '\\endfirsthead',
        '',
        '\\caption*{Continuation of Table~\\ref{tab:rq2-praticas-appsec}.}\\\\',
        *header,
        '\\endhead',
        '',
        '%\\midrule',
        '\\multicolumn{17}{r}{\\textit{Continued on next page}}\\\\',
        '%\\midrule',
        '\\endfoot',
        '',
        '\\bottomrule',
        '%\\multicolumn{17}{l}{\\footnotesize Fonte: Elaborado pelo autor.}\\\\',
        '\\endlastfoot',
        *body,
        '',
        '\\end{longtable}',
        '\\end{tiny}',
    ]
    return '\n'.join(lines) + '\n'


def main():
    tables = {
        RQ1_PATH / 'comparison_categories.tex': comparison_table(
            RQ1_PATH / 'comparison_categories.xlsx'),
        RQ1_PATH / 'correlations.tex': correlation_table(
            RQ1_PATH / 'correlations.xlsx'),
        RQ2_PATH / 'analysis_results.tex': rq2_table(
            RQ2_PATH / 'analysis_results_raw.xlsx'),
    }

    for path, content in tables.items():
        path.write_text(content, encoding='utf-8')
        print(f'Saved: {path}')


if __name__ == '__main__':
    main()
