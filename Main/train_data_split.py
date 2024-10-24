import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def run(df):
    output = []
    #remove duplicate rows
    df_cleaned = df.drop_duplicates()

    #convert categorical variables to numeric
    df_numeric = pd.get_dummies(df_cleaned, drop_first=True)

    #define the features (X) and target variable (y)
    if 'charges' not in df_numeric:
        return "error: target variable 'charges' not found."
    X = df_numeric.drop('charges', axis=1)  #all columns except the target
    y = df_numeric['charges']  #target variable

    #split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  #70-30 split

    output.append(f"training set size: {X_train.shape}")
    output.append(f"testing set size: {X_test.shape}")

    #print a few rows of the training set
    output.append("\nsample of the training data (without scaling):")
    output.append(str(X_train.head()))

    return "\n".join(output)
