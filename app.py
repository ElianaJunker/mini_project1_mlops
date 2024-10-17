from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load('regression.joblib')

# Define a data model for input validation
class HouseData(BaseModel):
    size: float
    bedrooms: int
    garden: int

# Define a predict endpoint
@app.post("/predict")
def predict_price(data: HouseData):
    # Prepare the input data for prediction
    input_data = np.array([[data.size, data.bedrooms, data.garden]])
    
    # Make prediction
    predicted_price = model.predict(input_data)[0]
    
    return {"predicted_price": predicted_price}

