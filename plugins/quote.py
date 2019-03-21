import requests
from userbot import bot, logger
from telethon import TelegramClient, events
from config import quote

@bot.on(events.NewMessage(**quote))
async def sendQute(event):
    logger.info("quotes plugin called")
    quotes_api_url = "https://opinionated-quotes-api.gigalixirapp.com/v1/quotes"
    data = requests.get(quotes_api_url).json()
    quote = data['quotes'][0]['quote']
    author = data['quotes'][0]['author']
    await event.reply(f'`{quote}`\n                       - __{author}__')
