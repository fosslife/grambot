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
    try:
        city_to_find = query[1]
    except IndexError:
        logger.info("No city provided")
        await event.respond("Please provide a city name")
        return
    try:
        is_forecast = query[2] or None
    except IndexError:
        is_forecast = None
    # print(is_forecast)
    logger.info(f"city to find - {city_to_find}")

    # Prepare request
    openweather_api_key = environ.get("openweather_api_key", None)
    params = {"q": city_to_find, "appid": openweather_api_key}

    # get geocoding lat log first
    geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
    geocoding_res = get_response(geocoding_url, params)
    logger.info(f"geocoding response - {geocoding_res}")
    # await event.respond("done")
    # return

    lat, lon = geocoding_res[0]["lat"], geocoding_res[0]["lon"]

    if is_forecast is None:
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
    # else:
    #     logger.info(f"sending forecast")
    #     openweather_url = "https://api.openweathermap.org/data/2.5/forecast"
    #     days_list = get_response(openweather_url, params)
    #     tg_response = "**Sending 5 days forecast**\n"
    #     try:
    #         for day in range(len(days_list['list'])):
    #             print("Day ", day);
    #             tg_response = f"Day **{day+1}**\n"
    #             days_list['list'][day]['name'] = days_list['city']['name']
    #             tg_response += format_weather_response(days_list['list'])
    #         await event.respond(tg_response)
    #     except Exception as e:
    #         logger.exception(f"{e}")


def get_response(url, params):
    res = requests.get(url, params=params).json()
    return res


def format_weather_response(weather_res):
    try:
        logger.info(f"request to format {weather_res}")
        temp_in_celcius = weather_res["main"]["temp"]
        feels_like = weather_res["main"]["feels_like"]
        temp_min = weather_res["main"]["temp_min"]
        temp_max = weather_res["main"]["temp_max"]
        humidity = weather_res["main"]["humidity"]
        pressure = weather_res["main"]["pressure"]
        sky = weather_res["weather"][0]["description"]
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
Weather: __{city},{country}__ - __{sky}__

Temperature:  __{temp_in_celcius:.2f}°C__,
Feels like:  __{feels_like:.2f}°C__
Min:  __{temp_min:.2f}°C__
Max:  __{temp_max:.2f}°C__

Humidity:  __{humidity}%__
Pressure:  __{pressure} Pa__ 
Wind:  __{wind} meter/sec__
Rain:  __{rain} cm__ (last 1 hour)
Snow:  __{snow} mm__ (last 1 hour)

Clouds:  __{cloud_coverage}%__ Coverage
"""
    except KeyError as e:
        logger.exception(f"Error in formatting {e}")
        pass
    except Exception as e:
        print("Error", weather_res)
        logger.exception(f"Error in formatting {e}")
