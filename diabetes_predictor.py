from pydantic import BaseModel

class DiabetesPredictor(BaseModel):
        Pregnancies:int
        Glucose:float 
        BloodPressure:float
        SkinThickness:float
        Insulin:float
        BMI:float
        DiabetesPedigreeFunction:float
        Age:int

