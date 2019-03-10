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
    header = soup.findAll('div', {"role": "heading"})[1]
    msg = header.findChild().text
    # print(children)
    # text = children[1].text
    await event.respond(msg)