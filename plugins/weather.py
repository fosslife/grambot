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
    city_to_find = query[1]
    try:
        is_forecast = query[2] or None
    except IndexError:
        is_forecast = None
    # print(is_forecast)
    logger.info(f"city to find - {city_to_find}")

    # Prepare request
    openweather_api_key = environ.get("openweather_api_key", None)
    params = {"q": city_to_find, "appid": openweather_api_key}
    if is_forecast is None:
        logger.info(f"Sending current weather info")
        openweather_url = "https://api.openweathermap.org/data/2.5/weather"
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
        temp_in_celcius = weather_res['main']['temp'] - 273.15
        humidity = weather_res['main']['humidity']
        pressure = weather_res['main']['pressure']
        sky = weather_res['weather'][0]['description']
        city = weather_res['name']
        country = weather_res['sys']['country']
        wind = weather_res['wind']['speed']
        rain = weather_res['rain']['1h']
        cloud_coverage = weather_res['clouds']['all']
        # print("\n\n", re.findall("", pattern_string))
        return f"""
Temp in `{city},{country}` is `{temp_in_celcius:.2f}°C`,
{sky}

Humidity `{humidity}`%
Pressure `{pressure}` Pa
Wind `{wind}` meter/sec
`{rain}` cm rain in last 1 hour
`{cloud_coverage}`% Cloud coverage
    """
    except Exception as e:
        print("Error", weather_res)
        logger.exception(f"Error in formatting {e}")
