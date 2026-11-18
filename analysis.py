import numpy as np
import pandas as pd
from scipy.stats import linregress

def load_data(filepath):
    """Load experimental data from a CSV file."""
    return pd.read_csv(filepath)

def calculate_residuals(y, y_pred):
    """Calculate ordinary minus predicted values."""
    return y - y_pred

def calculate_regression(x, y):
    """Perform ordinary least-squares regression."""
    result = linregress(x, y)

    slope = result.slope
    intercept = result.intercept

    y_pred = slope * x + intercept

    return slope, intercept, y_pred

def calculate_statistics(data):
    """Calculate descriptive statistics."""
    
    measurements = data["Measurement"]

    return {
        "Mean": measurements.mean(),
        "Std": measurements.std(),
        "Min": measurements.min(),
        "Max": measurements.max(),
        "Count": measurements.count()
    }

def evaluate_model(y, y_pred):
    """Calculate regression performance metrics."""

    residuals = calculate_residuals(y, y_pred)

    sse = np.sum(residuals**2)
    sst = np.sum((y - np.mean(y))**2)

    return {
        "SSE": sse,
        "MSE": np.mean(residuals**2),
        "RMSE": np.sqrt(np.mean(residuals**2)),
        "MAE": np.mean(np.abs(residuals)),
        "R2": 1 - sse / sst
    }

def validate_data(data):
    """Validate experimental data before analysis."""

    # Check required columns
    required_columns = ["Day", "Measurement"]

    for column in required_columns:
        if column not in data.columns:
            raise ValueError(
                f"Missing required column: {column}"
            )
    
    # Check for missing values
    if data[required_columns].isnull().any().any():
        raise ValueError(
            "Dataset contains missing values."
        )
    
    # Check for numeric data.
    for column in required_columns:
        if not pd.api.types.is_numeric_dtype(data[column]):
            raise ValueError(
                f"Column {column} must contain numeric data."
            )

    # Check sufficient observations
    if len(data) < 3:
        raise ValueError(
            "At least 3 observations are required."
        )

    # check variation in independent variable
    if data["Day"].nunique() < 2:
        raise ValueError(
            "Day values must not all be identical."
        )

    # Check finite values
    values = data[required_columns].to_numpy(
        dtype=float
    )

    if not np.isfinite(values).all():
        raise ValueError(
            "Dataset contains infinite or invalid values"
        )

        return True
        