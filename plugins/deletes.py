from userbot import bot
from telethon import TelegramClient, events


# @bot.on(events.MessageDeleted())
async def delted(event):
    try:
        id = event.original_update.channel_id
    except Exception:
        id = None
    await bot.send_message('me', 'someone deleted something')