from userbot import bot, logger
from telethon import TelegramClient, events
from config import myname
from os import environ
from datetime import datetime

@bot.on(events.NewMessage(**myname))
async def mynamefn(event):
    logger.info("myname plugin is called")
    if event.is_group:
        logger.info(f"incoming message is {event.raw_text.lower()}")
        group_id = event.message.to_id.channel_id
        await bot.forward_messages('me', event.message.id, group_id)