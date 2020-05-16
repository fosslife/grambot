from userbot import bot, logger
from telethon import TelegramClient, events
from config import generator
from bs4 import BeautifulSoup
import requests


urls = {
    "word": "https://www.thisworddoesnotexist.com/"
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