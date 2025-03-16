import requests
import pandas as pd
from datetime import datetime, timedelta
import random



# Replace with your WAQI API Key
API_KEY = 'de474c37bfef960bc38f8b88bf88cf81dddf6c52'

# Station ID (search for your station on the WAQI website)
station_id = '80'

# Calculate the timestamp for 100 days ago
end_date = datetime.utcnow()
start_date = end_date - timedelta(days=100)

# Convert to Unix timestamps
start_timestamp = int(start_date.timestamp())
end_timestamp = int(end_date.timestamp())
def dataget():

    # API endpoint for historical air quality data
    url = f'https://api.waqi.info/feed/here/?token=de474c37bfef960bc38f8b88bf88cf81dddf6c52'

    # Send the request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        x = []
        y = []

        print(data)
        for i in range(11):
            pm10_data = data['data']['forecast']['daily']['pm10']
            j=0
            # Print day and pm10 values
            for record in pm10_data:
                j+=1
                random_integer = random.randint(1, 10)
                x.append(i*len(pm10_data)+j)
                day = record['day']
                pm10_value = record['avg']
                y.append(float(pm10_value)+random_integer)
                print(f"Day: {day}, PM10 Average: {pm10_value}")
        print(x)
        print(y)
        return x,y
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
