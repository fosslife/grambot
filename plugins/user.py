from userbot import bot
from telethon import TelegramClient, events
from config import user
from telethon.tl.functions.users import GetFullUserRequest

@bot.on(events.NewMessage(**user))
async def getUser(event):
    pattern_string = event.pattern_match.string
    entity = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    try:
        info = await bot(GetFullUserRequest(entity))
        await event.respond(f"""
Username - `{info.user.username}`
{"User is a bot" if info.user.bot else "user is not a bot"}
{"User is restricted for " + info.user.restriction_reason  if info.user.restricted else "User is not restricted"}
Name - {info.user.first_name} {info.user.last_name if info.user.last_name else ""}
Status - `{info.about}`
id - {info.user.id}
{info.common_chats_count} groups common with me
{"I have blocked this user" if info.blocked else "I have not blocked this user"}

""")
    except Exception:
        await event.respond(f"Cannot find entity with `{entity}`")