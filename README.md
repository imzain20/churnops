# churnops
ChurnOps is an end-to-end MLOps project focused on building, deploying, and operating a customer churn prediction system in a production grade environment. 


This project demonstrates how to take a machine learning model from development to production using modern MLOps practices. It includes:

Model training pipeline
REST API for predictions
Containerization
Kubernetes deployment
CI/CD automation
Logging and monitoring

The model predicts whether a customer is likely to churn based on structured input features.

                ┌────────────────────┐
                │   Training Script  │
                │    (train.py)      │
                └────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Trained Model (.pkl) │
              │ Preprocessor (.pkl)  │
              └────────┬─────────────┘
                       │
                       ▼
              ┌──────────────────────┐
              │    FastAPI Service   │
              │  (/predict, /health) │
              └────────┬─────────────┘
                       │
                       ▼
              ┌──────────────────────┐
              │     Docker Image     │
              └────────┬─────────────┘
                       │
                       ▼
              ┌──────────────────────┐
              │   Kubernetes (K8s)   │
              │ Deployment + Service │
              └────────┬─────────────┘
                       │
                       ▼
              ┌──────────────────────┐
              │     End Users/API    │
              └──────────────────────┘
