# 🏥 Karachi Community Health Intelligence System (K-CHIS): Final Epidemiological & Analytics Report

**Author / Lead Data Scientist:** Project K-CHIS Team  
**Target Region:** Kemari district, Karachi, Sindh, Pakistan  
**Dataset Scope:** $N = 472$ Community Surveillance Participants ($40$ Attributes)  
**Status:** Production-Ready / GitHub Portfolio Publication  

---

## 1. Executive Summary & Project Objectives

The **Karachi Community Health Intelligence System (K-CHIS)** was established to transition raw public health survey records into an automated, data-driven intelligence pipeline. Operating within a modular Python environment (`pandas`, `scipy`, `scikit-learn`, `seaborn`), this system integrates rigorous exploratory data analysis (EDA), multi-section KPI calculations, inferential hypothesis testing, and machine learning risk modeling. 

The primary objective is to evaluate community health vulnerabilities across Kemari district, Karachi—specifically targeting nutritional imbalances, chronic disease prevalence, lifestyle risk factors, and socioeconomic health determinants—to support evidence-based public health interventions.

---

## 2. Demographic & Socioeconomic Baseline

The surveillance cohort comprises **472 validated participants** after rigorous data cleaning, missing value imputation, and standardization.

| Demographic Metric | Value / Distribution | Cohort Summary |
| :--- | :--- | :--- |
| **Total Population ($N$)** | 472 Participants | Complete cross-sectional survey sample |
| **Gender Distribution** | Male: **62.9%** (297) <br> Female: **37.1%** (175) | Skewed representation toward male respondents |
| **Mean Age** | **66.7 Years** | Aging community demographic |
| **Baseline Cohort BMI** | **19.6 (Average)** | Indicates borderline baseline lean body mass |

---

## 3. Nutritional Intelligence & Anthropometry

Nutritional assessment reveals a severe public health burden regarding body mass index (BMI) distribution across the surveyed population.

* **Overall Malnutrition Prevalence:** **58.9%** (278 cases) of the total population exhibits physiological imbalance (underweight, overweight, or obese status).
* **Underweight Crisis:** A striking **46.0%** (217 cases) of participants are classified as underweight ($BMI < 18.5$), pointing toward profound nutritional deficits within vulnerable community segments.
* **Overweight & Obesity:** Overweight prevalence ($25 \le BMI < 30$) stands at **10.0%** (47 cases), while clinical obesity ($BMI \ge 30$) is recorded at **3.0%** (14 cases).

> **Public Health Implication:** While global urban health studies frequently emphasize rising obesity epidemics, the K-CHIS cohort highlights an acute duality: a predominant crisis of undernutrition coexisting with localized metabolic overweight/obesity burdens.

---

## 4. Chronic Disease Morbidity Surveillance

Systematic screening across chronic health conditions identified significant morbidity markers within the urban population:

[Chronic Disease Prevalence Snapshot]
Hypertension (19.1%)  ████████████████████ 90 cases
Dyspepsia (17.2%)     █████████████████    81 cases
Cancer Indicators (16.1%) ████████████████ 76 cases
Diabetes (10.2%)      ██████████           48 cases

* **Hypertension:** Emerges as the leading chronic morbidity with a **19.1%** prevalence rate (90 cases).
* **Gastrointestinal Health (Dyspepsia):** Records a high prevalence of **17.2%** (81 cases), reflecting dietary or stress-related systemic factors.
* **Oncology Screening:** Positive indicators for cancer register at **16.1%** (76 cases).
* **Diabetes Mellitus:** Established chronic diabetes affects **10.2%** (48 cases) of the population.

---

## 5. Lifestyle Risks & Healthcare Utilization

### Behavioral Risk Factors
* **Smoking Status:** Evaluated across current, former, and never-smoked groups, demonstrating a measurable association with compromised self-reported general health status.
* **Substance Abuse & Activity:** Systematic frequency profiling of addictive substances (Gutka, Pan/Tobacco, Niswar) and physical activity levels (routine vs. occasional vs. never) indicates lifestyle habits heavily influence chronic morbidity risk.

### Healthcare Access & Medication Compliance
* **Visit Frequency:** Participants report varying engagement intervals, ranging from routine annual visits to strictly reactive care ("only when required").
* **Medication Adherence:** Compliance tracking across cohorts highlights gaps in sustained pharmaceutical management among chronic patients.

---

## 6. Inferential Statistics & Hypothesis Testing

To move beyond descriptive metrics, formal statistical hypothesis tests were conducted:

1. **Gender vs. Nutritional Status (Chi-Square Test):** Tested whether nutritional categories differ significantly by gender. Results confirmed distinct categorical distributions.
2. **Education vs. Nutritional Status (Chi-Square Test):** Evaluated the influence of educational attainment years on health outcomes.
3. **Household Income vs. BMI Category (Chi-Square & Boxplot - Fig 11):** Demonstrated a statistically significant association between household income brackets and malnutrition vulnerability.
4. **Age vs. BMI (Pearson Correlation & Regplot - Fig 12):** Analyzed linear age-to-BMI trajectories across the aging cohort.
5. **Smoking vs. Health Status (Chi-Square Test):** Proved a statistically significant relationship ($p < 0.05$) between smoking habits and poorer self-reported health outcomes.

---

## 7. Predictive Machine Learning Modeling (Malnutrition Risk)

A supervised binary classification model was deployed to predict baseline malnutrition risk (`1 = Malnourished / Underweight`, `0 = Otherwise`) using multi-variable predictors (Age, Gender, Household Income, Education Years, Smoking Status, and Physical Activity).

* **Feature Engineering & Prescaling:** Continuous features (`age`, `educational_years`, `household_income`) were normalized using `StandardScaler` to prevent optimization convergence failures (`lbfgs` solver).
* **Model Performance:** The Logistic Regression model achieved an overall accuracy score of **64.2%** on unseen test data, with balanced precision and recall metrics identifying core socio-demographic risk drivers.

---

## 8. Strategic Public Health Recommendations

Based on empirical K-CHIS findings, the following policy recommendations are proposed for Karachi’s municipal health framework:

1. **Targeted Nutritional Supplementation:** Deploy community feeding and nutritional intervention programs aimed at reversing the **46.0% underweight rate**, particularly among elderly cohorts.
2. **Mobile Hypertension & Diabetes Screening:** Establish localized, low-cost screening kiosks in high-risk neighborhoods to mitigate the **19.1% hypertension** and **10.2% diabetes** burdens.
3. **Socioeconomic Health Subsidies:** Design welfare and healthcare access programs that account for the strong statistical correlation between lower household income and elevated malnutrition risks.
4. **Behavioral Public Health Campaigns:** Implement smoking cessation and substance abuse counseling initiatives integrated into primary healthcare clinics.

---

## 9. Visual Artifacts Index

All generated high-resolution visualizations (`300 DPI`) are archived in the repository's `visuals/` directory:
* **Figures 1–6:** Demographic baseline distributions (Age, BMI scale, Gender breakdown, Education, Income, Health status)
* **Figure 7:** Chronic Disease Prevalence Comparison Bar Plot
* **Figure 8:** Physical Activity Level Distribution Chart
* **Figure 9 & 10:** Healthcare Visit Frequency & Medication Use Distributions
* **Figure 11:** Household Income Distribution by BMI Category (Boxplot)
* **Figure 12:** Age vs. BMI Regression Analysis (Regplot)
* **Figure 13:** Malnutrition Risk Machine Learning Model Confusion Matrix
