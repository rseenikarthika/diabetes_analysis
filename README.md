# Diabetes Data Engineering & Analysis Challenge

## Project Overview
This repository contains a complete workflow for **Diabetes Prediction Data Engineering and Analysis**. The project includes **data validation, cleaning, feature engineering, exploratory data analysis (EDA), risk group statistics, feature distributions, and multicollinearity checks**.

The dataset used is the **Diabetes Prediction Dataset** with the following features:

- `gender`
- `age`
- `hypertension`
- `heart_disease`
- `smoking_history`
- `bmi`
- `HbA1c_level`
- `blood_glucose_level`
- `diabetes` (Target: 0 = No, 1 = Yes)

---

## Project Structure
```
diabetes_analysis/
│
├─ analysis.py             # EDA notebook/script
├─ etl.py                  # Data validation & ETL pipeline
├─ dataset.csv             # Original dataset
├─ train.csv               # Cleaned & split training data
├─ test.csv                # Cleaned & split test data
├─ risk_groups.csv         # Diabetes prevalence in risk cohorts
├─ correlation.json        # Pearson correlation of numeric features vs diabetes
├─ multicollinearity.txt   # High correlation warnings among numeric predictors
├─ out/                    # Folder containing plots
├─ requirements.txt        # Python dependencies
└─ env/                    # Virtual environment (optional)
```

---

## Part 1: Data Validation & ETL
Implemented in `etl.py`:

- **Schema Validation**: Ensures correct data types and expected columns.
- **Cleaning & Quarantine**: Handles missing or invalid values.
- **Encoding & Z-Score Scaling**: Encodes categorical variables and scales numeric features.
- **Stratified Split**: Splits dataset into training and testing while preserving class distribution.

Output: Cleaned datasets (`train.csv`, `test.csv`) ready for analysis.

---

## Part 2: Exploratory Data Analysis (EDA)

Implemented in `analysis.py`:

### 1. Summary Statistics
- Mean, Std, Min, Median, Max, % Missing for numeric columns: `age`, `bmi`, `HbA1c_level`, `blood_glucose_level`.
- Counts of males vs females.
- Smoking history counts.
- Diabetes prevalence (%).

### 2. Correlation & Feature Insights
- Pearson correlation between numeric features and diabetes.
- Sorted table of correlations saved as `correlation.json`.
- Optional heatmap visualization of correlations.

### 3. Risk Group Statistics
Diabetes prevalence for specific cohorts:
- Elderly (`age ≥ 60`)
- Overweight (`BMI ≥ 30`)
- Hypertension (`hypertension = 1`)
- Heart Disease (`heart_disease = 1`)
- High Glucose (`blood_glucose_level ≥ 180`)
- Smokers (`smoking_history ∈ {current, ever, former}`)

Saved as `risk_groups.csv`.

### 4. Feature Distributions
Plots saved to `/out/plots/`:
- Histograms for numeric features.
- Boxplots grouped by diabetes.
- Bar chart of smoking history vs diabetes prevalence.

### 5. Multicollinearity Check
- Correlation matrix among numeric predictors.
- Flags high correlations (|r| > 0.8).
- Warnings saved in `multicollinearity.txt`.

---

## How to Run

1. **Clone the repository**
```bash
git clone https://github.com/rseenikarthika/diabetes_analysis
cd diabetes_analysis
```

2. **Create environment & install dependencies**
```bash
python -m venv env
source env/bin/activate      # Linux/Mac
env\Scripts\activate       # Windows
pip install -r requirements.txt
```

3. **Run ETL**
```bash
python etl.py
```

4. **Run Analysis**
```bash
python analysis.py
```

---

## Requirements
- Python 3.9+
- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- json

---

## Output
After running the scripts:

- Cleaned datasets: `train.csv`, `test.csv`
- Risk group statistics: `risk_groups.csv`
- Correlations: `correlation.json`
- Multicollinearity warnings: `multicollinearity.txt`
- Plots: `/out/plots/`  

---

## License
This project is open source and free to use under the MIT License.
