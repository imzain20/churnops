def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_data(df):
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline

    # Identify categorical and numerical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    numerical_cols = df.select_dtypes(exclude=['object']).columns.tolist()

    # Create preprocessing pipelines for both numerical and categorical data
    numerical_pipeline = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    categorical_pipeline = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine both pipelines into a single ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_pipeline, numerical_cols),
            ('cat', categorical_pipeline, categorical_cols)
        ]
    )

    # Fit and transform the data
    X = preprocessor.fit_transform(df)
    return X, preprocessor

def split_data(df, target_column):
    from sklearn.model_selection import train_test_split

    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def save_preprocessor(preprocessor, file_path):
    import joblib
    joblib.dump(preprocessor, file_path)

def load_preprocessor(file_path):
    import joblib
    return joblib.load(file_path)