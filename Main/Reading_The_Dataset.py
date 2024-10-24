import pandas as pd

def run(df):
    output = []
    #remove duplicate rows
    df_cleaned = df.drop_duplicates()

    #print a sample of the cleaned data for inspection
    output.append("sample data after removing duplicates:")
    output.append(str(df_cleaned.sample(10)))  #print 10 random samples for inspection

    return "\n".join(output)
