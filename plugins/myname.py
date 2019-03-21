from userbot import bot, logger
from telethon import TelegramClient, events
from config import myname
from os import environ
from datetime import datetime

@bot.on(events.NewMessage(**myname))
async def myname(event):
    logger.info("myname plugin is called")
    if event.is_group:
        users = environ.get("my_name_aliases", "").split(' ')
        logger.info(f"my name aliases are {users}")
        logger.info(f"incoming message is {event.raw_text.lower()}")
        present = [x for x in users if x.lower() in event.raw_text.lower()]
        if present:
            logger.info(f"your name present in incoming message, forwarding it to saved message")
            group_id = event.message.to_id.channel_id
            await bot.forward_messages('me', event.message.id, group_id)