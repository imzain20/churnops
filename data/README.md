# churn-mlops/data/README.md

# Customer Churn Prediction Dataset

This directory contains the dataset used for training the customer churn prediction model. The dataset includes various features related to customer behavior and demographics, which are essential for predicting whether a customer will churn.

## Dataset Description

- **Features**: The dataset consists of the following features:
  - CustomerID: Unique identifier for each customer
  - Gender: Gender of the customer (Male/Female)
  - Age: Age of the customer
  - Tenure: Number of months the customer has been with the company
  - Balance: Account balance of the customer
  - NumberOfProducts: Number of products the customer has purchased
  - HasCrCard: Whether the customer has a credit card (1 = Yes, 0 = No)
  - IsActiveMember: Whether the customer is an active member (1 = Yes, 0 = No)
  - EstimatedSalary: Estimated salary of the customer
  - Exited: Whether the customer has churned (1 = Yes, 0 = No)

## Data Source

The dataset is sourced from [insert data source here, if applicable]. It is important to ensure that the data is preprocessed correctly before training the model.

## Preprocessing Steps

Before using the dataset for training, the following preprocessing steps should be performed:
1. Handle missing values.
2. Encode categorical variables.
3. Scale numerical features.

## Usage

To use the dataset for training the model, load it into your Python environment and follow the preprocessing steps outlined above. The processed data can then be used to train the churn prediction model.