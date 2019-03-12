from userbot import bot
from telethon import TelegramClient, events
from config import messages

messages_mapper = {
    'todo': '✅ Added to TODO!',
    'riir': 'RIIR'
}

@bot.on(events.NewMessage(**messages))
async def messages(event):
    pattern_string = event.pattern_match.string
    message = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    await event.respond(messages_mapper[message])
