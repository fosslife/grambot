from userbot import bot, logger
from telethon import TelegramClient, events
from config import google
from bs4 import BeautifulSoup
import requests
import re

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

@bot.on(events.NewMessage(**google))
async def googlefn(event):
    logger.info("google plugin called")
    pattern_string = event.pattern_match.string
    query_string = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    logger.info(f"query string to search {query_string}")
    query_params = query_string.replace(" ", "+")
    res = requests.get('https://www.google.com/search',  {"q": query_params}, headers=USER_AGENT)
    soup = BeautifulSoup(res.text, 'html.parser')
    # first try to find div tag with attribute data-tts and data-tts-text
    try:
        tts_text = soup.findAll("div", {"data-tts" : True, "data-tts-text" : True})
        # there should be only one element present:
        try:
            msg = tts_text[0].text
            await event.respond(msg)
            logger.info("found record with attribute type tts_text")
            return # don't execute this method further
        except IndexError:
            pass
        # that means try another method:
        attr_kc_text = soup.findAll("div", {"data-attrid" : re.compile(r"^kc:/\w+/\w+:\w+")})
        # if there's any such tag
        if attr_kc_text:
            # it's probably in the second child of div tag with this attribute:   
            try:
                msg = attr_kc_text[0].findChild().findChild("div", {"role": "heading"}).text
                await event.respond(msg)
                logger.info("found record with attribute type kc:/x/x in second div")
                return
            except AttributeError:
                msg = attr_kc_text[0].findChild("div", {"role": "heading"}).findChild().text
                await event.respond(msg)
                logger.info("found record with attribute type kc:/x/x in first div")
                return # don't execute this method further
        # else search for another attribute type
        attr_hc_text = soup.findAll("div", {"data-attrid" : re.compile(r"^hw:/\w+/\w+:\w+")})
        # if it's present
        if attr_hc_text:
            # same logic
            msg = attr_hc_text[0].findChild().findChild().text
            await event.respond(msg)
            logger.info("found record with attribute type hw:/x/x in second div")
            return # don't execute this method further
        # Well, everything up above failed, try another methods:
        # Let's see if it's a time-related card
        rso = soup.find(id="rso")
        card = rso.findChildren("div", {"class": "card-section"}, recursive=True)
        try:
            time = card[0].findChild().text
            await event.respond(time)
            logger.info("found record as time card")
            return
        except Exception:
            pass
        # it's not a time card either
    except Exception:
        logger.info("couldn't find anything")
        await event.respond("can't find anything on that, please report this query to Spark")
