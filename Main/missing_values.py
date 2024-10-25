'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - missing_values.py
24 Oct 2024
**
'''
#This script is used to handle missing values in the dataset. 
import pandas as pd
#function to handle missing values in the dataset
def run(df):
    output = []
    #remove duplicate rows to clean up data
    df_cleaned = df.drop_duplicates()

    #check for missing values
    output.append("missing values before treatment:")
    output.append(str(df_cleaned.isnull().sum()))

    #option 1: delete rows with missing values if they are few
    #df_cleaned = df_cleaned.dropna()

    #missing values with median for continuous variables
    continuous_columns = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
    #fill missing values with the median for each continuous column
    for column in continuous_columns:
        if df_cleaned[column].isnull().sum() > 0:
            median_value = df_cleaned[column].median()
            df_cleaned[column].fillna(median_value, inplace=True)
            output.append(f"filled missing values in '{column}' with median value: {median_value}")

    #option 3: impute missing values with mode for categorical variables
    categorical_columns = df_cleaned.select_dtypes(include=['object']).columns
    #fill missing values with the most frequent value (mode) for each categorical column
    for column in categorical_columns:
        if df_cleaned[column].isnull().sum() > 0:
            mode_value = df_cleaned[column].mode()[0]  #get the most frequent value
            df_cleaned[column].fillna(mode_value, inplace=True)
            output.append(f"filled missing values in '{column}' with mode value: {mode_value}")

    #option 4: interpolate missing values based on nearby values
    #We removed this option as it may not be suitable for all datasets
    #df_cleaned = df_cleaned.interpolate(method='linear')

    #check for missing values again after treatment
    output.append("\nmissing values after treatment:")
    output.append(str(df_cleaned.isnull().sum()))

    #display a sample of the cleaned data
    output.append("\nsample data after missing value treatment:")
    output.append(str(df_cleaned.head()))

    return "\n".join(output)
