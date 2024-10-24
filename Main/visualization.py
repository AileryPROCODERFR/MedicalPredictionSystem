import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def run(df):
    output = []
    #remove duplicate rows to ensure clean data
    df_cleaned = df.drop_duplicates()

    #define the target variable (dependent variable)
    target_variable = 'charges'

    #visual analysis - scatter plots for continuous vs. continuous variables
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
    plt.show()
    output.append("scatter plots have been displayed.")

    #statistical correlation analysis - pearson's correlation
    df_encoded = pd.get_dummies(df_cleaned, drop_first=True)
    correlation_matrix = df_encoded[continuous_columns + [target_variable]].corr()
    output.append("\npearson's correlation matrix:")
    output.append(str(correlation_matrix))

    #plot correlation matrix for continuous variables only
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('correlation matrix (continuous variables)')
    plt.show()
    output.append("correlation matrix has been displayed.")

    #anova test for categorical variables
    categorical_columns = ['sex', 'smoker', 'region']
    anova_results = {}

    for column in categorical_columns:
        anova_groups = df_cleaned.groupby(column)['charges'].apply(list)
        f_val, p_val = stats.f_oneway(*anova_groups)
        anova_results[column] = (f_val, p_val)

    anova_df = pd.DataFrame(anova_results, index=["F-value", "p-value"]).T
    output.append("\nanova test results:\n")
    output.append(str(anova_df))

    #display categorical variables that are statistically significant (p < 0.05)
    significant_categorical = anova_df[anova_df["p-value"] < 0.05]
    output.append("\nsignificant categorical features (p < 0.05):\n")
    output.append(str(significant_categorical))

    #visual analysis - box plots for continuous vs. categorical variables
    categorical_columns = df_cleaned.select_dtypes(include=['object']).columns.tolist()

    plt.figure(figsize=(16, 10))
    for i, column in enumerate(categorical_columns, 1):
        plt.subplot(2, 3, i)
        sns.boxplot(x=column, y=target_variable, data=df_cleaned, palette='viridis', hue=column, dodge=False)
        plt.title(f'box plot: {column} vs {target_variable}')
        plt.xlabel(column)
        plt.ylabel(target_variable)
    plt.tight_layout()
    plt.show()
    output.append("box plots have been displayed.")

    #visual analysis - histogram for continuous variables
    plt.figure(figsize=(16, 10))
    for i, column in enumerate(continuous_columns + [target_variable], 1):
        plt.subplot(2, 3, i)
        sns.histplot(df_cleaned[column], bins=30, kde=True, color='skyblue')
        plt.title(f'distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('frequency')
    plt.tight_layout()
    plt.show()
    output.append("histograms have been displayed.")

    return "\n".join(output)
