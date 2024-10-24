import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def run(df):
    output = []
    #remove duplicate rows
    df_cleaned = df.drop_duplicates()

    #identify quantitative and categorical columns
    quantitative_columns = df_cleaned.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_columns = df_cleaned.select_dtypes(include=['object']).columns.tolist()

    #generate histograms for quantitative variables
    histogram_buffer = io.BytesIO()
    plt.figure(figsize=(16, 20))
    for i, column in enumerate(quantitative_columns, 1):
        plt.subplot(len(quantitative_columns), 1, i)
        sns.histplot(df_cleaned[column], bins=20, kde=True, color='skyblue')
        plt.title(f'distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('frequency')
        plt.grid(True)
    plt.tight_layout()
    plt.savefig(histogram_buffer, format='png')
    histogram_buffer.seek(0)
    output.append("histograms for quantitative variables have been generated.")

    #generate bar charts for categorical variables
    bar_chart_buffer = io.BytesIO()
    plt.figure(figsize=(16, 20))
    for i, column in enumerate(categorical_columns, 1):
        plt.subplot(len(categorical_columns), 1, i)
        sns.countplot(data=df_cleaned, x=column, palette='viridis')
        plt.title(f'distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('count')
        plt.grid(True, axis='y')
    plt.tight_layout()
    plt.savefig(bar_chart_buffer, format='png')
    bar_chart_buffer.seek(0)
    output.append("bar charts for categorical variables have been generated.")

    return "\n".join(output)