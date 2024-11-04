from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model_name = "bhadresh-savani/distilbert-base-uncased-emotion"
emotion_classifier = pipeline("text-classification", model=model_name)


# Data model for input validation
class TextData(BaseModel):
    text: str

# Predict endpoint
@app.post("/predict")
def predict_toxicity(data: TextData):
    results = emotion_classifier(data.text)

    #Get the result of the prediction (label and score)
    predicted_label = results[0]['label']
    score = results[0]['score']

    return {"predicted_label": predicted_label, "score": score}

