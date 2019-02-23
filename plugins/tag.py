from userbot import bot
from telethon import TelegramClient, events
from config import tag

@bot.on(events.NewMessage(**tag))
async def tag(event):
    await event.delete()
    await event.respond(event.raw_text, reply_to=event.reply_to_msg_id)
