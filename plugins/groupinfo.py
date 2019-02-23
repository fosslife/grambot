from userbot import bot
from telethon import TelegramClient, events
from config import id


@bot.on(events.NewMessage(**id))
async def id(event):
    try:
        id = event.message.to_id.channel_id
        await event.respond(f"groupid - {id}")
    except AttributeError:
        id = event.message.to_id.user_id
        await event.respond(f"userid - {id}")
