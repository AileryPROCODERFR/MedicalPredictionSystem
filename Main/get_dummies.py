'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - get_dummies.py
24 Oct 2024
**
'''

import pandas as pd

def run(df):
    output = []
    #remove duplicate rows
    df_cleaned = df.drop_duplicates()

    #display original data types before conversion
    output.append("data types before conversion:")
    output.append(str(df_cleaned.dtypes))

    #convert categorical variables to numeric
    df_numeric = pd.get_dummies(df_cleaned, drop_first=True)  #drop_first=True removes one category to avoid multicollinearity

    #display the first few rows of the converted dataframe
    output.append("\nsample data after conversion to numeric:")
    output.append(str(df_numeric.head()))

    #display the new data types after conversion
    output.append("\ndata types after conversion:")
    output.append(str(df_numeric.dtypes))

    return "\n".join(output)

