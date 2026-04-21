from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_churn():
    response = client.post("/predict", json={"feature1": 1, "feature2": 0, "feature3": 1})
    assert response.status_code == 200
    assert "prediction" in response.json()