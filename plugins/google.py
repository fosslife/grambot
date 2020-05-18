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
    # pattern_string = event.pattern_match.string
    try:
        query_string = event.pattern_match.string.split(" ", 1)[1] or ""
        logger.info(f"query string to search {query_string}")
        query_params = query_string.replace(" ", "+")
        logger.info(f"Query params {query_params}")
        res = requests.get('https://www.google.com/search',  {"q": query_params}, headers=USER_AGENT)
        soup = BeautifulSoup(res.text, 'html.parser')
    except Exception as e:
        logger.exception(f"Error while fetching records {e}")
        return
    # first try to find div tag with attribute data-tts and data-tts-text
    try:
        tts_text = soup.findAll("div", {"data-tts" : True, "data-tts-text" : True})
        logger.info(f"it's a tts_text match {tts_text}")
        # there should be only one element present:
        try:
            msg = tts_text[0].text
            logger.info(f"found record with attribute type tts_text {msg}")
            await event.respond(msg)
            return # don't execute this method further
        except IndexError as e:
            logger.error(f"index error occurred {e}")
            pass
        logger.info("tts_text match FAILED")
        # that means try another method:
        attr_kc_text = soup.findAll("div", {"data-attrid" : re.compile(r"^kc:/\w+/\w+:\w+")})
        # if there's any such tag
        if attr_kc_text:
            logger.info("it's attr_kc_text match")
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
            # print(rso)
            attribute = card[0].get('aria-label')
            if attribute is None:
                # it's a time realted card
                time = card[0].findChild().text
                logger.info(f"found record as time card {time}")
                await event.respond(time)
                return
            elif attribute == "Currency exchange rate converter":
                logger.info("it's a currency card")
                parent = soup.find(id="knowledge-currency__updatable-data-column") # Hopefully they won't change ID
                currency = parent.findChild().text
                _ = currency.split('equals')
                # print(currency, _)
                hacked_text = f"{_[0]} equals {_[1]}"   # ugly hack because some smartass in google did not put space after 'equals' word
                logger.info(f"currency conversion should be {currency}")
                await event.respond(hacked_text)
        except Exception as e:
            # print(e.with_traceback())
            logger.exception(e)
            pass
        # it's not a time card either
    except Exception as e:
        logger.info(f"Final exception {e}")
        await event.respond("can't find anything on that, please report this query to Spark")
