from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load('regression.joblib')

# Data model for input validation
class HouseData(BaseModel):
    size: float
    bedrooms: int
    garden: int

# Ppredict endpoint
@app.post("/predict")
def predict_price(data: HouseData):
    # Prepare the input data for prediction
    input_data = np.array([[data.size, data.bedrooms, data.garden]])
    
    # Make prediction
    predicted_price = model.predict(input_data)[0]
    
    return {"predicted_price": predicted_price}

