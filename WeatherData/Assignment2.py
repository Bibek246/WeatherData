import requests
import pandas as pd
import datetime
import json
import os

# ✅ CONFIGURATION - REPLACE WITH YOUR OWN DETAILS
API_KEY = "49bf24b7315b47c6b60d383a6aec5554"  #
CITY = "Idaho"  # Change this to your preferred location
COUNTRY = "USA"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ✅ Create a directory for storing data
FOLDER_NAME = "WeatherData"
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

# ✅ List to store collected data
weather_data = []

# ✅ Collect weather data for the past 7 days
for i in range(7):
    date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    
    # API Request Parameters
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }
    
    # Fetch data from OpenWeatherMap API
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_data.append({
            "Date": date,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Wind Speed (m/s)": data["wind"]["speed"],
            "Precipitation (mm)": data["rain"]["1h"] if "rain" in data and "1h" in data["rain"] else 0
        })
    else:
        print(f"⚠️ Failed to retrieve data for {date}")

# ✅ Convert collected data to DataFrame
weather_df = pd.DataFrame(weather_data)

# ✅ Save the dataset to a CSV file
csv_file_path = os.path.join(FOLDER_NAME, "weather_data.csv")
weather_df.to_csv(csv_file_path, index=False)

print(f"✅ Weather data successfully saved as {csv_file_path}")

# ✅ Define metadata
metadata = {
    "Title": f"Daily Weather Data for {CITY}, {COUNTRY}",
    "Creator": "Your Name",
    "Date Created": datetime.datetime.now().strftime("%Y-%m-%d"),
    "Description": f"Dataset containing daily weather metrics (temperature, humidity, wind speed, and precipitation) for {CITY} over a 7-day period.",
    "Location": f"{CITY}, {COUNTRY}",
    "Timeframe": f"{(datetime.datetime.now() - datetime.timedelta(days=6)).strftime('%Y-%m-%d')} to {datetime.datetime.now().strftime('%Y-%m-%d')}",
    "Columns": ["Date", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Precipitation (mm)"],
    "Data Types": {
        "Date": "String (YYYY-MM-DD)",
        "Temperature": "Numeric (°C)",
        "Humidity": "Numeric (%)",
        "Wind Speed": "Numeric (m/s)",
        "Precipitation": "Numeric (mm)"
    },
    "Units": {
        "Temperature": "Degrees Celsius",
        "Humidity": "Percentage",
        "Wind Speed": "Meters per second",
        "Precipitation": "Millimeters"
    },
    "Collection Method": "Python script using OpenWeatherMap API",
    "Environment": "Python (Jupyter Notebook/Google Colab)",
    "Extraction Date": datetime.datetime.now().strftime("%Y-%m-%d"),
    "Motivation": "Understanding daily weather trends in a specific location.",
    "Scope": "Analyze short-term weather variations and compare with seasonal norms.",
    "Future Changes": "Expand dataset to include multiple cities and longer timeframes.",
    "Data Format": "CSV (.csv)",
    "Metadata Standards": ["Dublin Core", "ISO 19115"]
}

# ✅ Save metadata as a JSON file
metadata_file_path = os.path.join(FOLDER_NAME, "metadata.json")
with open(metadata_file_path, "w") as json_file:
    json.dump(metadata, json_file, indent=4)

print(f"✅ Metadata successfully saved as {metadata_file_path}")
