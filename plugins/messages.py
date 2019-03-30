from userbot import bot, logger
from telethon import TelegramClient, events
from config import messages

messages_mapper = {
    'todo': '✅ Added to TODO!',
    'riir': 'RIIR'
}

@bot.on(events.NewMessage(**messages))
async def messagesfns(event):
    logger.info("called messages plugin")
    pattern_string = event.pattern_match.string
    message = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    logger.info(f"message to send {message}")
    await event.respond(messages_mapper[message])
