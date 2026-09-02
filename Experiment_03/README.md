# Experiment 03: Preprocessing & Distance Metrics

## Aim
To impute missing values and analyze variable relationships and sample similarities.

## Pearson Correlation Matrix
|                          |   Pregnancies |   Glucose |   BloodPressure |   SkinThickness |   Insulin |       BMI |   DiabetesPedigreeFunction |       Age |   Outcome |
|:-------------------------|--------------:|----------:|----------------:|----------------:|----------:|----------:|---------------------------:|----------:|----------:|
| Pregnancies              |     1         |  0.128213 |      0.208615   |       0.0817698 | 0.0250475 | 0.0215587 |                -0.0335227  | 0.544341  |  0.221898 |
| Glucose                  |     0.128213  |  1        |      0.218937   |       0.192615  | 0.419451  | 0.231049  |                 0.137327   | 0.266909  |  0.492782 |
| BloodPressure            |     0.208615  |  0.218937 |      1          |       0.191892  | 0.0453633 | 0.281257  |                -0.00237834 | 0.324915  |  0.165723 |
| SkinThickness            |     0.0817698 |  0.192615 |      0.191892   |       1         | 0.15561   | 0.543205  |                 0.102188   | 0.126107  |  0.214873 |
| Insulin                  |     0.0250475 |  0.419451 |      0.0453633  |       0.15561   | 1         | 0.180241  |                 0.126503   | 0.0971012 |  0.20379  |
| BMI                      |     0.0215587 |  0.231049 |      0.281257   |       0.543205  | 0.180241  | 1         |                 0.153438   | 0.0255969 |  0.312038 |
| DiabetesPedigreeFunction |    -0.0335227 |  0.137327 |     -0.00237834 |       0.102188  | 0.126503  | 0.153438  |                 1          | 0.0335613 |  0.173844 |
| Age                      |     0.544341  |  0.266909 |      0.324915   |       0.126107  | 0.0971012 | 0.0255969 |                 0.0335613  | 1         |  0.238356 |
| Outcome                  |     0.221898  |  0.492782 |      0.165723   |       0.214873  | 0.20379   | 0.312038  |                 0.173844   | 0.238356  |  1        |

## Distance Comparison Table
| Metric    |         Raw |    MinMax |   Standardized |
|:----------|------------:|----------:|---------------:|
| Euclidean |  66.9035    | 0.627987  |        3.39903 |
| Manhattan | 106.276     | 1.40468   |        8.20425 |
| Cosine    |   0.0316227 | 0.0915996 |        1.58472 |

## Student Questions & Answers
1. **Why impute with median?** Median is robust to outliers, which are present in columns like Insulin.
2. **Which pair has the highest correlation?** Glucose and Outcome show a strong correlation (0.49).
3. **How does scaling affect distance?** Raw Euclidean distance is dominated by variables with large ranges (like Insulin), while scaling provides an equal weight to all features.
