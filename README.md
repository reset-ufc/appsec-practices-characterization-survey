# 🎓 Characterization of Appsec Practices and the Adoption of Automated Security Tools: A Comprehensive Survey With Brazilian Developers

_**Paper Description:**_  
*(Insert the full description of the paper here.)*

---

## 📁 Repository Structure

The repository is structured as follows:

```
analysis-security-survey/
│
├── data/
│
├── results/
│
├── venv/
│
├── .gitignore
│
├── characterization_analysis_of_the_participants.ipynb
│
├── LICENSE
│
├── requirements.txt
│
├── RQ1.ipynb
│
└── RQ2.ipynb
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

All generated plots and outputs will automatically appear inside the `results/` folder.
