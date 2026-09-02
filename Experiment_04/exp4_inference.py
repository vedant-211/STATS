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
# Experiment 4: Inference
t_stat, p_val = stats.ttest_1samp(df_clean['Glucose'], 120)
print(f'One-sample t-test p-value: {p_val}')
# CI for Proportion
p_hat = df_clean['Outcome'].mean()
ci = stats.norm.interval(0.95, loc=p_hat, scale=np.sqrt(p_hat*(1-p_hat)/len(df_clean)))
print(f'95% CI for Outcome: {ci}')
