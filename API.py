import requests
from datetime import datetime


latitude = input("Enter the latitude: ")
longitude = input("Enter the longitude: ")

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation"

response = requests.get(url)

data = response.json()

times = data["hourly"] ["time"]
Temperature = data["hourly"] ["temperature_2m"]
precipitation = data["hourly"] ["precipitation"]

print(f"The temperature and precipitation at {latitude} and {longitude} for past five hours are: ")
for i in range(6):
    dt = datetime.strptime(times[i], "%Y-%m-%dT%H:%M")
    local_time = dt.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{local_time} --> {Temperature[i]} , {precipitation[i]} .")