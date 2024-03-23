import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np


def createArimaModel(data, test) -> None:
    """
    Create an ARIMA model
    """
    model = ARIMA(data, order=(5, 1, 0))

    model_fit = model.fit()

    predictions = model_fit.forecast(steps=len(test))
    mse = mean_squared_error(test, predictions)
    print("Mean Squared Error:", mse)


def createLinearRegressionModel(data) -> LinearRegression:
    """
    Create a Linear Regression model
    """
    # Create a LinearRegression model
    model = LinearRegression()

    # Fit the model to the training data
    # Fit model to X/Y
    model.fit(np.array(range(len(data))).reshape(-1, 1), data)
    # theory: model.fit(months, passengers) months/years need to be X, passengers need to be Y

    return model
