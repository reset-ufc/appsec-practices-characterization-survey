# 🎓 Characterization of Appsec Practices and the Adoption of Automated Security Tools: A Comprehensive Survey With Brazilian Developers

## Context

*The adoption of Application Security (AppSec) practices is essential for protecting software systems against vulnerabilities and cyber threats. However, the effectiveness of these practices largely depends on their consistent adoption and on developers’ perceptions regarding ease of use, perceived effectiveness, essentiality, and applicability within real-world software development contexts.*

## Goal

*This study aims to characterize a set of AppSec practices in terms of frequency of use, ease of application, perceived effectiveness, and perceived essentiality. Additionally, it investigates how automated security tools are incorporated into the software development process and identifies the main challenges faced by Brazilian developers in their adoption.*
---

## 🔬 Methodology

This study followed a structured, multi-step process to define and evaluate AppSec practices:

### 📚 1. Literature Review

An extensive survey of the scientific literature was conducted to identify an initial, comprehensive set of software security practices.

### 🧠 2. Expert Refinement

The initial set was iteratively filtered, refined, and grouped by experts in Software Engineering and Software Security to:

- reduce redundancy,

- harmonize terminology, and

- ensure conceptual clarity and practical relevance.

### ✅ 3. Final AppSec Set

This process resulted in a final set of 16 Application Security (AppSec) practices.

### 📝 4. Questionnaire & Data Collection

A questionnaire based on the final set was administered to software developers working in Brazil, yielding 83 valid responses.

### 📊 5. Data Scope

The questionnaire captured:

- 👤 Participants’ profiles

- 🔐 Security-related experience

- 📈 Perceptions and adoption of AppSec practices

- 🛠️ Use of automated security tools

## 📁 Repository Structure

The repository is structured as follows:

```
analysis-security-survey/
│
├── data/: Input datasets for analysis
│
├── results/: Results tables for each research question (RQ)
│
├── study_artifacts: Materials used to support the study analyses. 
│
├── characterization_analysis_of_the_participants.ipynb: Code for performing a descriptive analysis to characterize the study participants.
│
├── requirements.txt: List of required Python packages;
│
├── RQ1.ipynb: Code for generating the results table and plots related to RQ1;
│
└── RQ2.ipynb: Code for generating the results table and plots related to RQ2;
│
└── RQ3.ipynb: Code for generating the results table and plots related to RQ3;
│
└── RQ3_part2_analysis.ipynb: Extension of the analyses from the first code (‘RQ3.ipynb’).
```

---

## ⚙️ Requirements

All dependencies for replicating the analyses can be installed using the `requirements.txt` file.  
Typical libraries expected:

- pandas  
- numpy  
- matplotlib  
- seaborn  
- jupyter  
- scikit-learn  
- scipy  

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 💻 How to Run the Replication Package

### 1. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 2. Install required packages:

```bash
pip install -r requirements.txt
```

### 3. Launch Jupyter Notebook:

```bash
jupyter notebook
```

### 4. Open and run the notebooks in the following order:

1. `characterization_analysis_of_the_participants.ipynb`  
2. `RQ1.ipynb`  
3. `RQ2.ipynb`
4. `RQ3.ipynb`
5. `RQ3_part2_analysis.ipynb`

The plots and tables can be found either in the code files or in the results directories (`results/`).
