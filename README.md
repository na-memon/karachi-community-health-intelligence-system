# 🏥 Karachi Community Health Intelligence System (K-CHIS)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Data-Pandas%2FNumPy-orange?style=flat-square&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-yellow?style=flat-square&logo=scikit-learn&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)

> A comprehensive, data-driven epidemiological surveillance, statistical testing, and predictive machine learning platform designed to analyze community health vulnerabilities in Kemari district, Karachi, Pakistan.

---

## 📊 Executive Summary & Key Metrics

The **Karachi Community Health Intelligence System (K-CHIS)** transforms primary community health survey data into actionable public health intelligence. Designed for epidemiologists, healthcare administrators, and policymakers, this platform provides multi-dimensional visibility into urban health disparities across a surveyed cohort of **N = 472**.

| Public Health Indicator | Prevalence Rate | Priority Level |
| :--- | :---: | :---: |
| **Overall Malnutrition** | **58.9%** | 🔴 Critical Priority |
| **Underweight Status (BMI < 18.5)** | **46.0%** | 🔴 Critical Vulnerability |
| **Hypertension (High Blood Pressure)** | **19.1%** | 🟠 High Risk |
| **Dyspepsia & Gastrointestinal Issues** | **17.2%** | 🟡 Moderate Risk |
| **Cancer Indicators & Screenings** | **16.1%** | 🟡 Elevated |
| **Diabetes Mellitus** | **10.2%** | 🟡 Elevated |

---

## 🗂️ Project Architecture & Directory Structure

```text
karachi-community-health-intelligence-system/
│
├── dashboard/               # Interactive 6-Page Streamlit Application
│   └── app.py               # Main application entry point
│
├── data/                    # Cleaned and validated survey datasets
│   └── Karachi Community Health Surveillance Analytics System_cleaned.xlsx
│
├── notebooks/               # Jupyter Notebooks for End-to-End Pipeline
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_visualization.ipynb
│   ├── 03_health_intelligence_kpis.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_executive_summary.ipynb
│
├── visuals/                 # 13 Publication-Ready Exported Visual Assets (Fig 1 - Fig 13)
│   ├── fig1_age_distribution.png
│   ├── fig2_bmi_classification.png
│   ├── ... (Figures 3 through 13)
│
├── reports/                 # Comprehensive executive documentation & summaries
├── src/                     # Core helper modules & transformation scripts
├── requirements.txt         # Project Python dependencies
└── LICENSE                  # MIT Open-Source License 
```
## 🚀 Key Analytic Modules & Visuals
The interactive dashboard (dashboard/app.py) embeds 13 publication-ready analytical figures categorized into 6 specialized pages https://karachi-community-health-intelligence-system-dlmsv2v62aavpa4ej.streamlit.app/: 

Executive Overview: High-level system architecture, cohort summaries, and primary KPI cards.

Demographic & Population Profiling: Age distribution, gender representation, educational tiers, and household income distribution (Fig 1 - Fig 5).

Nutritional & Malnutrition Assessment: Detailed BMI classifications and socioeconomic stratification (Fig 2, Fig 11).

Chronic Disease Surveillance: Non-communicable disease prevalence and prescribed medication usage (Fig 7, Fig 10).

Behavioral & Lifestyle Risk Mapping: Substance habits, gutka/tobacco consumption, physical activity index, and healthcare facility visit frequency (Fig 8, Fig 9).

Inferential Statistics & Machine Learning: Chi-square tests, Pearson correlations, age-BMI trajectory regression (Fig 12), and predictive Logistic Regression performance metrics (Accuracy: 78.4%, AUC-ROC: 0.84) (Fig 13).

This repository contains the cleaned dataset used for research analytics regarding community health surveillance in Karachi.

## Dataset Description
- **File:** `Karachi Community Health Surveillance Analytics System_cleaned.xlsx`
- **Rows:** 472
- **Columns:** 40 (covering demographics, anthropometric measurements, lifestyle routines, dietary servings, and chronic health conditions).
- **Anonymization:** All personal identifiers (PII) have been completely removed.

## Citation
If you use this dataset in your research, please cite our published journal article:
> * Dr S.A.M et al., 2025. Assessment of malnutrition and its determinant among the elderly population of Kemari, Pakistan. Journal of Population Therapeutics and Clinical Pharmacology, 32(4), 1182-1190. https://doi.org/10.53555/r5b13x15*

## License
This dataset is licensed under the **Creative Commons Attribution 4.0 International (CC-BY 4.0)** license. See the [LICENSE](LICENSE) file for details.


## Author

Dr. Najeeb Akhter
