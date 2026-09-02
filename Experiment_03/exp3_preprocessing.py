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
# Experiment 3: Preprocessing & Distances
plt.figure(figsize=(10,8))
sns.heatmap(df_clean.corr(), annot=True, cmap='coolwarm')
plt.savefig('plots/correlation.png')

# Distances between first two patients
p1, p2 = df_clean.drop('Outcome', axis=1).iloc[0], df_clean.drop('Outcome', axis=1).iloc[1]
print(f'Euclidean: {euclidean(p1, p2)}')
