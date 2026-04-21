from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

router = APIRouter()

# Load the trained model and preprocessor
model = joblib.load("models/model.pkl")

class ChurnRequest(BaseModel):
    features: list

@router.post("/predict")
async def predict_churn(request: ChurnRequest):
    try:
        # Convert features to numpy array and reshape for prediction
        features_array = np.array(request.features).reshape(1, -1)
        prediction = model.predict(features_array)
        return {"churn_prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/health")
async def health_check():
    return {"status": "healthy"}