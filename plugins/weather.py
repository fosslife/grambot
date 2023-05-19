import requests
from userbot import bot, logger
from telethon import TelegramClient, events
from os import environ
import re
from config import weather


@bot.on(events.NewMessage(**weather))
async def get_weather(event):
    logger.info("weather plugin called")
    query = event.pattern_match.string.split(" ")
    logger.info(f"weather query - {query}")
    openweather_api_key = environ.get("openweather_api_key", None)

    if len(query) == 1:
        logger.info(f"no city provided")
        await event.respond("Please provide a city name")
        return
    elif len(query) == 2:
        city_to_find = query[1]
        logger.info(f"city to find - {city_to_find}")

        latinfo = get_lat_lon_from_city(city_to_find)
        if latinfo is None:
            await event.respond("City not found")
            return
        lat, lon = latinfo

        logger.info(f"Sending current weather info")
        openweather_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": openweather_api_key,
            "units": "metric",
        }
        weather_res = get_response(openweather_url, params)
        tg_response = format_weather_response(weather_res)
        await event.respond(tg_response)
        return
    elif len(query) == 3 and query[2] == "forecast":
        logger.info(f"forecast")
        await event.respond("Forecast not implemented yet")
        return
    elif len(query) == 3 and query[2] == "air":
        city_to_find = query[1]
        logger.info(f"city to find - {city_to_find}")

        latinfo = get_lat_lon_from_city(city_to_find)
        if latinfo is None:
            await event.respond("City not found")
            return
        lat, lon = latinfo

        logger.info(f"Sending current air pollution info")
        openweather_url = "https://api.openweathermap.org/data/2.5/air_pollution"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": openweather_api_key,
            "units": "metric",
        }
        weather_res = get_response(openweather_url, params)
        tg_response = format_air_pollution_response(weather_res, city_to_find)
        await event.respond(tg_response)


def get_lat_lon_from_city(city_to_find):
    # Prepare request
    openweather_api_key = environ.get("openweather_api_key", None)
    params = {"q": city_to_find, "appid": openweather_api_key}

    # get geocoding lat log first
    geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
    geocoding_res = get_response(geocoding_url, params)
    if len(geocoding_res) == 0:
        # logger.info(f"geocoding response - {geocoding_res}")
        return
    # logger.info(f"geocoding response - {geocoding_res}")

    lat, lon = geocoding_res[0]["lat"], geocoding_res[0]["lon"]
    return lat, lon


def get_response(url, params):
    res = requests.get(url, params=params).json()
    return res


def format_weather_response(weather_res):
    try:
        weather_icons = {
            "01d": "☀️",
            "01n": "☀️",
            "02d": "🌤️",
            "02n": "🌤️",
            "03d": "⛅",
            "03n": "⛅",
            "04d": "🌥️",
            "04n": "🌥️",
            "09d": "🌦️",
            "09n": "🌦️",
            "10d": "🌧️",
            "10n": "🌧️",
            "11d": "⛈️",
            "11n": "⛈️",
            "13d": "❄️",
            "13n": "❄️",
            "50d": "🌫️",
            "50n": "🌫️"
        }
        # logger.info(f"request to format {weather_res}")
        temp_in_celcius = weather_res["main"]["temp"]
        feels_like = weather_res["main"]["feels_like"]
        temp_min = weather_res["main"]["temp_min"]
        temp_max = weather_res["main"]["temp_max"]
        humidity = weather_res["main"]["humidity"]
        pressure = weather_res["main"]["pressure"]
        sky = weather_res["weather"][0]["description"]
        icon = weather_res["weather"][0]["icon"]
        city = weather_res["name"]
        country = weather_res["sys"]["country"]
        wind = weather_res["wind"]["speed"]
        if "rain" in weather_res:
            rain = weather_res["rain"]["1h"]
        else:
            rain = 0
        if "snow" in weather_res:
            snow = weather_res["snow"]["1h"]
        else:
            snow = 0
        cloud_coverage = weather_res["clouds"]["all"]
        # print("\n\n", re.findall("", pattern_string))
        return f"""
```
Weather: {city},{country} - {weather_icons[icon]} {sky} 

Temperature:      {temp_in_celcius:.2f}°C,
Feels like:       {feels_like:.2f}°C
Min:              {temp_min:.2f}°C
Max:              {temp_max:.2f}°C

Humidity:         {humidity}%
Pressure:         {pressure} Pa 
Wind:             {wind} meter/sec
Rain:             {rain} cm (last 1 hour)
Snow:             {snow} mm (last 1 hour)

Clouds:           {cloud_coverage}% Coverage
```
"""
    except KeyError as e:
        logger.exception(f"Error in formatting {e}")
        pass
    except Exception as e:
        print("Error", weather_res)
        logger.exception(f"Error in formatting {e}")


def format_air_pollution_response(air_response, location):
    print(air_response)

    aqi_emojis_dict = {
        "1": "🟢",
        "2": "🟡",
        "3": "🟠",
        "4": "🔴",
        "5": "🟤",
    }

    aqi = air_response["list"][0]["main"]["aqi"] 
    co2 = air_response["list"][0]["components"]["co"]
    no = air_response["list"][0]["components"]["no"]
    no2 = air_response["list"][0]["components"]["no2"]
    o3 = air_response["list"][0]["components"]["o3"]
    so2 = air_response["list"][0]["components"]["so2"]
    pm2_5 = air_response["list"][0]["components"]["pm2_5"]
    pm10 = air_response["list"][0]["components"]["pm10"]
    nh3 = air_response["list"][0]["components"]["nh3"]

    return f"""
Air Pollution: __{location}__

Air Quality Index: {aqi_emojis_dict[str(aqi)]} __{aqi}__

CO: __{co2} μg/m³__ (Carbon Monoxide)
NO: __{no} μg/m³__ (Nitrogen Monoxide)
NO2: __{no2} μg/m³__ (Nitrogen Dioxide)
O3: __{o3} μg/m³__ (Ozone)
SO2: __{so2} μg/m³__ (Sulfur Dioxide)
PM2.5: __{pm2_5} μg/m³__ (Fine Particulate Matter)
PM10: __{pm10} μg/m³__ (Coarse Particulate Matter)
NH3: __{nh3} μg/m³__ (Ammonia)

"""



""" 
note:
```
CO - Carbon Monoxide
NO - Nitrogen Monoxide
NO2 - Nitrogen Dioxide
O3 - Ozone
SO2 - Sulfur Dioxide
PM2.5 - Fine Particulate Matter
PM10 - Coarse Particulate Matter
NH3 - Ammonia
```
"""