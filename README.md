# 🏥 Karachi Community Health Intelligence System (K-CHIS)

> A comprehensive, data-driven epidemiological surveillance, statistical testing, and predictive machine learning platform designed to analyze community health vulnerabilities in Karachi, Pakistan.

---

## 📌 Project Overview
The **Karachi Community Health Intelligence System (K-CHIS)** transforms raw public health survey data into actionable health intelligence. This project integrates automated exploratory data analysis (EDA), multi-section KPI reporting, rigorous inferential statistics (Chi-Square and Pearson correlation), and predictive machine learning modeling to uncover socioeconomic, nutritional, and chronic disease trends.

---

## 📂 Project Architecture & Directory Structure
```text
karachi-community-health-intelligence-system/
│
├── data/                               # Raw and cleaned surveillance datasets
│   ├── Karachi Community Health Surveillance Analytics System.xlsx
│   └── Karachi Community Health Surveillance Analytics System_cleaned.xlsx
│
├── notebooks/                          # Jupyter Notebook pipeline (01 to 05)
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_visualization.ipynb
│   ├── 03_health_intelligence_kpis.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_executive_summary.ipynb
│
├── src/                                # Modularized Python source code
│   ├── preprocessing.py
│   └── utils.py
│
├── visuals/                            # Exported high-resolution figures (Figs 1–13)
│   ├── fig1_to_fig6_*.png
│   ├── fig7_disease_prevalence.png
│   ├── fig8_physical_activity.png
│   ├── fig9_healthcare_visits.png
│   ├── fig10_medication_use.png
│   ├── fig11_income_by_bmi.png
│   ├── fig12_age_vs_bmi_regplot.png
│   └── fig13_confusion_matrix.png
│
├── reports/                            # Formal documentation & executive briefs
│   └── final_health_intelligence_report.md
│
├── dashboard/                          # Interactive Streamlit Web Application
│   └── app.py
│
├── requirements.txt                    # Project dependencies
└── README.md                           # Project documentation


## 📊 Key Findings & Epidemiological Insights
Demographic Baseline: Analyzed a surveillance cohort of 472 participants across Karachi, capturing detailed demographic, socioeconomic, and lifestyle metrics.

Nutritional Vulnerability: Identified an overall malnutrition prevalence rate of 58.9%, with a striking 46.0% underweight rate among vulnerable groups.

Chronic Disease Morbidity:

Hypertension emerged as the leading chronic condition at 19.1% prevalence.

Dyspepsia recorded high gastrointestinal incidence at 17.2%.

Cancer indicators registered at 16.1%, while established diabetes stands at 10.2%.

Statistical Correlations: Chi-square testing confirmed a statistically significant relationship between household income brackets and nutritional/BMI outcomes.

Predictive Modeling: A trained Logistic Regression model (with standardized scaling) successfully predicted baseline malnutrition risk factors across multi-variable demographic and lifestyle features.

## 🛠️ Tech Stack & Libraries
Language: Python 3.x

Data Manipulation & Analysis: Pandas, NumPy

Statistical Testing: SciPy (chi2_contingency, pearsonr)

Machine Learning: Scikit-Learn (LogisticRegression, StandardScaler, metrics evaluation)

Data Visualization: Seaborn, Matplotlib

Interactive Dashboard: Streamlit

Environment: VS Code, Git / GitHub

## Author

Dr. Najeeb Akhter
PhD | Researcher | Public Health | Data Analytics | Monitoring & Evaluation