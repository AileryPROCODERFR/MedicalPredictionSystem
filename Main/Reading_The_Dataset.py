'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - Reading_The_Dataset.py
24 Oct 2024
**
'''
#this script reads the dataset from a csv file and removes duplicate rows
import pandas as pd
#function to read the dataset from a csv file
def run(df):
    output = []
    #remove duplicate rows
    df_cleaned = df.drop_duplicates()

    #print a sample of the cleaned data for inspection
    output.append("sample data after removing duplicates:")
    output.append(str(df_cleaned.sample(10)))  #print 10 random samples for inspection

    return "\n".join(output)