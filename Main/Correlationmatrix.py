'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - correlationmatrix.py
24 Oct 2024
**
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#load the dataset from csv file
file_path = "Medical_insurance.csv"  #dataset file location
medical_insurance_df = pd.read_csv(file_path)

#remove duplicate rows
medical_insurance_df_cleaned = medical_insurance_df.drop_duplicates()

#convert categorical variables to dummy variables
medical_insurance_df_encoded = pd.get_dummies(medical_insurance_df_cleaned, drop_first=True)

#correlation analysis for continuous variables
quantitative_columns = medical_insurance_df_encoded.select_dtypes(include=['float64', 'int64']).columns.tolist()
correlation_matrix = medical_insurance_df_encoded[quantitative_columns].corr()

#plot correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('correlation matrix (continuous variables)')
plt.show()

#anova test for categorical variables
categorical_columns = ['sex', 'smoker', 'region']  #original categorical columns
anova_results = {}

for column in categorical_columns:
    anova_groups = medical_insurance_df_cleaned.groupby(column)['charges'].apply(list)
    f_val, p_val = stats.f_oneway(*anova_groups)
    anova_results[column] = (f_val, p_val)

anova_df = pd.DataFrame(anova_results, index=["F-value", "p-value"]).T
print("\nanova test results:\n", anova_df)

#display significant categorical variables (p < 0.05)
significant_categorical = anova_df[anova_df["p-value"] < 0.05]
print("\nsignificant categorical features (p < 0.05):\n", significant_categorical)

#visualize the relationship between region and charges
plt.figure(figsize=(10, 6))
sns.boxplot(x='region', y='charges', data=medical_insurance_df_cleaned)
plt.title('box plot of charges by region')
plt.ylabel('charges ($)')
plt.xlabel('region')
plt.grid(True)
plt.show()
