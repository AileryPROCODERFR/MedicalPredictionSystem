import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset from csv file
file_path = "Medical_insurance.csv"  #update this path to match your file location
medical_insurance_df = pd.read_csv(file_path)

#remove duplicate rows
medical_insurance_df_cleaned = medical_insurance_df.drop_duplicates()

#identify and remove outliers using the iqr method
quantitative_columns = medical_insurance_df_cleaned.select_dtypes(include=['float64', 'int64']).columns

for column in quantitative_columns:
    #calculate q1 (25th percentile) and q3 (75th percentile)
    Q1 = medical_insurance_df_cleaned[column].quantile(0.25)
    Q3 = medical_insurance_df_cleaned[column].quantile(0.75)
    IQR = Q3 - Q1  #interquartile range

    #define outlier bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    #remove outliers
    medical_insurance_df_cleaned = medical_insurance_df_cleaned[
        (medical_insurance_df_cleaned[column] >= lower_bound) &
        (medical_insurance_df_cleaned[column] <= upper_bound)
    ]

#identify cleaned quantitative and categorical columns
quantitative_columns_cleaned = medical_insurance_df_cleaned.select_dtypes(include=['float64', 'int64']).columns.tolist()
categorical_columns_cleaned = medical_insurance_df_cleaned.select_dtypes(include=['object']).columns.tolist()

#visualize the cleaned data

#set up the figure for plotting histograms of quantitative variables
plt.figure(figsize=(12, 8))  #adjust the figure size to fit within your screen dimensions
for i, column in enumerate(quantitative_columns_cleaned[:4], 1):  #show the first 4 quantitative variables
    plt.subplot(2, 2, i)  #create a 2x2 grid
    sns.histplot(medical_insurance_df_cleaned[column], bins=20, kde=True, color='skyblue')
    plt.title(f'distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('frequency')
    plt.grid(True)

#adjust layout for better spacing
plt.tight_layout()
plt.show()

#set up the figure for plotting bar charts of categorical variables
plt.figure(figsize=(12, 8))  #adjust the figure size
for i, column in enumerate(categorical_columns_cleaned[:4], 1):  #show the first 4 categorical variables
    plt.subplot(2, 2, i)  #create a 2x2 grid
    sns.countplot(data=medical_insurance_df_cleaned, x=column, palette='viridis')
    plt.title(f'distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('count')
    plt.grid(True, axis='y')

#adjust layout for better spacing
plt.tight_layout()
plt.show()