from userbot import bot
from telethon import TelegramClient, events
from config import tag

@bot.on(events.NewMessage(**tag))
async def tag(event):
    await event.delete()
    pattern_string = event.pattern_match.string
    params = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    as_user, orig_user = params.split(",")
    print(as_user, orig_user)
    await event.respond(f"[{as_user}](http://t.me/{orig_user})", reply_to=event.reply_to_msg_id)