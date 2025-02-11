**🚀 Weather Data Collection Project**
📌 Author: BIBEK SHARMA
📌 Date Created: 2025-02-05
📌 Last Updated: 2025-02-05

📌 Project Description
This project collects daily weather data for a specified location using the OpenWeatherMap API. The collected data includes:

**Temperature (°C)
Humidity (%)
Wind Speed (m/s)
Precipitation (mm)**
The dataset is stored in CSV format and is accompanied by a metadata.json file following Dublin Core and ISO 19115 metadata standards.

📌 Folder Structure
WeatherData/
│── weather_data.csv        # Main dataset with collected weather metrics
│── metadata.json           # Metadata file describing the dataset
│── Convert_Json.py         # Python script to convert metadata.json to Excel
│── README.md               # Project documentation
📌 Installation & Setup
🔹 1. Prerequisites
Before running the script, ensure you have:

Python 3.7+
Required Python libraries:
pip install requests pandas openpyxl
🔹 2. Getting Your OpenWeatherMap API Key
Go to OpenWeatherMap
Sign up (if you don’t have an account)
Generate a free API key and replace "YOUR_API_KEY" in the script.
📌 How to Run the Script
🔹 Step 1: Collect Weather Data
Run the following Python script to fetch and store real-time weather data:

python Convert_Json.py
This will:

Fetch weather data from OpenWeatherMap API.
Save the data in weather_data.csv.
Generate a metadata.json file with dataset details.
📌 Output Files
File Name	Description
weather_data.csv	Contains collected weather data.
metadata.json	Stores metadata about the dataset.
metadata.xlsx	(Optional) Metadata converted to Excel format.
📌 Example Dataset (weather_data.csv)
Date	Temperature (°C)	Humidity (%)	Wind Speed (m/s)	Precipitation (mm)
2024-02-01	8.5	72	4.5	1.2
2024-02-02	7.2	78	3.9	0.0
📌 Example Metadata (metadata.json)
{
    "Title": "Daily Weather Data for New York, USA",
    "Creator": "Your Name",
    "Date Created": "2024-02-05",
    "Description": "Dataset containing daily weather metrics (temperature, humidity, wind speed, and precipitation) for New York over a 7-day period.",
    "Location": "New York, USA",
    "Timeframe": "2024-01-29 to 2024-02-04",
    "Columns": ["Date", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Precipitation (mm)"],
    "Collection Method": "Python script using OpenWeatherMap API",
    "Environment": "Python (Jupyter Notebook/Google Colab)",
    "Data Format": "CSV (.csv)",
    "Metadata Standards": ["Dublin Core", "ISO 19115"]
}
📌 Data Backup & Storage
Primary Storage: The dataset is stored locally in the WeatherData/ folder.
Backup Storage: Recommended backup options:
Google Drive (manual upload or sync)
GitHub repository (for version control)
Zenodo (for public sharing)
📌 Future Improvements
✅ Expand to Multiple Locations
✅ Increase Data Collection Period (e.g., 30 days instead of 7 days)
✅ Automate Data Collection Using Cron Jobs

📌 License
This dataset is provided under the MIT License. You are free to use, modify, and distribute it with proper attribution.

📌 Contact Informati on
Author: Bibek Sharma

✅ Ready to Contribute?
Feel free to submit a pull request if you’d like to improve the dataset or scripts! 🚀
