import requests
from userbot import bot
from telethon import TelegramClient, events
from os import environ
import re

@bot.on(events.NewMessage(pattern='\.weather'))
async def getWeather(event):
    pattern_string = event.pattern_match.string
    city_to_find = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    openweather_url = "https://api.openweathermap.org/data/2.5/weather"
    openweather_api_key = environ.get("openweather_api_key", None)
    params = { "q" : city_to_find, "appid": openweather_api_key }
    res = requests.get(openweather_url, params=params).json()
    temp_in_celcius = res['main']['temp'] -  273.15
    humidity = res['main']['humidity']
    pressure = res['main']['pressure']
    sky = res['weather'][0]['description']
    city = res['name']
    country = res['sys']['country']
    # print("\n\n", re.findall("", pattern_string))
    await event.respond(f"Temp in `{city},{country}` is `{temp_in_celcius:.2f}°C`, {sky}\nHumidity `{humidity}`%\nPressure `{pressure}` Pa")
    