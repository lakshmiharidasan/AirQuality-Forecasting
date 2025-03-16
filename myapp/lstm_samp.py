


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

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

# Normalize Data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Create Sliding Window
def create_dataset(data, look_back=24):
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:i + look_back, :])
        y.append(data[i + look_back, 0])  # Predict the pollutant (e.g., PM2.5)
    return np.array(X), np.array(y)

look_back = 24  # Use the past 24 hours to predict the next hour
X, y = create_dataset(scaled_data, look_back)

# Train-Test Split
train_size = int(len(X) * 0.8)
train_X, test_X = X[:train_size], X[train_size:]
train_y, test_y = y[:train_size], y[train_size:]

        # Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, input_shape=(look_back, 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_X, train_y, epochs=100, batch_size=64)

# Make predictions
train_predict = model.predict(train_X)
test_predict = model.predict(test_X)
print(test_predict)

# Inverse transform the predictions to original scale
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)
y_test = scaler.inverse_transform(np.hstack((test_y.reshape(-1, 1), np.zeros((test_y.shape[0], scaled_data.shape[1] - 1)))))[:, 0]

# print(test_y)
# test_y = scaler.inverse_transform(test_y)
# Plot Results
plt.figure(figsize=(10, 6))
plt.plot(test_y, label='Actual')
plt.plot(test_predict, label='Predicted')
plt.title(f'{pollutant} Forecasting')
plt.xlabel('Time')
plt.ylabel(f'{pollutant} Level')
plt.legend()
plt.show()
print("******************************************************")
print("******************************************************")
print(test_predict)
print("******************************************************")
print( test_y)

