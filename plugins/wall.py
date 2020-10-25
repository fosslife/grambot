from userbot import bot, logger
from telethon import TelegramClient, events
from telethon.tl import types
from bs4 import BeautifulSoup
import requests
from config import wall
from random import randint, choice

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


@bot.on(events.NewMessage(**wall))
async def wall(event):
    logger.info("Wallpaper plugin called")
    try:
        res = requests.get('https://wallhaven.cc/toplist',  {"page": randint(2, 120) }, headers=USER_AGENT)
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            page = soup.find("section", {"class": "thumb-listing-page"})
            ls = page.findChildren("li")
            selectedls = choice(ls)
            thumbinfo = selectedls.findChild("div", {"class": "thumb-info"})
            imageid = selectedls.findChild().get("data-wallpaper-id")
            url = f"https://w.wallhaven.cc/full/{imageid[:2]}/wallhaven-{imageid}."
            isPng = thumbinfo.findChild("span", {"class": "png"}, recursive=True)
            if isPng is None:
                url = url + "jpg"
            else:
                url = url + "png"
            logger.info(f"url is {url}")
            await event.respond(file=types.InputMediaPhotoExternal(url))
        except Exception as e:
            await event.respond("Error occurred while sending, please try once again if file is too large")
            logger.exception(e)
    except Exception as e:
        logger.exception(e)