# Churn Prediction MLOps Project

This project, named **churn-mlops**, is designed to predict customer churn using machine learning techniques. It includes a complete MLOps pipeline with model training, evaluation, and deployment using FastAPI, Docker, and Kubernetes.

## Project Structure

```
churn-mlops
├── api                   # FastAPI application
│   ├── main.py          # Entry point for the FastAPI application
│   └── routers
│       └── churn.py     # API endpoints for churn prediction
├── config                # Configuration files
│   └── config.yaml      # Configuration settings
├── data                  # Dataset information
│   └── README.md        # Information about the dataset
├── docker                # Docker configurations
│   ├── Dockerfile       # Dockerfile for building the FastAPI image
│   └── requirements.txt  # Python dependencies for Docker
├── docs                  # Documentation
│   └── README.md        # Documentation for the project
├── kubernetes           # Kubernetes configurations
│   ├── deployment.yaml   # Deployment configuration
│   └── service.yaml      # Service configuration
├── logs                  # Log files
│   └── .gitkeep         # Keep logs directory in version control
├── models                # Trained models
│   └── model.pkl        # Saved customer churn prediction model
├── notebooks             # Jupyter notebooks
│   └── exploratory_data_analysis.ipynb # EDA notebook
├── src                   # Source code
│   ├── __init__.py      # Marks src as a package
│   ├── data_preprocessing.py # Data preprocessing functions
│   ├── model_training.py # Model training logic
│   ├── model_evaluation.py # Model evaluation functions
│   └── utils.py         # Utility functions
├── tests                 # Unit tests
│   ├── test_api.py      # Tests for FastAPI endpoints
│   ├── test_model.py    # Tests for model functions
│   └── test_utils.py    # Tests for utility functions
├── .github               # GitHub Actions workflows
│   └── workflows
│       └── ci-cd.yml    # CI/CD pipeline configuration
├── .gitignore            # Git ignore file
├── LICENSE               # Project license
├── README.md             # Project overview and documentation
└── requirements.txt      # Python dependencies for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/churn-mlops.git
   cd churn-mlops
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application:**
   ```
   uvicorn api.main:app --reload
   ```

4. **Access the API:**
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the API documentation and test the endpoints.

## API Usage Examples

- **Health Check:**
  ```
  GET /health
  ```

- **Predict Churn:**
  ```
  POST /predict
  Request Body: {
      "feature1": value1,
      "feature2": value2,
      ...
  }
  ```

## Deployment Steps

1. **Build the Docker image:**
   ```
   docker build -t churn-mlops .
   ```

2. **Deploy to Kubernetes:**
   ```
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
   ```

## Logging and Monitoring

Logs are stored in the `logs` directory. Ensure that logging is properly configured in the FastAPI application for monitoring purposes.

## Code Quality Practices

This project follows best practices for code quality, including:
- Type hints for function signatures
- Pydantic models for request validation
- Unit tests for critical components

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Thanks to the contributors and the open-source community for their support and resources.