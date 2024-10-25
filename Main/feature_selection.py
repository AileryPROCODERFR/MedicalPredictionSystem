'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - feature_selection.py
24 Oct 2024
**
'''
#This script is used to perform feature selection on the medical insurance dataset.
#required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
#load the dataset from csv file
def run(df):
    output = []
    #remove duplicate rows to ensure clean data
    df_cleaned = df.drop_duplicates()

    #define the target variable
    target_variable = 'charges'

    #visual analysis - scatter plots for continuous variables
    continuous_columns = df_cleaned.select_dtypes(include=['float64', 'int64']).columns.tolist()
    #remove the target variable from the list of continuous columns for scatter plots
    if target_variable in continuous_columns:
        continuous_columns.remove(target_variable)
    #plot scatter plots for each continuous variable against the target variable
    plt.figure(figsize=(16, 10))#set the figure size (width, height)
    for i, column in enumerate(continuous_columns, 1):
        plt.subplot(2, 3, i)
        sns.scatterplot(x=df_cleaned[column], y=df_cleaned[target_variable], color='skyblue')
        plt.title(f'scatter plot: {column} vs {target_variable}')
        plt.xlabel(column)
        plt.ylabel(target_variable)
    plt.tight_layout()
    plt.show()  #display the scatterplots
    #output the results
    output.append("scatter plots have been generated.")

    #statistical correlation analysis - pearson's correlation
    correlation_matrix = df_cleaned[continuous_columns + [target_variable]].corr()
    output.append("\npearson's correlation matrix:")
    output.append(str(correlation_matrix))

    #visual analysis - box plots for continuous vs. categorical variables
    categorical_columns = df_cleaned.select_dtypes(include=['object']).columns.tolist()
    #plot box plots for each categorical variable against the target variable
    plt.figure(figsize=(16, 10))
    for i, column in enumerate(categorical_columns, 1):
        plt.subplot(2, 3, i)
        sns.boxplot(x=column, y=target_variable, data=df_cleaned, palette='viridis', hue=column, legend=False)
        plt.title(f'box plot: {column} vs {target_variable}')
        plt.xlabel(column)
        plt.ylabel(target_variable)
    plt.tight_layout()
    plt.show()  #display the boxplots
    #output the results
    output.append("box plots have been generated.")
    #return the output as a string
    return "\n".join(output)