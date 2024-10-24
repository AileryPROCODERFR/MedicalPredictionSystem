'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - missing_values.py
24 Oct 2024
**
'''
import pandas as pd

def run(df):
    output = []
    #remove duplicate rows
    df_cleaned = df.drop_duplicates()

    #check for missing values
    output.append("missing values before handling:")
    output.append(str(df_cleaned.isnull().sum()))

    #identify and remove outliers using the iqr method
    quantitative_columns = df_cleaned.select_dtypes(include=['float64', 'int64']).columns

    for column in quantitative_columns:
        #calculate q1 (25th percentile) and q3 (75th percentile)
        Q1 = df_cleaned[column].quantile(0.25)
        Q3 = df_cleaned[column].quantile(0.75)
        IQR = Q3 - Q1  #interquartile range

        #define outlier bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        #remove outliers
        df_cleaned = df_cleaned[
            (df_cleaned[column] >= lower_bound) &
            (df_cleaned[column] <= upper_bound)
        ]

    #check for missing values again after removing outliers
    output.append("\nmissing values after handling outliers:")
    output.append(str(df_cleaned.isnull().sum()))

    #display the shape of the dataset before and after outlier removal
    output.append(f"\noriginal dataset shape: {df.shape}")
    output.append(f"dataset shape after outlier removal: {df_cleaned.shape}")

    #display a sample of the cleaned data
    output.append("\nsample data after outlier removal:")
    output.append(str(df_cleaned.head()))

    return "\n".join(output)
