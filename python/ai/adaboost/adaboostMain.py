import random
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



# Separate features and target variables
X_data = pd.read_excel()
y_excel_data = pd.read_excel()
X_data = X_data.iloc[:, :].astype('float')


y_data = y_excel_data.iloc[:, 1].astype('float')
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2,
                                                                        random_state=42)

rand = random.randint(0, 1000)
model = AdaBoostRegressor(n_estimators=20, random_state=rand)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
