from userbot import bot, logger
from telethon import TelegramClient, events
from config import cleanup

@bot.on(events.NewMessage(**cleanup))
async def clean(event):
    logger.info("cleanup plugin called")
    pattern_string = event.pattern_match.string
    limit = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    id = await event.get_input_chat()
    from_user = 'me'
    logger.info(f"deleting {limit} messages from {id}")
    m = await bot.get_messages(id, limit=int(limit))
    await bot.delete_messages(id, m)
    await event.respond("cleanup done")
