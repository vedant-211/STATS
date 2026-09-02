import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats
from scipy.spatial.distance import euclidean, cityblock, cosine
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 1. Load Data
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df = pd.read_csv(url, names=cols)

# 2. Preprocessing (Handling Zeros as Missing)
medical_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df_clean = df.copy()
for col in medical_cols:
    df_clean[col] = df_clean[col].replace(0, np.nan)
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())
# Experiment 1: EDA & Data Quality
print('--- Data Quality Analysis ---')
for col in df.columns:
    zeros = (df[col]==0).sum() if col not in ['Pregnancies', 'Outcome'] else 0
    print(f'{col}: Zeros={zeros}')

# Outlier detection
Q1 = df_clean.quantile(0.25)
Q3 = df_clean.quantile(0.75)
IQR = Q3 - Q1
outliers = ((df_clean < (Q1 - 1.5 * IQR)) | (df_clean > (Q3 + 1.5 * IQR))).sum()
print('
Outliers per column:
', outliers)
