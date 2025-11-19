import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import json

df = pd.read_csv("train.csv")
numeric_cols = ['age','bmi','HbA1c_level','blood_glucose_level']

# Create output folder
os.makedirs("out/plots", exist_ok=True)

# --- Summary Statistics ---
summary = df[numeric_cols].agg(['mean','std','min','median','max'])
summary['%missing'] = df[numeric_cols].isna().mean() * 100
print(summary)

# Demographics
print("Gender counts:\n", df['gender'].value_counts())
print("Smoking history counts:\n", df['smoking_history'].value_counts())
print("Diabetes prevalence: {:.2f}%".format(df['diabetes'].mean()*100))

# --- Correlation with diabetes ---
corr = df[numeric_cols + ['diabetes']].corr()['diabetes'].sort_values(ascending=False)
print("Correlation with diabetes:\n", corr)
corr.to_json("correlation.json")

# --- Risk group statistics ---
risk_conditions = {
    "Elderly": df['age'] >= 60,
    "Overweight": df['bmi'] >= 30,
    "Hypertension": df['hypertension'] == 1,
    "Heart Disease": df['heart_disease'] == 1,
    "High Glucose": df['blood_glucose_level'] >= 180,
    "Smokers": df['smoking_history'].isin([1,2,3])
}

risk_data = []
for cohort, condition in risk_conditions.items():
    subset = df[condition]
    risk_data.append([cohort, len(subset), round(subset['diabetes'].mean()*100,2)])

risk_df = pd.DataFrame(risk_data, columns=['Cohort','N','Diabetes %'])
risk_df.to_csv("risk_groups.csv", index=False)

# --- Feature distributions ---
for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.savefig(f"out/plots/{col}_hist.png")
    plt.close()

    plt.figure()
    sns.boxplot(x='diabetes', y=col, data=df)
    plt.savefig(f"out/plots/{col}_box.png")
    plt.close()

plt.figure()
sns.barplot(x='smoking_history', y='diabetes', data=df)
plt.savefig("out/plots/smoking_diabetes.png")
plt.close()

# --- Multicollinearity ---
corr_matrix = df[numeric_cols].corr()
with open("multicollinearity.txt", "w") as f:
    for i in numeric_cols:
        for j in numeric_cols:
            if i != j and abs(corr_matrix.loc[i,j]) > 0.8:
                f.write(f"⚠️ High correlation between {i} and {j} = {corr_matrix.loc[i,j]:.2f}\n")

print("Analysis complete. Plots and CSVs saved.")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import json

df = pd.read_csv("train.csv")
numeric_cols = ['age','bmi','HbA1c_level','blood_glucose_level']

# Create output folder
os.makedirs("out/plots", exist_ok=True)

# --- Summary Statistics ---
summary = df[numeric_cols].agg(['mean','std','min','median','max'])
summary['%missing'] = df[numeric_cols].isna().mean() * 100
print(summary)

# Demographics
print("Gender counts:\n", df['gender'].value_counts())
print("Smoking history counts:\n", df['smoking_history'].value_counts())
print("Diabetes prevalence: {:.2f}%".format(df['diabetes'].mean()*100))

# --- Correlation with diabetes ---
corr = df[numeric_cols + ['diabetes']].corr()['diabetes'].sort_values(ascending=False)
print("Correlation with diabetes:\n", corr)
corr.to_json("correlation.json")

# --- Risk group statistics ---
risk_conditions = {
    "Elderly": df['age'] >= 60,
    "Overweight": df['bmi'] >= 30,
    "Hypertension": df['hypertension'] == 1,
    "Heart Disease": df['heart_disease'] == 1,
    "High Glucose": df['blood_glucose_level'] >= 180,
    "Smokers": df['smoking_history'].isin([1,2,3])
}

risk_data = []
for cohort, condition in risk_conditions.items():
    subset = df[condition]
    risk_data.append([cohort, len(subset), round(subset['diabetes'].mean()*100,2)])

risk_df = pd.DataFrame(risk_data, columns=['Cohort','N','Diabetes %'])
risk_df.to_csv("risk_groups.csv", index=False)

# --- Feature distributions ---
for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.savefig(f"out/plots/{col}_hist.png")
    plt.close()

    plt.figure()
    sns.boxplot(x='diabetes', y=col, data=df)
    plt.savefig(f"out/plots/{col}_box.png")
    plt.close()

plt.figure()
sns.barplot(x='smoking_history', y='diabetes', data=df)
plt.savefig("out/plots/smoking_diabetes.png")
plt.close()

# --- Multicollinearity ---
corr_matrix = df[numeric_cols].corr()
with open("multicollinearity.txt", "w") as f:
    for i in numeric_cols:
        for j in numeric_cols:
            if i != j and abs(corr_matrix.loc[i,j]) > 0.8:
                f.write(f"⚠️ High correlation between {i} and {j} = {corr_matrix.loc[i,j]:.2f}\n")

print("Analysis complete. Plots and CSVs saved.")
