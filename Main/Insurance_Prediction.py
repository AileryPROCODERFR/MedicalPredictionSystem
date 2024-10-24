import pandas as pd
import joblib
import os

def predict_insurance(age, sex, bmi, children, smoker, region):
    #load the saved model
    model_path = os.path.join(os.path.dirname(__file__), 'insurance_model.pkl')
    if not os.path.exists(model_path):
        return "error: model file 'insurance_model.pkl' not found."

    #load the trained model, which includes the preprocessing pipeline
    model = joblib.load(model_path)

    #create a dataframe for the input data
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    #make the prediction using the entire model pipeline
    try:
        prediction = model.predict(input_data)
        return f"${prediction[0]:.2f}"
    except Exception as e:
        return f"error during prediction: {e}"

#example usage
if __name__ == "__main__":
    age = 30
    sex = 'male'
    bmi = 25.0
    children = 1
    smoker = 'no'
    region = 'northeast'

    print(predict_insurance(age, sex, bmi, children, smoker, region))
