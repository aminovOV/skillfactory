import requests
import json
# import time
from settings import WEATHER_API_KEY


class Weather:
    def __init__(self, location=None):
        self.location = location
        self.url = f'https://api.openweathermap.org/data/2.5/weather?q={self.location}&APPID=' \
                   f'{WEATHER_API_KEY}&lang=ru&units=metric'
        self.response = requests.get(self.url)
        self.weather_data = json.loads(self.response.text)

    def get_weather(self):
        w = self.weather_data
        return f'Погода в городе {w["name"]} сейчас:\n\nТемпература     {round(w["main"]["temp"])} °C\n' \
               f'Ощущается, как  {round(w["main"]["feels_like"])} °C\n' \
               f'Минимальная     {round(w["main"]["temp_min"])} °C\n' \
               f'Максимальная    {round(w["main"]["temp_max"])} °C\n' \
               f'{w["weather"][0]["description"].capitalize()}\n' \
               f'Скорость ветра  {round(w["wind"]["speed"])} м/с\n' \
               f'Влажность       {w["main"]["humidity"]}%\n' \
               f'Давление        {round(w["main"]["pressure"] * 0.75)} мм рт.ст.\n' \
               # f'Восход          {time.strftime("%H:%M", time.localtime(w["sys"]["sunrise"]))}\n' \
               # f'Заход           {time.strftime("%H:%M", time.localtime(w["sys"]["sunset"]))}\n'


class WeatherByGeolocation(Weather):
    def __init__(self, lat, lon):
        super().__init__()
        self.lat = lat
        self.lon = lon
        self.url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&APPID=' \
                   f'{WEATHER_API_KEY}&lang=ru&units=metric'
        self.response = requests.get(self.url)
        self.weather_data = json.loads(self.response.text)


if __name__ == '__main__':
    city_1 = Weather('Москва')
    print(city_1.get_weather())
    city_2 = WeatherByGeolocation("55.5804", "54.4435")
    print(city_2.get_weather())
