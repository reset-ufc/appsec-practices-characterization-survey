# 🎓 Essential, but Ignored: Developers’ Perspectives on AppSec Practices and Automated Security Tools

## Context

Application Security (AppSec) practices are essential for protecting software systems against vulnerabilities and cyber threats. However, their effectiveness depends on consistent adoption, which is often influenced by developers’ perceptions and practical constraints.

## Goal

This study investigates how developers perceive, adopt, and prioritize AppSec practices, and how automated security tools are integrated into development workflows.
---
## 🔬 Method

To achieve these objectives, we conducted an empirical, developer-centered study grounded in a curated set of 16 AppSec practices derived from prior research and expert validation. Based on this set, we designed and administered a questionnaire to software developers working in the software industry, yielding 83 valid responses. The questionnaire captured participants’ profiles, security-related experience, perceptions of AppSec practices, and the adoption and use of automated security tools.

## 📚 Results
The results reveal a heterogeneous landscape of AppSec adoption, with substantial variation across practices, with a notable gap between perceived essentiality and actual use. While some practices and tools are widely adopted, others remain underused due to usability and integration challenges. Automated tool adoption is similarly affected by factors such as false positives, learning curves, and difficulties integrating tools into existing development workflows.

## 🧠 Conclusion
Our findings provide developer-centered empirical evidence that AppSec practices and automated tools,
although widely regarded as essential, are not consistently adopted in practice. These insights inform the design of tools, training initiatives, and organizational strategies to support more effective and sustainable integration of security into software development.

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
