import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit

# Load CSV
df = pd.read_csv("dataset.csv")

# --- Schema validation ---
required_cols = ['gender','age','hypertension','heart_disease',
                 'smoking_history','bmi','HbA1c_level','blood_glucose_level','diabetes']
missing_cols = [c for c in required_cols if c not in df.columns]
if missing_cols:
    raise ValueError(f"Missing columns: {missing_cols}")

# --- Cleaning ---
df = df.dropna(subset=['age','bmi','HbA1c_level','blood_glucose_level','diabetes'])
df = df[df['age'] > 0]

# --- Encoding categorical variables ---
df['gender'] = df['gender'].map({'Male':0,'Female':1})
df['smoking_history'] = df['smoking_history'].map({'never':0,'current':1,'former':2,'ever':3})

# --- Scaling numeric features ---
scaler = StandardScaler()
for col in ['age','bmi','HbA1c_level','blood_glucose_level']:
    df[col] = scaler.fit_transform(df[[col]])

# --- Stratified split ---
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_idx, test_idx in split.split(df, df['diabetes']):
    train_df = df.iloc[train_idx]
    test_df = df.iloc[test_idx]

train_df.to_csv("train.csv", index=False)
test_df.to_csv("test.csv", index=False)
print("ETL complete. Train/test CSVs saved.")
