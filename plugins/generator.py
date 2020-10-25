from userbot import bot, logger
from telethon import TelegramClient, events
from telethon.tl import types
from config import generator
from bs4 import BeautifulSoup
import requests
from random import randint
import urllib
from random import random

urls = {
    "word": "https://www.thisworddoesnotexist.com/",
    "waifu": "https://www.thiswaifudoesnotexist.net/",
    "art": "https://thisartworkdoesnotexist.com/",
    "cat": "https://thiscatdoesnotexist.com/",
    "person": "https://thispersondoesnotexist.com/image",
    "lyrics": "https://theselyricsdonotexist.com/generate.php",
}


@bot.on(events.NewMessage(**generator))
async def generate(event):
    logger.info("generator plugin called")
    category = event.pattern_match.string.split(" ")[1]
    if not category:
        logger.info("No category found to generate")
        return
    url = urls[category]
    if category == "word":
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        word = soup.find(id="definition-word").text
        definition = soup.find(id="definition-definition").text
        example = soup.find(id="definition-example").text
        await event.respond(f"""**{word}**\n{definition}\n\n__{example}__""", parse_mode="md")
    elif category == "waifu":
        fullurl = f"""{url}example-{randint(1, 99999)}.jpg"""
        await event.respond(file=fullurl)
    elif category == "art":
        fullurl = f"""{url}?random={random()}"""
        try:
            await event.respond(file=types.InputMediaPhotoExternal(fullurl))
        except Exception as ex:
            print("Error Occurred", ex)
            await event.respond("Error")
    elif category == "cat":
        fullurl = f"{url}?random={random()}"
        await event.respond(file=types.InputMediaPhotoExternal(fullurl))
    elif category == "person":
        fullurl = f"{url}?random={random()}"
        await event.respond(file=types.InputMediaPhotoExternal(fullurl))
    # Doesn't work
    # elif category == "lyrics":
    #     # print(event.pattern_match.string)
    #     try:
    #         mood = event.pattern_match.string.split(" ")[2]
    #         genre = event.pattern_match.string.split(" ")[3]
    #         message = event.pattern_match.string.split(" ")[4]
    #         res = requests.post(url, data={"lyricMood": mood, "lyricsGenre": genre, "message": message}, headers={
    #                             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    #                             "Origin": "https://theselyricsdonotexist.com"})
    #         print(res)
    #         await event.respond("Done")
    #     except Exception as ex:
    #         print("Error Occurred", ex)
    #         await event.respond("Error")
    else:
        await event.respond("Cannot generate selected entity")
