import pytest
import joblib
import numpy as np
from src.model_evaluation import evaluate_model
from src.model_training import train_model

@pytest.fixture
def sample_data():
    # Sample data for testing
    return np.array([[1, 0, 30, 1], [0, 1, 25, 0], [1, 1, 35, 1]])

def test_train_model(sample_data):
    model = train_model(sample_data)
    assert model is not None
    assert hasattr(model, 'predict')

def test_evaluate_model(sample_data):
    model = train_model(sample_data)
    accuracy, precision, recall = evaluate_model(model, sample_data)
    assert accuracy >= 0.0 and accuracy <= 1.0
    assert precision >= 0.0 and precision <= 1.0
    assert recall >= 0.0 and recall <= 1.0

def test_model_serialization(sample_data):
    model = train_model(sample_data)
    joblib.dump(model, 'models/model.pkl')
    loaded_model = joblib.load('models/model.pkl')
    assert loaded_model is not None
    assert hasattr(loaded_model, 'predict')