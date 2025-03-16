import requests
import random


def fetch_aqi_data(city, token):
    """
    Fetch AQI data for a city using the AQICN API.
    """
    base_url = f"https://api.waqi.info/feed/{city}/?token={token}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "aqi" in data["data"]:
            return data["data"]
        else:
            return {"error": "No data available"}
    else:
        return {"error": f"Error {response.status_code}: Unable to fetch data"}


def dynamic_suggestions(aqi, industry_count, vehicle_population, weather_condition):
    """
    Generate dynamic suggestions based on AQI, industry, vehicle population, and weather conditions.
    """
    base_suggestions = {
        "low": [
            "Promote carpooling and public transport to maintain good air quality.",
            "Encourage industries to adopt green practices.",
            "Increase awareness campaigns about sustainable living."
        ],
        "moderate": [
            "Limit heavy vehicle movement during peak hours.",
            "Ensure routine emissions checks for vehicles and industries.",
            "Encourage planting trees in industrial and urban areas."
        ],
        "high": [
            "Implement odd-even vehicle policies temporarily.",
            "Introduce stricter emissions control for industries.",
            "Advise people to reduce outdoor activities and use air purifiers."
        ],
        "hazardous": [
            "Declare an emergency and halt high-emission industries temporarily.",
            "Restrict vehicle movement except for essential services.",
            "Provide masks and health advisories to citizens."
        ]
    }
    try:
        if aqi <= 50:
            level = "low"
        elif aqi <= 100:
            level = "moderate"
        elif aqi <= 200:
            level = "high"
        else:
            level = "hazardous"
    except:
        level = "low"

    # Randomize suggestions for variability
    suggestions = random.sample(base_suggestions[level], k=min(2, len(base_suggestions[level])))

    # Add contextual suggestions
    if industry_count > 50:
        suggestions.append("Enforce pollution control regulations for industries.")
    if vehicle_population > 100000:
        suggestions.append("Expand public transport infrastructure to reduce private vehicle use.")
    if "rain" in weather_condition.lower():
        suggestions.append("Utilize the rainy season to clean roads and reduce dust particles.")

    return suggestions


# Example usage
def fetch_aqi_data_sug(aqi):
    city = "Kozhikode"
    api_token = "de474c37bfef960bc38f8b88bf88cf81dddf6c52"  # Replace with your AQICN API token
    industry_count = 70
    vehicle_population = 120000
    weather_condition = "clear"

    # data = fetch_aqi_data(city, api_token)
    if True:
        aqi = float(aqi)
        suggestions = dynamic_suggestions(aqi, industry_count, vehicle_population, weather_condition)
        print(f"Current AQI for {city}: {aqi}")
        print("Suggestions:")
        return suggestions[:2]

        # sug=[]
        # for suggestion in suggestions:
        #     print(f"- {suggestion}")
        #     sug.append(suggestion)

    else:
        aqi = 100
        suggestions = dynamic_suggestions(aqi, industry_count, vehicle_population, weather_condition)
        print(f"Current AQI for {city}: {aqi}")
        print("Suggestions:")
        return suggestions

