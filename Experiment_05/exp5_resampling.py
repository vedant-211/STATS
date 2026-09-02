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
# Experiment 5: Resampling
boot_means = [df_clean['Glucose'].sample(frac=1, replace=True).mean() for _ in range(1000)]
print(f'Bootstrap 95% CI: {np.percentile(boot_means, [2.5, 97.5])}')
