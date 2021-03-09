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
        category = event.pattern_match.string.split(" ")[1]
    except IndexError:
        return await event.respond(f"select a category:```\ntoplist\nrandom\nhot\nlatest```")
    url = f"https://wallhaven.cc/{category}"
    try:
        tonsfw = '010' if event.pattern_match.string.split(" ")[2] == "nsfw" else "000"
    except IndexError:
        tonsfw = '000'
    try:
        #   120 is the limit of max pages
        res = requests.get(url,  {"page": randint(2, 40), "purity": tonsfw }, headers=USER_AGENT)
        logger.info(f"url generated {res.url}")
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
            await event.respond(f"Error occurred while sending, please try once again if file is too large\n here's full url to download manually{url}")
            logger.exception(e)
            pass
    except Exception as e:
        logger.exception(e)