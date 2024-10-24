<<<<<<< HEAD
import pandas as pd
import numpy as np
import pickle  #for saving and loading the model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  #basic model
from sklearn.preprocessing import StandardScaler

#load the dataset
file_path = "Medical_insurance.csv"  #dataset file path
medical_insurance_df = pd.read_csv(file_path) #read the dataset
medical_insurance_df_cleaned = medical_insurance_df.drop_duplicates()
medical_insurance_df_numeric = pd.get_dummies(medical_insurance_df_cleaned, drop_first=True)

#define features and target variable
X = medical_insurance_df_numeric.drop('charges', axis=1)
y = medical_insurance_df_numeric['charges']

#retrain the model
model = LinearRegression()
model.fit(X, y)

#save the trained model
model_filename = 'best_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)

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

#function to be used with the gui
def run(df):
    output = []
    #clean the input dataframe
    df_cleaned = df.drop_duplicates()
    df_numeric = pd.get_dummies(df_cleaned, drop_first=True)
    
    X = df_numeric.drop('charges', axis=1, errors='ignore')
    if 'charges' in df_numeric:
        y = df_numeric['charges']
    else:
        return "error: target variable 'charges' not found."
    
    #fit the model
    model.fit(X, y)
    with open(model_filename, 'wb') as file:
        pickle.dump(model, file)
    output.append(f"model saved as {model_filename}.")
    
    #example prediction
    test_prediction = predict_charges(30, 'male', 25.0, 1, 'no', 'northeast')
    output.append(f"test prediction: ${test_prediction:.2f}")
    
    return "\n".join(output)
=======
import pandas as pd
import numpy as np
import pickle  #for saving and loading the model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  #basic model
from sklearn.preprocessing import StandardScaler

#load the dataset
file_path = "Medical_insurance.csv"  #dataset file path
medical_insurance_df = pd.read_csv(file_path) #read the dataset
medical_insurance_df_cleaned = medical_insurance_df.drop_duplicates()
medical_insurance_df_numeric = pd.get_dummies(medical_insurance_df_cleaned, drop_first=True)

#define features and target variable
X = medical_insurance_df_numeric.drop('charges', axis=1)
y = medical_insurance_df_numeric['charges']

#retrain the model
model = LinearRegression()
model.fit(X, y)

#save the trained model
model_filename = 'best_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)

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

#function to be used with the gui
def run(df):
    output = []
    #clean the input dataframe
    df_cleaned = df.drop_duplicates()
    df_numeric = pd.get_dummies(df_cleaned, drop_first=True)
    
    X = df_numeric.drop('charges', axis=1, errors='ignore')
    if 'charges' in df_numeric:
        y = df_numeric['charges']
    else:
        return "error: target variable 'charges' not found."
    
    #fit the model
    model.fit(X, y)
    with open(model_filename, 'wb') as file:
        pickle.dump(model, file)
    output.append(f"model saved as {model_filename}.")
    
    #example prediction
    test_prediction = predict_charges(30, 'male', 25.0, 1, 'no', 'northeast')
    output.append(f"test prediction: ${test_prediction:.2f}")
    
    return "\n".join(output)
>>>>>>> 2e88566b4932547307bc157aae7bf007d2d4e008
