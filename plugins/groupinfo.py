from userbot import bot, logger
from telethon import TelegramClient, events
from config import id


@bot.on(events.NewMessage(**id))
async def id(event):
    logger.info("group info plugin called")
    try:
        id = event.message.to_id.channel_id
        logger.info(f"sending group id - {id}")
        await event.respond(f"groupid - {id}")
    except AttributeError:
        id = event.message.to_id.user_id
        logger.info("sending user id - {id}")
        await event.respond(f"userid - {id}")
