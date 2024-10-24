'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - correlationmatrix.py
24 Oct 2024
**
'''
#This script is used to analyze the correlation between variables in the medical insurance dataset.
#Requires the modules pandas, matplotlib, seaborn, and scipy to be installed along with the dataset file "Medical_insurance.csv".
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats #import the stats module from scipy library

#load the dataset from csv file
file_path = "Medical_insurance.csv" 
#Read the dataset from the file path
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

#anova test for categorical variables - check if there is a significant difference in charges based on categories
categorical_columns = ['sex', 'smoker', 'region']  #original categorical columns
#initialize dictionary to store anova results
anova_results = {}
#perform anova test for each categorical variable
for column in categorical_columns:
    anova_groups = medical_insurance_df_cleaned.groupby(column)['charges'].apply(list) #group charges by category
    f_val, p_val = stats.f_oneway(*anova_groups) #perform anova test
    anova_results[column] = (f_val, p_val) #store the results
#convert the results to a dataframe for better visualization
anova_df = pd.DataFrame(anova_results, index=["F-value", "p-value"]).T
print("\nanova test results:\n", anova_df)

#display significant categorical variables (p < 0.05)
significant_categorical = anova_df[anova_df["p-value"] < 0.05]
print("\nsignificant categorical features (p < 0.05):\n", significant_categorical)

#visualize the relationship between region and charges
plt.figure(figsize=(10, 6)) #set the figure size (width, height)
sns.boxplot(x='region', y='charges', data=medical_insurance_df_cleaned) #create a box plot
plt.title('box plot of charges by region') #set the title of the plot
plt.ylabel('charges ($)') #set the y-axis label
plt.xlabel('region') #set the x-axis label
plt.grid(True) #display grid lines
plt.show() #display the plot
