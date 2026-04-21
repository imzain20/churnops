from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os

# Load the trained model and preprocessor
model_path = os.path.join(os.path.dirname(__file__), '../models/model.pkl')
model = joblib.load(model_path)

# Initialize FastAPI app
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model for prediction
class ChurnRequest(BaseModel):
    feature_1: float
    feature_2: float
    feature_3: float
    # Add other features as needed

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Prediction endpoint
@app.post("/predict")
def predict(request: ChurnRequest):
    features = [[
        request.feature_1,
        request.feature_2,
        request.feature_3,
        # Add other features as needed
    ]]
    prediction = model.predict(features)
    return {"churn_prediction": prediction[0]}