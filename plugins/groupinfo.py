from userbot import bot
from telethon import TelegramClient, events
from config import group


@bot.on(events.NewMessage(**group))
async def group(event):
    try:
        id = event.message.to_id.channel_id
        await event.respond(f"groupid - {id}")
    except AttributeError:
        await event.respond("This doesn't look like a group")
