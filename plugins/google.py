from userbot import bot
from telethon import TelegramClient, events
from config import google
from bs4 import BeautifulSoup
import requests
import re

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

@bot.on(events.NewMessage(**google))
async def google(event):
    pattern_string = event.pattern_match.string
    query_string = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    query_params = query_string.replace(" ", "+")
    res = requests.get('https://www.google.com/search',  {"q": query_params}, headers=USER_AGENT)
    soup = BeautifulSoup(res.text, 'html.parser')
    # first try to find div tag with attribute data-tts and data-tts-text
    tts_text = soup.findAll("div", {"data-tts" : True, "data-tts-text" : True})
    # there should be only one element present:
    try:
        msg = tts_text[0].text
        await event.respond(msg)
        return # don't execute this method further
    except IndexError as e:
        pass
    # that means try another method:
    attr_kc_text = soup.findAll("div", {"data-attrid" : re.compile(r"^kc:/[a-z]+/[a-z_]+:[a-z]+")})
    print(attr_kc_text)
    # it's probably in the second child of div tag with this attribute:   
    msg = attr_kc_text[0].findChild().findChild().text
    await event.respond(msg)