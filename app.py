from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd
import uvicorn
import bz2
from diabetes_predictor import DiabetesPredictor


app = FastAPI()

#loading 
scalarobject=bz2.BZ2File("Model/standardScalar.pkl", "rb")
scaler=pickle.load(scalarobject)
modelforpred = bz2.BZ2File("Model/modelForPrediction.pkl", "rb")
model = pickle.load(modelforpred)

## Route for homepage

@app.get('/')
def index():
    return {"message":"Hi welcome"}

## Route for Single data point prediction
@app.post('/predictdata')
def predict_datapoint(data:DiabetesPredictor):

    data = data.dict()
    Pregnancies=data["Pregnancies"]
    Glucose = data['Glucose']
    BloodPressure = data['BloodPressure']
    SkinThickness = data['SkinThickness']
    Insulin = data['Insulin']
    BMI = data['BMI']
    DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']
    Age = data['Age']

    new_data=scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    predict=model.predict(new_data)
       
    if predict[0] ==1 :
        result = 'Diabetic'
    else:
        result ='Non-Diabetic'
        
    return result


if __name__=="__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)