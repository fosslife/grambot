from userbot import bot, logger
from telethon import TelegramClient, events
from config import omni
import requests
from os import environ

@bot.on(events.NewMessage(**omni))
async def omnifn(event):
    logger.info("omni plugin called")
    appid = environ.get("wolfram_appid", None)
    if not appid:
        await event.respond("no appid provided")
        return
    pattern_string = event.pattern_match.string
    query_string = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    if not query_string:
        await event.respond("please provide (a query to search)")
    query_params = query_string.replace(" ", "+")
    url = f"https://api.wolframalpha.com/v2/query?input={query_params}"
    res = requests.get(url,  {
        "format": "plaintext",
        "output": "JSON",
        "appid": appid
        })
    res_json = res.json()
    pods = res_json['queryresult']['pods']
    result_pod = ''
    for o in pods:
        if o['title'] == "Result":
            result_pod = o
    # print(result_pod)
    await event.respond(result_pod['subpods'][0]['plaintext'])