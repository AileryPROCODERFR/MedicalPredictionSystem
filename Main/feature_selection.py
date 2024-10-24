import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def run(df):
    output = []
    #remove duplicate rows to ensure clean data
    df_cleaned = df.drop_duplicates()

    #define the target variable
    target_variable = 'charges'

    #visual analysis - scatter plots for continuous variables
    continuous_columns = df_cleaned.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if target_variable in continuous_columns:
        continuous_columns.remove(target_variable)

    plt.figure(figsize=(16, 10))
    for i, column in enumerate(continuous_columns, 1):
        plt.subplot(2, 3, i)
        sns.scatterplot(x=df_cleaned[column], y=df_cleaned[target_variable], color='skyblue')
        plt.title(f'scatter plot: {column} vs {target_variable}')
        plt.xlabel(column)
        plt.ylabel(target_variable)
    plt.tight_layout()
    plt.show()  #display the scatterplots

    output.append("scatter plots have been generated.")

    #statistical correlation analysis - pearson's correlation
    correlation_matrix = df_cleaned[continuous_columns + [target_variable]].corr()
    output.append("\npearson's correlation matrix:")
    output.append(str(correlation_matrix))

    #visual analysis - box plots for continuous vs. categorical variables
    categorical_columns = df_cleaned.select_dtypes(include=['object']).columns.tolist()

    plt.figure(figsize=(16, 10))
    for i, column in enumerate(categorical_columns, 1):
        plt.subplot(2, 3, i)
        sns.boxplot(x=column, y=target_variable, data=df_cleaned, palette='viridis', hue=column, legend=False)
        plt.title(f'box plot: {column} vs {target_variable}')
        plt.xlabel(column)
        plt.ylabel(target_variable)
    plt.tight_layout()
    plt.show()  #display the boxplots

    output.append("box plots have been generated.")

    return "\n".join(output)
