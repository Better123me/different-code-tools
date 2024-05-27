import random

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

y_data = y_excel_data.iloc[:, features[feature]].astype('float')
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2,
                                                                        random_state=42)

rand = random.randint(0, 1000)
model = RandomForestRegressor(n_estimators=20, random_state=rand)
model.fit(X_train, y_train)
predictions = model.predict(X_test)