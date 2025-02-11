import requests
import pandas as pd
import datetime
import json
import os

# CONFIGURATION 
NOAA_API_KEY = "uagEMkVRBjNQvHyUVEUDmOffkWEaMvSN"  # My actual NOAA API key
STATION_ID = "GHCND:USW00024131"  # Boise Airport, Idaho
BASE_URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"

# Define parameters for data collection
START_DATE = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d")  # 365 days ago
END_DATE = datetime.datetime.now().strftime("%Y-%m-%d")  # Today

# Create a directory for storing data
FOLDER_NAME = "WeatherData"
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

# NOAA Request Parameters
params = {
    "datasetid": "GHCND",  # Daily Global Historical Climatology Network
    "stationid": STATION_ID,
    "startdate": START_DATE,
    "enddate": END_DATE,
    "limit": 1000,
    "units": "metric",
    "datatypeid": ["TMAX", "TMIN", "PRCP", "AWND"],  # Max temp, Min temp, Precipitation, Wind speed
    "sortfield": "date",
    "sortorder": "asc"
}

headers = {"token": NOAA_API_KEY}  # Authorization header

# Fetch historical weather data
response = requests.get(BASE_URL, params=params, headers=headers)

# Check if the response is valid
if response.status_code == 200:
    data = response.json()
    records = data.get("results", [])

    # Convert NOAA response to structured format
    weather_data = []
    for record in records:
        date = record["date"][:10]  # Extract date from timestamp
        datatype = record["datatype"]
        value = record["value"]

        # Find existing record for the date or create new
        existing_record = next((item for item in weather_data if item["Date"] == date), None)
        if not existing_record:
            existing_record = {"Date": date, "Max Temperature (°C)": None, "Min Temperature (°C)": None, "Wind Speed (m/s)": None, "Precipitation (mm)": None}
            weather_data.append(existing_record)

        # Assign values based on datatype
        if datatype == "TMAX":
            existing_record["Max Temperature (°C)"] = round(value / 10, 2)  # Convert tenths of Celsius to Celsius
        elif datatype == "TMIN":
            existing_record["Min Temperature (°C)"] = round(value / 10, 2)
        elif datatype == "PRCP":
            existing_record["Precipitation (mm)"] = round(value / 10, 2)  # Convert tenths of mm to mm
        elif datatype == "AWND":
            existing_record["Wind Speed (m/s)"] = round(value, 2)  # NOAA returns wind speed in m/s

    # Convert to Pandas DataFrame
    weather_df = pd.DataFrame(weather_data)

    # Save the dataset to a CSV file
    csv_file_path = os.path.join(FOLDER_NAME, f"noaa_weather_data_{END_DATE}.csv")
    weather_df.to_csv(csv_file_path, index=False)

    print(f"✅ Weather data successfully saved as {csv_file_path}")

    # Define metadata
    metadata = {
        "Title": "Daily Historical Weather Data from NOAA",
        "Creator": "Your Name",
        "Date Created": datetime.datetime.now().strftime("%Y-%m-%d"),
        "Description": "Dataset containing daily historical weather metrics (temperature, humidity, wind speed, and precipitation) for a selected NOAA station.",
        "Location": "Station ID: " + STATION_ID,
        "Timeframe": f"{START_DATE} to {END_DATE}",
        "Columns": ["Date", "Max Temperature (°C)", "Min Temperature (°C)", "Wind Speed (m/s)", "Precipitation (mm)"],
        "Data Types": {
            "Date": "String (YYYY-MM-DD)",
            "Max Temperature": "Numeric (°C)",
            "Min Temperature": "Numeric (°C)",
            "Wind Speed": "Numeric (m/s)",
            "Precipitation": "Numeric (mm)"
        },
        "Units": {
            "Temperature": "Degrees Celsius",
            "Wind Speed": "Meters per second",
            "Precipitation": "Millimeters"
        },
        "Collection Method": "Python script using NOAA Climate Data Online (CDO) API",
        "Environment": "Python (Jupyter Notebook/Google Colab)",
        "Extraction Date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "Motivation": "Understanding past weather trends for a given location.",
        "Scope": "Analyze short-term historical weather variations.",
        "Data Format": "CSV (.csv)",
        "Metadata Standards": ["Dublin Core", "ISO 19115"]
    }

    # Save metadata as a JSON file
    metadata_file_path = os.path.join(FOLDER_NAME, "noaa_metadata.json")
    with open(metadata_file_path, "w") as json_file:
        json.dump(metadata, json_file, indent=4)

    print(f"✅ Metadata successfully saved as {metadata_file_path}")

else:
    print(f"⚠️ Failed to retrieve data. Response: {response.text}")
