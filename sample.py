# # # import requests
# # # import datetime
# # # import csv
# # #
# # #
# # # # Function to fetch air pollution data
# # # def fetch_air_pollution_data(lat, lon, start, end, api_key):
# # #     url = f"http://api.openweathermap.org/data/2.5/air_pollution/history"
# # #     params = {
# # #         "lat": lat,
# # #         "lon": lon,
# # #         "start": start,
# # #         "end": end,
# # #         "appid": api_key
# # #     }
# # #     try:
# # #         response = requests.get(url, params=params)
# # #         response.raise_for_status()
# # #         return response.json()
# # #     except requests.exceptions.RequestException as e:
# # #         print(f"Error: {e}")
# # #         return None
# # #
# # #
# # # # Function to save data to CSV
# # # def save_to_csv(data, filename):
# # #     with open(filename, mode='w', newline='') as file:
# # #         writer = csv.writer(file)
# # #         # Writing header
# # #         writer.writerow(["Datetime", "CO", "NO", "NO2", "O3", "SO2", "PM2.5", "PM10", "NH3"])
# # #
# # #         for entry in data:
# # #             timestamp = entry["dt"]
# # #             components = entry["components"]
# # #             writer.writerow([
# # #                 datetime.datetime.fromtimestamp(timestamp),
# # #                 components.get("co", ""),
# # #                 components.get("no", ""),
# # #                 components.get("no2", ""),
# # #                 components.get("o3", ""),
# # #                 components.get("so2", ""),
# # #                 components.get("pm2_5", ""),
# # #                 components.get("pm10", ""),
# # #                 components.get("nh3", "")
# # #             ])
# # #
# # #
# # # # Main script
# # # if __name__ == "__main__":
# # #     # Input values
# # #     lat = 37.7749  # Example latitude (San Francisco)
# # #     lon = -122.4194  # Example longitude (San Francisco)
# # #     start_date = datetime.datetime(2024, 10, 1)
# # #     end_date = datetime.datetime(2025, 1, 1)
# # #     api_key = "cd23d18e873a64aa6069e12a93c208dd"  # Replace with your OpenWeatherMap API key
# # #     filename = "air_pollution_data.csv"
# # #
# # #     # Splitting the date range into smaller chunks (if needed)
# # #     start_timestamp = int(start_date.timestamp())
# # #     end_timestamp = int(end_date.timestamp())
# # #
# # #     # Fetching data
# # #     print("Fetching air pollution data...")
# # #     data = fetch_air_pollution_data(lat, lon, start_timestamp, end_timestamp, api_key)
# # #
# # #     # Save to CSV if data exists
# # #     if data and "list" in data:
# # #         print(f"Saving data to {filename}...")
# # #         save_to_csv(data["list"], filename)
# # #         print(f"Data saved successfully to {filename}")
# # #     else:
# # #         print("No data fetched or an error occurred.")
# # import requests
# # import datetime
# # import csv
# # import time
# #
# #
# # # Function to fetch air pollution data
# # def fetch_air_pollution_data(lat, lon, start, end, api_key):
# #     url = "http://api.openweathermap.org/data/2.5/air_pollution/history?lat=11.45678&lon=75.456&start=2024-10-10&end=2025-01-01&appid=4a71ee40c8c4a56bd5285b77e1aff85b"
# #     try:
# #         response = requests.get(url)
# #         response.raise_for_status()
# #         return response.json()
# #     except requests.exceptions.RequestException as e:
# #         print(f"Error: {e}")
# #         return None
# #
# #
# # # Function to save data to CSV
# # def save_to_csv(data, filename):
# #     with open(filename, mode='w', newline='') as file:
# #         writer = csv.writer(file)
# #         # Writing header
# #         writer.writerow(["Datetime", "CO", "NO", "NO2", "O3", "SO2", "PM2.5", "PM10", "NH3"])
# #
# #         for entry in data:
# #             timestamp = entry["dt"]
# #             components = entry["components"]
# #             writer.writerow([
# #                 datetime.datetime.fromtimestamp(timestamp),
# #                 components.get("co", ""),
# #                 components.get("no", ""),
# #                 components.get("no2", ""),
# #                 components.get("o3", ""),
# #                 components.get("so2", ""),
# #                 components.get("pm2_5", ""),
# #                 components.get("pm10", ""),
# #                 components.get("nh3", "")
# #             ])
# #
# #
# # # Main script
# # if __name__ == "__main__":
# #     # Input values
# #     lat = 37.7749  # Example latitude (San Francisco)
# #     lon = -122.4194  # Example longitude (San Francisco)
# #     start_date = datetime.datetime(2024, 10, 1)
# #     end_date = datetime.datetime(2025, 1, 1)
# #     api_key = "4a71ee40c8c4a56bd5285b77e1aff85b"  # Replace with your OpenWeatherMap API key
# #     filename = "air_pollution_data.csv"
# #
# #     # Splitting the date range into smaller chunks (if necessary)
# #     current_date = start_date
# #     data_list = []
# #
# #     print("Fetching air pollution data...")
# #     while current_date < end_date:
# #         # Get timestamps for the current range
# #         start_timestamp = int(current_date.timestamp())
# #         next_date = current_date + datetime.timedelta(days=5)  # Fetch 5 days of data at a time
# #         end_timestamp = int(min(next_date.timestamp(), end_date.timestamp()))
# #
# #         # Fetch data
# #         data = fetch_air_pollution_data(lat, lon, start_timestamp, end_timestamp, api_key)
# #         if data and "list" in data:
# #             data_list.extend(data["list"])
# #         else:
# #             print(f"No data for {current_date} to {next_date}")
# #
# #         # Move to the next range
# #         current_date = next_date
# #         time.sleep(1)  # Avoid hitting API rate limits
# #
# #     # Save to CSV if data exists
# #     if data_list:
# #         print(f"Saving data to {filename}...")
# #         save_to_csv(data_list, filename)
# #         print(f"Data saved successfully to {filename}")
# #     else:
# #         print("No data fetched or an error occurred.")
#
#
# import openmeteo_requests
#
# import requests_cache
# import pandas as pd
# from retry_requests import retry
#
# # Setup the Open-Meteo API client with cache and retry on error
# cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
# retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
# openmeteo = openmeteo_requests.Client(session = retry_session)
#
# # Make sure all required weather variables are listed here
# # The order of variables in hourly or daily is important to assign them correctly below
# url = "https://air-quality-api.open-meteo.com/v1/air-quality"
# params = {
# 	"latitude": 52.52,
# 	"longitude": 13.41,
# 	"hourly": ["pm10", "pm2_5"]
# }
# responses = openmeteo.weather_api(url, params=params)
#
# # Process first location. Add a for-loop for multiple locations or weather models
# response = responses[0]
# print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
# print(f"Elevation {response.Elevation()} m asl")
# print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
# print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
#
# # Process hourly data. The order of variables needs to be the same as requested.
# hourly = response.Hourly()
# hourly_pm10 = hourly.Variables(0).ValuesAsNumpy()
# hourly_pm2_5 = hourly.Variables(1).ValuesAsNumpy()
#
# hourly_data = {"date": pd.date_range(
# 	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
# 	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
# 	freq = pd.Timedelta(seconds = hourly.Interval()),
# 	inclusive = "left"
# )}
# hourly_data["pm10"] = hourly_pm10
# hourly_data["pm2_5"] = hourly_pm2_5
#
# hourly_dataframe = pd.DataFrame(data = hourly_data)
# print(hourly_dataframe)


fname=r"C:\Users\GAYATHRI\Downloads\New folder\archive\station_day.csv"

import csv
date=[]
co=[]
# Open the CSV file
filename = "your_file.csv"  # Replace with your CSV file path
with open(fname, mode='r') as file:
    csv_reader = csv.reader(file)

    # Read and print the header (optional)
    header = next(csv_reader)
    print(f"Header: {header}")

    # Read and print each row
    for row in csv_reader:
        print(row)
        date.append(row[1])
        try:
            co.append(float(row[8]))
        except:
            co.append(0.0)

