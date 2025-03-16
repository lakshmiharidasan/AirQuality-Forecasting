import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense

# Load Dataset
# Replace 'air_pollution_data.csv' with your dataset file
data = pd.read_csv('station_day.csv', parse_dates=['Date'], index_col='Date')
pollutant = 'PM2.5'  # Replace with the pollutant you want to forecast

# Handle Missing Values
data = data.fillna(method='ffill')

# Feature Selection (pollutants + weather data if available)
features = ['PM2.5']  # Example columns
data = data[features]

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def create_dataset(data, look_back=24):
    X, y = [], []
    for i in range(len(data)):
        print(data,type(data))
        print(type(data))
        print(data['PM2.5'][i])
        X.append(data['PM2.5'][i])
        y.append(i)  # Predict the pollutant (e.g., PM2.5)
    return X,y

look_back = 24  # Use the past 24 hours to predict the next hour
X, y = create_dataset(data, look_back)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

        # Sample dataset (replace with your own data)
data = {
    'Time':y_train, #[1, 2, 3, 4, 5, 6],
    'Value':X_train # [10, 12, 14, 16, 18, 20]
}


print(X_train)
# Create and train the linear regression model
df = pd.DataFrame(data)

        # Separate the independent variable (X) and dependent variable (y)
X = df[['Time']]
y = df['Value']

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions for future time points (e.g., forecasting for time = 7)
predicted_value=[]
# for i in y_test:
#     print(i)
#     pv = model.predict(np.array([i]))
#     predicted_value.append((pv))


future_time = len(X)+2
pv=[]
for i in y_test:
    predicted_value = model.predict(np.array([[i]]))
    pv.append(predicted_value[0])

print(pv)

# Plot Results
plt.figure(figsize=(10, 6))
plt.plot(y_test, label='Actual')
plt.plot(pv, label='Predicted')
plt.title(f'{pollutant} Forecasting')
plt.xlabel('Time')
plt.ylabel(f'{pollutant} Level')
plt.legend()
plt.show()