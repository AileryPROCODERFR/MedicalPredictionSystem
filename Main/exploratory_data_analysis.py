<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset from csv file
file_path = "Medical_insurance.csv"  #dataset file location
medical_insurance_df = pd.read_csv(file_path)

#remove duplicate rows
medical_insurance_df_cleaned = medical_insurance_df.drop_duplicates()

#identify quantitative and categorical columns
quantitative_columns = medical_insurance_df_cleaned.select_dtypes(include=['float64', 'int64']).columns.tolist()
categorical_columns = medical_insurance_df_cleaned.select_dtypes(include=['object']).columns.tolist()

#set up the figure for plotting histograms of quantitative variables
plt.figure(figsize=(16, 20))
for i, column in enumerate(quantitative_columns, 1):
    plt.subplot(len(quantitative_columns), 1, i)
    sns.histplot(medical_insurance_df_cleaned[column], bins=20, kde=True, color='skyblue')
    plt.title(f'distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('frequency')
    plt.grid(True)

#show histograms for quantitative variables
plt.tight_layout()
plt.show()

#set up the figure for plotting bar charts of categorical variables
plt.figure(figsize=(16, 20))
for i, column in enumerate(categorical_columns, 1):
    plt.subplot(len(categorical_columns), 1, i)
    sns.countplot(data=medical_insurance_df_cleaned, x=column, palette='viridis')
    plt.title(f'distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('count')
    plt.grid(True, axis='y')

#show bar charts for categorical variables
plt.tight_layout()
plt.show()
=======
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset from csv file
file_path = "Medical_insurance.csv"  #dataset file location
medical_insurance_df = pd.read_csv(file_path)

#remove duplicate rows
medical_insurance_df_cleaned = medical_insurance_df.drop_duplicates()

#identify quantitative and categorical columns
quantitative_columns = medical_insurance_df_cleaned.select_dtypes(include=['float64', 'int64']).columns.tolist()
categorical_columns = medical_insurance_df_cleaned.select_dtypes(include=['object']).columns.tolist()

#set up the figure for plotting histograms of quantitative variables
plt.figure(figsize=(16, 20))
for i, column in enumerate(quantitative_columns, 1):
    plt.subplot(len(quantitative_columns), 1, i)
    sns.histplot(medical_insurance_df_cleaned[column], bins=20, kde=True, color='skyblue')
    plt.title(f'distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('frequency')
    plt.grid(True)

#show histograms for quantitative variables
plt.tight_layout()
plt.show()

#set up the figure for plotting bar charts of categorical variables
plt.figure(figsize=(16, 20))
for i, column in enumerate(categorical_columns, 1):
    plt.subplot(len(categorical_columns), 1, i)
    sns.countplot(data=medical_insurance_df_cleaned, x=column, palette='viridis')
    plt.title(f'distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('count')
    plt.grid(True, axis='y')

#show bar charts for categorical variables
plt.tight_layout()
plt.show()
>>>>>>> 2e88566b4932547307bc157aae7bf007d2d4e008
