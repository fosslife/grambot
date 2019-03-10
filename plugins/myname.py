from userbot import bot
from telethon import TelegramClient, events
from config import myname
from os import environ
from datetime import datetime

@bot.on(events.NewMessage(**myname))
async def myname(event):
    if event.is_group:
        users = environ.get("my_name_aliases", "").split(' ')
        present = [x for x in users if x.lower() in event.raw_text.lower()]
        if present:
            group_id = event.message.to_id.channel_id
            await bot.forward_messages('me', event.message.id, group_id)