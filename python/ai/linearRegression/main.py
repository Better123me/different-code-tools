import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
output_data = output_excel_data.iloc[:, features[feature]].values
# Using OLS for Multiple Linear Regression
model = sm.OLS(output_data, input_data)
results = model.fit()

# Using models for prediction
y_pred = results.predict(input_data)
