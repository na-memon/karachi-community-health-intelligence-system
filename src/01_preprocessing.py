## Preprocessing Module

import pandas as pd


def clean_health_data(filepath):
  """Loads the raw Karachi health dataset, handles missing values,

  normalizes text, fixes typos, enforces data types, and drops duplicates.
  """
  # 1. Load data
  df = pd.read_excel(filepath)

  # 2. Handle missing values
  if "dependents" in df.columns:
    df["dependents"] = df["dependents"].fillna(df["dependents"].median())

  categorical_fill_cols = ["supplements", "wrokpreference"]
  for col in categorical_fill_cols:
    if col in df.columns:
      df[col] = df[col].fillna("unknown")

  if "addictive_substance" in df.columns:
    df["addictive_substance"] = df["addictive_substance"].fillna("none")

  # 3. Normalize text (lowercase & strip)
  string_cols = df.select_dtypes(include=["object", "str"]).columns
  for col in string_cols:
    df[col] = df[col].str.lower().str.strip()

  # 4. Fix specific typos
  if "nutritional_scale" in df.columns:
    df["nutritional_scale"] = df["nutritional_scale"].replace(
        "normal weihgt", "normal weight"
    )

  # 5. Enforce data types
  int_cols = ["age", "educational_years", "household_income"]
  for col in int_cols:
    if col in df.columns:
      df[col] = df[col].astype(int)

  float_cols = ["height_m", "weight_kg", "bmi", "dependents"]
  for col in float_cols:
    if col in df.columns:
      df[col] = df[col].astype(float)

  categorical_cols = [
      "gender",
      "nutritional_scale",
      "marital_status",
      "ethinicity",
      "family_status",
      "living_status",
      "economic_dependency",
      "decision_making",
      "health_status",
      "hypertension",
      "dyspepsia",
      "cancer",
      "diabetes",
      "healthcare_visits",
      "taking_medicines",
      "take_care_during_illness",
      "supplements",
      "smoking_status",
      "smoking_routine",
      "types_of_beverages",
      "substance_abuse",
      "addictive_substance",
      "physical_activity",
      "servings6_11bread",
      "serving2_4fruit",
      "serving3_5vegetables",
      "servings2_3dairy",
      "serving2_3meat",
      "fattype",
      "householdactivity",
      "wrokpreference",
      "sleepingtime",
      "sleepiingpills",
  ]

  for col in categorical_cols:
    if col in df.columns:
      df[col] = df[col].astype("category")

  # 6. Drop duplicate rows
  df = df.drop_duplicates().reset_index(drop=True)

  return df