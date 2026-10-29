# 🎓 Essential, but Neglected: Developers' Perspectives on AppSec Practices and Automated Security Tools

This replication package accompanies the study. It includes questionnaire materials, survey data, manually developed qualitative codebooks, analysis notebooks and scripts, and the tables and figures reported in the paper. The notebooks reproduce computational analyses; qualitative coding was performed manually and is documented separately.

## Context

Application Security (AppSec) practices are essential for protecting software systems against vulnerabilities and cyber threats. However, their practical effectiveness is closely related to consistent adoption, while developers report a range of practical constraints surrounding their use.

## Goal

This study investigates how developers perceive and report using AppSec practices, and how they report using automated security tools within development workflows.

## 🔬 Method

To achieve these objectives, we conducted an empirical, developer-centered study grounded in a curated set of 16 AppSec practices, including Secure Coding, Code Review, Threat Modeling, and Fuzz Testing, derived from prior research and refined through expert analysis by three researchers. Based on this set, we designed and administered a questionnaire to Brazilian software professionals working in the software industry, yielding 83 valid responses. The questionnaire captured participants’ profiles, security-related experience, perceptions of AppSec practices, and reported adoption and use of automated security tools.

## 📚 Results

The results reveal a heterogeneous landscape of reported AppSec use, with a notable gap between perceived essentiality and reported frequency of use. Practices such as Code Review and Secure Coding are more frequently reported, whereas Penetration Testing and External Security Auditing are reported less frequently despite their comparatively higher perceived essentiality. Participants also report challenges associated with automated security tool use, including false positives, learning curves, and difficulties integrating tools into existing development workflows.

## 🧠 Conclusion

Our findings provide developer-centered empirical evidence that AppSec practices perceived as essential are not always reported as frequently used, while automated security tool use is accompanied by recurring challenges related to integration, usability, and tool output quality. These insights can inform the design of tools, training initiatives, and organizational strategies aimed at better supporting the integration of security into software development.

---

## 📁 Repository Structure

```
appsec-practices-characterization-survey/
├── data/                                  Input data (survey answers, in Portuguese)
│   ├── survey_all_responses_ptbr.xlsx     All answers to the questionnaire
│   └── qualitative_responses_ptbr.xlsx    Open-ended responses used in qualitative analyses
├── qualitative_analysis/                  Codebooks of the open questions Q16, Q18, Q19, Q27 and Q31
│   ├── codebook_Q16_pt_br.xlsx            Q16 codebook (Portuguese only)
│   ├── codebook_Q18_en.xlsm               Q18 codebook (English)
│   ├── codebook_Q18_pt_br.xlsm            Q18 codebook (Portuguese)
│   ├── codebook_Q19_en.xlsm               Q19 codebook (English)
│   ├── codebook_Q19_pt_br.xlsm            Q19 codebook (Portuguese)
│   ├── codebook_Q27_en.xlsm               Q27 codebook (English)
│   ├── codebook_Q27_pt_br.xlsm            Q27 codebook (Portuguese)
│   ├── codebook_Q31_en.xlsm               Q31 codebook (English)
│   └── codebook_Q31_pt_br.xlsm            Q31 codebook (Portuguese)
├── results/                               Generated tables, spreadsheets, and figures
│   ├── characterization/
│   ├── RQ1/
│   ├── RQ2/
│   ├── RQ3/
│   └── tools_usage_frequency_responses.xlsx
├── scripts/
│   └── generate_latex_tables.py           LaTeX tables of RQ1 and RQ2
├── study_artifacts/                       Questionnaire, consent forms, and supplementary materials
│   ├── Script_survey_en.pdf               Questionnaire (English)
│   ├── Script_survey_pt_br.pdf            Questionnaire (Portuguese)
│   ├── Free_and_Informed_Consent_Form_(FICF)_en.pdf        Consent form (English)
│   ├── Termo_de_Consentimento_Livre_e_Esclarecido_(TCLE)_pt_br.pdf  Consent form (Portuguese)
│   └── appsec_practice_selection_and_consolidation.xlsm   AppSec practice selection and consolidation process
├── characterization_analysis_of_the_participants.ipynb
├── RQ1.ipynb
├── RQ2.ipynb
├── RQ3.ipynb
├── RQ3_part2_analysis.ipynb
└── requirements.txt
```

### Notebooks and outputs

| Notebook / script | Analysis | Outputs |
|---|---|---|
| `characterization_analysis_of_the_participants.ipynb` | Profile of the participants | `results/characterization/roles_analysis.xlsx`, `system_types_analysis.xlsx`, `system_domains_analysis.xlsx`, `organization_sectors_analysis.xlsx`, `certifications_analysis.xlsx` |
| `RQ1.ipynb` | Perceived frequency of use, effectiveness, ease of use and essentiality of the 16 practices; Spearman correlations between these attributes | `results/RQ1/comparison_categories.xlsx`, `correlations.xlsx` |
| `RQ2.ipynb` | Differences between groups (experience, organization size, role): Mann-Whitney U tests and Cliff's delta | `results/RQ2/analysis_results_raw.xlsx`, `analysis_results_formatted.xlsx`; `results/tools_usage_frequency_responses.xlsx` (answers about the use of each tool category) |
| `RQ3.ipynb` | Frequency of use of automated security tools, by category and period | `results/RQ3/{daily,weekly,monthly,annually,not_applicable}/*.csv`, `summary_period_category_tools.xlsx` |
| `RQ3_part2_analysis.ipynb` | Challenges (Q28), desired improvements (Q29) and future use (Q32, Q33) of automated security tools; overlap between the groups | `results/RQ3/challenges_by_group.tex`, `challenges_within_across_groups.tex`/`.xlsx`, `improvements_within_across_groups.tex`/`.xlsx`, `group_overlap_venn.pdf`/`.png`, `group_overlap_sankey.pdf`/`.png` |
| `scripts/generate_latex_tables.py` | LaTeX tables of RQ1 and RQ2, from the spreadsheets above | `results/RQ1/comparison_categories.tex`, `correlations.tex`, `results/RQ2/analysis_results.tex` |

### Analysis decisions

- **Sample:** We analyze 83 eligible respondents who reported either direct (n=62) or indirect (n=21) professional exposure to security in software development. Respondents reporting neither were excluded.
- **Unweighted RQ1 analysis:** Each valid participant response contributes equally. For descriptive comparisons, the mean of valid responses is divided by the maximum score for that dimension (4 for frequency of use; 5 for ease of use, perceived effectiveness, and essentiality). No expertise-based weights are applied. Spearman correlations use original participant-level responses, not normalized aggregate scores.
- **Not Applicable responses:** For AppSec practice perceptions (Q17 and Q20–Q22), "Não Aplicável" ("Not Applicable") is treated as missing and excluded from descriptive means and RQ2 group tests. RQ1 correlations use only participants with valid responses to both dimensions of a pair. In Q24, however, "Not Applicable" denotes reported non-use of the corresponding *tool category* and is retained as a response category.
- **RQ2 comparison groups:** Direct (n=62) vs. indirect (n=21) security experience; large (n=65; at least 100 employees) vs. small (n=16; up to 99 employees) organizations; and security specialists (n=57) vs. non-specialists (n=26). The two respondents with unknown organization size are excluded only from analyses requiring that variable.
- **Security specialists:** Classification is based on Q6. Respondents reporting at least one explicitly security-focused role (e.g., Cryptographer, Penetration Tester, Privacy Engineer, Security Engineer, Security Analyst, DevSecOps, AppSec, or SOC Analyst) are classified as specialists; DevOps Engineer alone is not considered a specialist role.
- **Group tests (RQ2):** We use two-sided Mann-Whitney U (Wilcoxon rank-sum) tests and Cliff's Delta to describe the magnitude and direction of group differences. Group membership is not interpreted causally.
- **Multiple comparisons:** For RQ1, Holm-adjusted p-values are computed across the 96 Spearman correlations (16 practices × 6 dimension pairs). For RQ2, Holm correction is applied separately within each family of 16 practice-level tests for a given grouping factor and perception dimension. Statistical significance is assessed using adjusted p-values below 0.05.
- **Tool adoption (RQ3):** Q23 distinguishes participants reporting use (n=49), partial use (n=20), and non-use (n=14) of automated security tools. Q24–Q30 were shown to the 69 participants who reported use or partial use. Q28 and Q29 counts and percentages refer to those 69 participants unless a smaller group denominator is explicitly reported. Q25 records specific tools used *currently or previously*; consequently, a tool reported in Q25 does not necessarily imply current use of its category in Q24.
- **Qualitative material:** Codebooks for Q16, Q18, Q19, Q27, and Q31 document manual analysis; executing the notebooks does not reproduce the human coding process.

The questionnaire responses are in Portuguese, and notebooks use the original question wording and response options. The `study_artifacts/` and `qualitative_analysis/` folders provide Portuguese and English materials as indicated in the repository structure.

### Data privacy and release checks

The questionnaire included optional contact information fields (Q30 and Q34). These fields are excluded from the publicly released dataset. Survey responses, qualitative excerpts, and generated outputs were reviewed to remove direct personal identifiers. Participant identifiers are used only to support traceability across study artifacts.


## ⚙️ Requirements

- Python 3.14 (the results were produced with Python 3.14.7);
- the packages in `requirements.txt`, with the exact versions used (including Jupyter);
- Google Chrome or Chromium, used by `kaleido` to export the Sankey diagram. If it is not installed, run `plotly_get_chrome` once after installing the requirements.

## 💻 How to Run the Replication Package

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 2. Install the requirements

```bash
pip install -r requirements.txt
```

### 3. Run the notebooks, in this order

1. `characterization_analysis_of_the_participants.ipynb`
2. `RQ1.ipynb`
3. `RQ2.ipynb`
4. `RQ3.ipynb`
5. `RQ3_part2_analysis.ipynb`

Run the notebooks interactively with `jupyter notebook`, or sequentially from a Linux/macOS shell:

```bash
for notebook in characterization_analysis_of_the_participants RQ1 RQ2 RQ3 RQ3_part2_analysis; do
    jupyter nbconvert --to notebook --execute --inplace "$notebook.ipynb"
done
```

On Windows (PowerShell), the equivalent is:

```powershell
foreach ($notebook in @("characterization_analysis_of_the_participants", "RQ1", "RQ2", "RQ3", "RQ3_part2_analysis")) {
  jupyter nbconvert --to notebook --execute --inplace "$notebook.ipynb"
}
```

**Note:** The `--inplace` option overwrites the notebook files with executed versions. Work in a fresh clone or a separate working copy if you want to preserve the committed notebook outputs. Notebook execution regenerates computational results, not the manual qualitative codebooks.
 

### 4. Generate the LaTeX tables of RQ1 and RQ2

```bash
python scripts/generate_latex_tables.py
```

Generated computational outputs are written to `results/` (the folders are created if they do not exist), and plots are also displayed in the notebooks. Compare the regenerated files with the archived results to check reproducibility. Qualitative codebooks remain documented research artifacts rather than notebook-generated outputs.