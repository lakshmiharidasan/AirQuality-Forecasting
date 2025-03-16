import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Generate a synthetic time series dataset (you can replace this with your real data)
def generate_synthetic_data(num_points):
    x = np.linspace(0, 10, num_points)
    y = np.sin(x) + np.random.normal(0, 0.1, num_points)
    return y

# Sample data generation
num_points = 200
data = generate_synthetic_data(num_points)
print(data)
print(type(data))

#
#
# Normalize the data
scaler = MinMaxScaler()
data = scaler.fit_transform(data.reshape(-1, 1))

# Split the data into training and testing sets
train_size = int(len(data) * 0.8)
train_data, test_data = data[:train_size], data[train_size:]

# Create sequences for the LSTM model
def create_sequences(data, look_back):
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:i+look_back])
        y.append(data[i+look_back])
    return np.array(X), np.array(y)

look_back = 10  # You can adjust this parameter to change the sequence length
train_X, train_y = create_sequences(train_data, look_back)
test_X, test_y = create_sequences(test_data, look_back)

print(train_X[0])
print(type(train_X[0]))
print(type(train_X[0]))


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

# Inverse transform the predictions to original scale
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(np.arange(0, len(train_data)), scaler.inverse_transform(train_data), label='Training Data')
plt.plot(np.arange(len(train_data), len(train_data) + len(test_data)), scaler.inverse_transform(test_data), label='Testing Data')
plt.plot(np.arange(look_back, look_back + len(train_predict)), train_predict, label='Training Predictions')
plt.plot(np.arange(len(train_data) + look_back, len(train_data) + look_back + len(test_predict),), test_predict, label='Testing Predictions')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
