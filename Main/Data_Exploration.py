'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - Data_Exploration.py
24 Oct 2024
**
'''
#This script is used to explore the medical insurance dataset and provide an overview of the data.
import pandas as pd

def run(df):
    output = []
    #remove duplicate rows
    df_cleaned = df.drop_duplicates()

    #display basic information about the dataset
    output.append("dataset overview:")
    output.append(str(df_cleaned.info()))  #show data types, non-null counts, and memory usage
    output.append("\nfirst few rows of the dataset:")
    output.append(str(df_cleaned.head()))  #display the first few rows for inspection

    #describe the dataset to understand numerical attributes
    output.append("\nsummary statistics for numerical columns:")
    output.append(str(df_cleaned.describe()))  #show summary statistics for quantitative attributes

    #identify column types
    quantitative_columns = df_cleaned.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_columns = df_cleaned.select_dtypes(include=['object']).columns.tolist()

    output.append(f"\nquantitative columns: {quantitative_columns}")
    output.append(f"categorical/qualitative columns: {categorical_columns}")

    #check for unwanted columns (columns with mostly missing values or redundant information)
    missing_data = df_cleaned.isnull().sum()
    output.append("\nmissing data per column:")
    output.append(str(missing_data))

    #identify columns with more than 50% missing values
    columns_to_remove = missing_data[missing_data > (0.5 * len(df_cleaned))].index.tolist()
    output.append(f"\ncolumns to potentially remove (more than 50% missing values): {columns_to_remove}")

    #if there are unwanted columns, drop them
    if columns_to_remove:
        df_cleaned = df_cleaned.drop(columns=columns_to_remove)
        output.append(f"\nupdated dataset shape after removing unwanted columns: {df_cleaned.shape}")
    else:
        output.append("\nno columns were removed as all have sufficient data.")

    #display final column list after removing unwanted columns
    output.append("\nfinal column list:")
    output.append(str(df_cleaned.columns.tolist()))

    return "\n".join(output)