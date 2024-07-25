import requests
import tkinter as tki
from tkinter import messagebox

api_key = 'ec2b6cec8b67a520a7721de6d0aa0551'


def get_weather(city):
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"Other error occurred: {err}"


def display_weather(data):
    if isinstance(data, dict):
        city = data.get('name')
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']

        weather_info = f"""
        City: {city}
        Temperature: {temp}°C
        Weather: {weather}
        Wind Speed: {wind_speed} m/s
        Humidity: {humidity}%
        """
        messagebox.showinfo("Weather Information", weather_info)
    else:
        messagebox.showerror("Error", data)


def fetch_weather():
    city = city_entry.get().strip()
    if city:
        weather_data = get_weather(city)
        display_weather(weather_data)
    else:
        messagebox.showwarning("Input Error", "City name cannot be empty.")


root = tki.Tk()
root.title("Weather App")

tki.Label(root, text="Enter City Name:").pack(pady=10)

city_entry = tki.Entry(root)
city_entry.pack(pady=5)

tki.Button(root, text="Get Weather", command=fetch_weather).pack(pady=20)

root.mainloop()
