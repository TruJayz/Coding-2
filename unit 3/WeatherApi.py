import requests


lat = 40.71
ion = 74.01


url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={ion}&current_weather=true"

response = requests.get(url)
data = response.json()


current = data["current_weather"]
temp = current["temperature"]
wind = current["windspeed"]
print(f"Current temperature: {temp}°C")
print(f"Wind speed: {wind} km/h")