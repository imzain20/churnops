from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import joblib
import os

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Example preprocessing steps
    data = data.drop(columns=['unnecessary_column'])
    data = pd.get_dummies(data, drop_first=True)
    return data

def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def save_model(model, model_path):
    joblib.dump(model, model_path)

def main():
    # Load and preprocess data
    data = load_data('data/churn_data.csv')
    processed_data = preprocess_data(data)
    
    # Split data into features and target
    X = processed_data.drop(columns=['churn'])
    y = processed_data['churn']
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Save the trained model
    model_path = os.path.join('models', 'model.pkl')
    save_model(model, model_path)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()