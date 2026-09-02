# Experiment 02: Descriptive Statistics and Visualization

## Aim
To compute summary statistics and visualize feature distributions and relationships.

## Descriptive Statistics Summary
|                          |       mean |        std |    min |    max |     variance |      IQR |
|:-------------------------|-----------:|-----------:|-------:|-------:|-------------:|---------:|
| Pregnancies              |   3.84505  |   3.36958  |  0     |  17    |    11.3541   |   5      |
| Glucose                  | 120.895    |  31.9726   |  0     | 199    |  1022.25     |  41.25   |
| BloodPressure            |  69.1055   |  19.3558   |  0     | 122    |   374.647    |  18      |
| SkinThickness            |  20.5365   |  15.9522   |  0     |  99    |   254.473    |  32      |
| Insulin                  |  79.7995   | 115.244    |  0     | 846    | 13281.2      | 127.25   |
| BMI                      |  31.9926   |   7.88416  |  0     |  67.1  |    62.16     |   9.3    |
| DiabetesPedigreeFunction |   0.471876 |   0.331329 |  0.078 |   2.42 |     0.109779 |   0.3825 |
| Age                      |  33.2409   |  11.7602   | 21     |  81    |   138.303    |  17      |
| Outcome                  |   0.348958 |   0.476951 |  0     |   1    |     0.227483 |   1      |

## Visualization Findings
- **Glucose**: Shows a roughly normal distribution but with a small peak at zero (missing data).
- **Outcome Relationship**: The BMI boxplot indicates that diabetic patients tend to have a higher median BMI compared to non-diabetic patients.
- **Glucose vs BMI**: Positive relationship observed; higher glucose levels often coincide with higher BMI.

## Student Questions & Answers
1. **What is the mean Age?** 33.24
2. **Which variable has the highest variance?** Insulin (13281.18)
3. **Is there a relationship between Glucose and BMI?** Yes, a general positive trend is visible in scatter plots.
