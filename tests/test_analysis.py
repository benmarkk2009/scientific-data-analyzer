import numpy as np
import pandas as pd
import pytest
from analysis import (
    calculate_regression,
    calculate_residuals,
    evaluate_model,
    validate_data
)

def test_linear_regression():

    # Create a dataset with known results
    x = np.array([1, 2, 3, 4])
    y = np.array([5, 7, 9, 11])

    # Run our regression function
    slope, intercept, y_pred = calculate_regression(x, y)

    # Verify the results
    assert np.isclose(slope, 2.0)
    assert np.isclose(intercept, 3.0)
    assert np. allclose(y_pred, y)

def test_residuals():

    y = np.array([10, 20, 30])
    y_pred = np.array([9, 22, 28])

    residuals = calculate_residuals(y, y_pred)

    expected = np.array([1, -2, 2])

    assert np.allclose(residuals, expected)

def test_model_metrics():

    y = np.array([2, 4, 6])
    y_pred = np.array([3, 4, 5])

    metrics = evaluate_model(y, y_pred)

    assert np.isclose(metrics["SSE"], 2.0)
    assert np.isclose(metrics["MSE"], 2 / 3)
    assert np.isclose(metrics["RMSE"], np.sqrt(2 / 3))
    assert np.isclose(metrics["MAE"], 2 / 3)
    assert np.isclose(metrics["R2"], 0.75)

def test_missing_values():

    data = pd.DataFrame({
        "Day": [1, 2, 3],
        "Measurement": [10.0, None, 12.0]
    })

    with pytest.raises(ValueError):
        validate_data(data)

def test_missing_column():
    data = pd.DataFrame({
        "Day": [1, 2, 3]
    })
    with pytest.raises(ValueError):
        validate_data(data)