import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense

def forecast_data(data):

    # Normalize Data
    # scaler = MinMaxScaler(feature_range=(0, 1))
    # data=np.asarray(data)
    # scaled_data = scaler.fit_transform(data)

    # Create Sliding Window
    def create_dataset(data, look_back=24):
        X, y = [], []
        for i in range(len(data) - look_back):
            X.append([data[i:i + look_back]])
            y.append(data[look_back])  # Predict the pollutant (e.g., PM2.5)
        return np.array(X), np.array(y)

    look_back = 24  # Use the past 24 hours to predict the next hour
    X, y = create_dataset(data, look_back)

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
    print("predictions==========")
    print(predictions)
    return predictions
    # predictions = scaler.inverse_transform(np.hstack((predictions, np.zeros((predictions.shape[0], scaled_data.shape[1] - 1)))))[:, 0]
    # y_test = scaler.inverse_transform(np.hstack((y_test.reshape(-1, 1), np.zeros((y_test.shape[0], scaled_data.shape[1] - 1)))))[:, 0]

