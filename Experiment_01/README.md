# Experiment 01: Data Quality and EDA

## Aim
To assess the quality of the Pima Indians Diabetes Dataset by identifying missing values (zeros) and outliers.

## Dataset Summary Table
| Variable                 | Dtype   |   Zeros |   Outliers |
|:-------------------------|:--------|--------:|-----------:|
| Pregnancies              | int64   |       0 |          4 |
| Glucose                  | int64   |       5 |          5 |
| BloodPressure            | int64   |      35 |         45 |
| SkinThickness            | int64   |     227 |          1 |
| Insulin                  | int64   |     374 |         34 |
| BMI                      | float64 |      11 |         19 |
| DiabetesPedigreeFunction | float64 |       0 |         29 |
| Age                      | int64   |       0 |          9 |
| Outcome                  | int64   |       0 |          0 |

## Student Questions & Answers
1. **Are there missing values?** Yes, biologically unrealistic zeros in Glucose, BloodPressure, SkinThickness, Insulin, and BMI function as missing data.
2. **Which variable has the most outliers?** Insulin contains the highest number of outliers based on IQR bounds.
3. **Is the dataset balanced?** No, Outcome 0 (Non-Diabetic) is more frequent than Outcome 1.
4. **Data Types?** All features are numerical (int64 or float64).
