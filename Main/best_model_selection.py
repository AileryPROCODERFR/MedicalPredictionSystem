'''
**
Author: Undergraduate Group 30
U3232140,U3188967,U3284359,U3268553
Assessment 3 Best_model_Selection.py
24 Oct 2024
**
'''
import pandas as pd
import numpy as np
import pickle  #for saving and loading the model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  #basic model
from sklearn.preprocessing import StandardScaler

#load the dataset
file_path = "Medical_insurance.csv"  #dataset file path
medical_insurance_df = pd.read_csv(file_path) #read the dataset
#Need to clean the data before training the model
medical_insurance_df_cleaned = medical_insurance_df.drop_duplicates() #uses the drop_duplicates method to remove duplicate rows
medical_insurance_df_numeric = pd.get_dummies(medical_insurance_df_cleaned, drop_first=True) #convert categorical variables to numeric

#define features and target variable
X = medical_insurance_df_numeric.drop('charges', axis=1) #plot all columns except the target variable 'charges' as features
y = medical_insurance_df_numeric['charges'] #Set the target variable 'charges' on the y-axis

#retrain the model
model = LinearRegression() #create a new model object (instance) of the LinearRegression class
model.fit(X, y) #fit the model to the data

#save the trained model to a file using pickle module
model_filename = 'best_model.pkl' #Found in the same directory as the script
#open the file in write-binary mode and save the model to the file
with open(model_filename, 'wb') as file:
    pickle.dump(model, file) #save the model to the file

#create a prediction function
def predict_charges(age, sex, bmi, children, smoker, region):
    """
    predicts medical charges based on input values
    
    parameters:
        age (int): age of the individual
        sex (str): gender ('male' or 'female')
        bmi (float): body mass index
        children (int): number of dependents
        smoker (str): smoking status ('yes' or 'no')
        region (str): region ('northeast', 'northwest', 'southeast', 'southwest')
        
    returns:
        float: predicted medical charges
    """
    #build input data similar to training format
    input_data = pd.DataFrame({
        'age': [age],
        'bmi': [bmi],
        'children': [children],
        'sex_male': [1 if sex == 'male' else 0],
        'smoker_yes': [1 if smoker == 'yes' else 0],
        'region_northwest': [1 if region == 'northwest' else 0],
        'region_southeast': [1 if region == 'southeast' else 0],
        'region_southwest': [1 if region == 'southwest' else 0]
    })

    #load the saved model
    with open(model_filename, 'rb') as file:
        loaded_model = pickle.load(file)
    
    #make the prediction
    prediction = loaded_model.predict(input_data)
    return float(prediction[0])

#function to be used within the gui
def run(df):
    #initialize the output list to store messages
    output = []
    #clean the input dataframe
    df_cleaned = df.drop_duplicates()
    df_numeric = pd.get_dummies(df_cleaned, drop_first=True)
    #define the features and target variable
    X = df_numeric.drop('charges', axis=1, errors='ignore')
    #check if the target variable is present, return an error message if not
    if 'charges' in df_numeric:
        y = df_numeric['charges']
    else:
        return "error: target variable 'charges' not found."
    
    #fit the model to the data
    model.fit(X, y)
    with open(model_filename, 'wb') as file:
        pickle.dump(model, file)
    output.append(f"model saved as {model_filename}.")
    
    #example prediction using the new model
    test_prediction = predict_charges(30, 'male', 25.0, 1, 'no', 'northeast')
    output.append(f"test prediction: ${test_prediction:.2f}")
    #split the data into training and testing sets
    return "\n".join(output)
