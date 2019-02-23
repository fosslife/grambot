from userbot import bot
from telethon import TelegramClient, events
from config import tag

@bot.on(events.NewMessage(**tag))
async def tag(event):
    await event.delete()
    pattern_string = event.pattern_match.string
    params = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    as_user, orig_user = params.split(",")
    msg = f"<a href='http://t.me/{orig_user.strip()}/'>{as_user.strip()}</a>"
    await event.respond(msg, reply_to=event.reply_to_msg_id, parse_mode="HTML")