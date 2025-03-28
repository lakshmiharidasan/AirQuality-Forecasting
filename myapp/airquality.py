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
print("data=================================")
print("data=================================")
print("data=================================")
print(data)
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
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Build GRU Model
model = Sequential([
    GRU(64, input_shape=(look_back, X.shape[2]), return_sequences=False),
    Dense(1)  # Predict one pollutant level
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

# Train Model
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2, verbose=1)

# Predict
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(np.hstack((predictions, np.zeros((predictions.shape[0], scaled_data.shape[1] - 1)))))[:, 0]
y_test = scaler.inverse_transform(np.hstack((y_test.reshape(-1, 1), np.zeros((y_test.shape[0], scaled_data.shape[1] - 1)))))[:, 0]

# Plot Results
plt.figure(figsize=(10, 6))
plt.plot(y_test, label='Actual')
plt.plot(predictions, label='Predicted')
plt.title(' Forecasting')
plt.xlabel('Time')
plt.ylabel(f'{pollutant} Level')
plt.legend()
plt.show()


from sklearn.metrics import mean_squared_error
import numpy as np

# Mean Squared Error (MSE)
mse = mean_squared_error(y_test, predictions)

# Peak Signal-to-Noise Ratio (PSNR)
# PSNR is usually used in image processing, but it can be adapted for regression problems like this
# PSNR = 20 * log10(MAX / sqrt(MSE))
# Here MAX is the maximum value that a pixel can have, in the case of pollutant data, it's the maximum value in your dataset
max_value = np.max(scaled_data)  # You can also use a predefined maximum if you know it

psnr = 20 * np.log10(max_value / np.sqrt(mse))

# Print MSE and PSNR
print(f'Mean Squared Error (MSE): {mse}')
print(f'Peak Signal-to-Noise Ratio (PSNR): {psnr} dB')
