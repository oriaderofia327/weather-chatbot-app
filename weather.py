import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("API_KEY")



# Ask user for city
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check if city exists
if response.status_code == 200:

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["main"]
    country = data["sys"]["country"]


    print(f"\nWeather in {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Country : {country}") 

else:
    print(data)
