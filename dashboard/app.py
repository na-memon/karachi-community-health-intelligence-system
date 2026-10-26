from pathlib import Path
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Karachi Community Health Intelligence System (K-CHIS)",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------
# Directory & Path Resolution (Local & Cloud Compatible)
# ----------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
VISUALS_DIR = PROJECT_ROOT / "visuals"
DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "Karachi Community Health Surveillance Analytics System_cleaned.xlsx"
)


@st.cache_data
def load_data():
  if DATA_PATH.exists():
    return pd.read_excel(DATA_PATH)
  return None


df = load_data()

# ----------------------------------------------------
# Navigation Sidebar
# ----------------------------------------------------
st.sidebar.image(
    "https://img.icons8.com/color/96/hospital-3.png", width=70
)  # Professional Header Icon
st.sidebar.title("K-CHIS Navigation")
page = st.sidebar.radio(
    "Select Analysis Module:",
    [
        "1. Executive Overview",
        "2. Demographic & Population KPIs",
        "3. Nutritional & Malnutrition Profile",
        "4. Chronic Disease Surveillance",
        "5. Lifestyle & Behavioral Risk Mapping",
        "6. Statistical & Predictive Insights",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "**System Status:** Online 🟢\n\n**Cohort Sample Size:** N = 472\n\n**Author:**"
    " Public Health Analytics Team"
)

# ----------------------------------------------------
# Page 1: Executive Overview
# ----------------------------------------------------
if page == "1. Executive Overview":
  st.title(
      "🏥 Karachi Community Health Intelligence System (K-CHIS)"
  )
  st.subheader(
      "Executive Intelligence Platform & Population Health Surveillance"
  )

  # Executive KPI Cards
  col1, col2, col3, col4 = st.columns(4)
  col1.metric(
      "Total Cohort (N)",
      f"{len(df):,}" if df is not None else "472",
      "Verified Survey",
  )
  col2.metric("Malnutrition Rate", "58.9%", delta="Critical Priority")
  col3.metric("Hypertension Rate", "19.1%", delta="High Risk")
  col4.metric("Diabetes Prevalence", "10.2%", delta="Elevated")

  st.markdown("---")

  col_text, col_img = st.columns([1.2, 1])

  with col_text:
    st.markdown("""
        ### Strategic Overview & Mission
        The **Karachi Community Health Intelligence System (K-CHIS)** transforms primary community health survey data 
        into rigorous public health intelligence. Designed for health administrators, epidemiologists, and policymakers, 
        this platform delivers end-to-end visibility into urban health vulnerabilities across Karachi.

        #### **Key Highlights:**
        * **Comprehensive Surveillance:** Tracks non-communicable diseases (NCDs), nutritional deficits, and socioeconomic determinants.
        * **Evidence-Based Insights:** Utilizes statistical hypothesis testing ($p < 0.05$) and machine learning predictive modeling.
        * **Actionable Decision Support:** Directs public health interventions toward high-risk demographics and communities.
        """)

  with col_img:
    fig_path = VISUALS_DIR / "fig6_health_status.png"
    if fig_path.exists():
      st.image(
          str(fig_path),
          caption="Fig 6: Overall Population Health Status",
          use_container_width=True,
      )
    else:
      st.warning("Visual asset `fig6_health_status.png` not found in visuals/")

  if df is not None:
    with st.expander("🔍 Preview Cleaned Surveillance Dataset (First 5 Rows)"):
      st.dataframe(df.head(), use_container_width=True)

# ----------------------------------------------------
# Page 2: Demographic & Population KPIs
# ----------------------------------------------------
elif page == "2. Demographic & Population KPIs":
  st.title("📊 Demographic & Population Profiling")
  st.write(
      "Analysis of baseline population characteristics, including age distribution, gender representation, educational attainment, and household economic status."
  )

  col1, col2 = st.columns(2)

  with col1:
    p1 = VISUALS_DIR / "fig1_age_distribution.png"
    if p1.exists():
      st.image(
          str(p1),
          caption="Fig 1: Cohort Age Distribution & Density",
          use_container_width=True,
      )

    p3 = VISUALS_DIR / "fig3_gender_distribution.png"
    if p3.exists():
      st.image(
          str(p3),
          caption="Fig 3: Gender Representation Breakdown",
          use_container_width=True,
      )

  with col2:
    p4 = VISUALS_DIR / "fig4_education_distribution.png"
    if p4.exists():
      st.image(
          str(p4),
          caption="Fig 4: Educational Attainment Tiers",
          use_container_width=True,
      )

    p5 = VISUALS_DIR / "fig5_income_distribution.png"
    if p5.exists():
      st.image(
          str(p5),
          caption="Fig 5: Household Income Distribution (PKR)",
          use_container_width=True,
      )

# ----------------------------------------------------
# Page 3: Nutritional & Malnutrition Profile
# ----------------------------------------------------
elif page == "3. Nutritional & Malnutrition Profile":
  st.title("🥗 Nutritional Assessment & Malnutrition Vulnerability")
  st.write(
      "Detailed clinical breakdown of nutritional status, BMI classifications, and economic correlations with malnutrition."
  )

  # Top KPI metrics for Nutrition
  col_m1, col_m2, col_m3, col_m4 = st.columns(4)
  col_m1.metric("Malnutrition Prevalence", "58.9%", delta="Critical")
  col_m2.metric("Underweight Rate", "46.0%", delta="BMI < 18.5")
  col_m3.metric("Normal Weight", "41.1%")
  col_m4.metric("Overweight / Obese", "12.9%")

  st.markdown("---")

  col1, col2 = st.columns(2)

  with col1:
    p2 = VISUALS_DIR / "fig2_bmi_classification.png"
    if p2.exists():
      st.image(
          str(p2),
          caption="Fig 2: BMI Classification & Weight Categories",
          use_container_width=True,
      )

  with col2:
    p11 = VISUALS_DIR / "fig11_income_by_bmi.png"
    if p11.exists():
      st.image(
          str(p11),
          caption="Fig 11: Household Income Stratified by BMI Status",
          use_container_width=True,
      )

# ----------------------------------------------------
# Page 4: Chronic Disease Surveillance
# ----------------------------------------------------
elif page == "4. Chronic Disease Surveillance":
  st.title("🫀 Chronic Morbidity & Non-Communicable Disease Surveillance")
  st.write(
      "Tracking prevalence rates for key chronic ailments, disease indicators, and patient medication patterns across the cohort."
  )

  col1, col2 = st.columns(2)

  with col1:
    p7 = VISUALS_DIR / "fig7_disease_prevalence.png"
    if p7.exists():
      st.image(
          str(p7),
          caption="Fig 7: Chronic Disease & Condition Prevalence Rates",
          use_container_width=True,
      )

  with col2:
    p10 = VISUALS_DIR / "fig10_medication_use.png"
    if p10.exists():
      st.image(
          str(p10),
          caption="Fig 10: Prescribed Medication & Treatment Usage Patterns",
          use_container_width=True,
      )

# ----------------------------------------------------
# Page 5: Lifestyle & Behavioral Risk Mapping
# ----------------------------------------------------
elif page == "5. Lifestyle & Behavioral Risk Mapping":
  st.title("🚬 Lifestyle Factors & Healthcare Utilization")
  st.write(
      "Evaluation of behavioral risk indicators (tobacco/gutka usage), physical activity baselines, and healthcare facility visit frequencies."
  )

  col1, col2 = st.columns(2)

  with col1:
    p8 = VISUALS_DIR / "fig8_physical_activity.png"
    if p8.exists():
      st.image(
          str(p8),
          caption="Fig 8: Physical Activity Index & Daily Routines",
          use_container_width=True,
      )

  with col2:
    p9 = VISUALS_DIR / "fig9_healthcare_visits.png"
    if p9.exists():
      st.image(
          str(p9),
          caption=(
              "Fig 9: Healthcare Facility Utilization & Consultation Frequencies"
          ),
          use_container_width=True,
      )

# ----------------------------------------------------
# Page 6: Statistical & Predictive Insights
# ----------------------------------------------------
elif page == "6. Statistical & Predictive Insights":
  st.title("🔬 Inferential Statistics & Predictive Machine Learning")
  st.markdown("""
    Advanced statistical modeling, correlation analyses, and predictive classification performance evaluating malnutrition risk.
    """)

  # Performance Metric Summary Box
  st.success(
      "💡 **Predictive Model Performance Summary:** Accuracy: **78.4%** |"
      " Precision: **0.79** | Recall: **0.82** | AUC-ROC: **0.84**"
  )

  col1, col2 = st.columns(2)

  with col1:
    p12 = VISUALS_DIR / "fig12_age_vs_bmi_regplot.png"
    if p12.exists():
      st.image(
          str(p12),
          caption="Fig 12: Age vs. BMI Regression & Trajectory Analysis",
          use_container_width=True,
      )

  with col2:
    p13 = VISUALS_DIR / "fig13_confusion_matrix.png"
    if p13.exists():
      st.image(
          str(p13),
          caption="Fig 13: Logistic Regression Model Confusion Matrix",
          use_container_width=True,
      )