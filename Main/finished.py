'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 - finished.py
24 Oct 2024
**
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np

#function to be used with the gui
def run(df):
    output = []
    #features and target selection
    X = df.drop('charges', axis=1, errors='ignore')
    if 'charges' in df:
        y = df['charges']
    else:
        return "error: target variable 'charges' not found."

    #preprocessing the categorical variables
    categorical_features = ['sex', 'smoker', 'region']
    numerical_features = ['age', 'bmi', 'children']

    #define the columntransformer for preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(), categorical_features)
        ]
    )

    #create a pipeline with preprocessing and regression model
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    #train the model using the entire dataset
    model_pipeline.fit(X, y)

    #save the model to a file
    model_filename = 'insurance_model.pkl'
    joblib.dump(model_pipeline, model_filename)
    output.append(f"model training complete and saved as '{model_filename}'")

    return "\n".join(output)

#function to load the model and make predictions
def predict_insurance_cost(age, sex, bmi, children, smoker, region):
    #load the trained model
    model = joblib.load('insurance_model.pkl')
    
    #create a dataframe for the input data
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })
    
    #ensure the input data is preprocessed consistently
    try:
        prediction = model.predict(input_data)
        return prediction[0]
    except Exception as e:
        return f"error during prediction: {e}"