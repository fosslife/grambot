from userbot import bot, logger
from telethon import TelegramClient, events
from config import dad

@bot.on(events.NewMessage(**dad))
async def dad(event):
    logger.info("dad plugin is called")
    user = event.pattern_match.group(2)
    await event.respond(f"Hi {user}, I am spark")
