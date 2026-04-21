# Churn Prediction MLOps Project

This project, named **churn-mlops**, is designed to predict customer churn using machine learning techniques. It includes a complete MLOps pipeline with model training, evaluation, and deployment using FastAPI, Docker, and Kubernetes.

## Project Structure

```
churn-mlops
├── api                   # FastAPI application
│   ├── main.py          # Entry point for the FastAPI app
│   └── routers
│       └── churn.py     # API endpoints for churn prediction
├── config                # Configuration files
│   └── config.yaml      # Environment variable settings
├── data                  # Dataset information
│   └── README.md        # Dataset description
├── docker                # Docker configuration
│   ├── Dockerfile        # Docker image instructions
│   └── requirements.txt  # Docker dependencies
├── docs                  # Documentation
│   └── README.md        # Project documentation
├── kubernetes           # Kubernetes configurations
│   ├── deployment.yaml   # Deployment settings
│   └── service.yaml      # Service settings
├── logs                  # Log files
│   └── .gitkeep         # Keep logs directory in Git
├── models                # Trained models
│   └── model.pkl        # Saved churn prediction model
├── notebooks             # Jupyter notebooks
│   └── exploratory_data_analysis.ipynb # EDA notebook
├── src                   # Source code
│   ├── __init__.py      # Package marker
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
├── LICENSE               # Licensing information
├── README.md             # Project overview and setup instructions
└── requirements.txt      # Python dependencies
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
   Open your browser and go to `http://127.0.0.1:8000/docs` to view the API documentation and test the endpoints.

## API Usage Examples

- **Health Check:**
  ```
  GET /health
  ```

- **Predict Churn:**
  ```
  POST /predict
  Request Body:
  {
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

3. **Access the application:**
   Use the service URL provided by Kubernetes to access the deployed application.

## Logging and Monitoring

The application includes logging capabilities to track requests and errors. Ensure that the logs directory is monitored for any issues.

## Code Quality Practices

- Follow PEP 8 guidelines for Python code.
- Use type hints for function signatures.
- Write unit tests for all critical components.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Special thanks to the contributors and the open-source community for their support and resources.