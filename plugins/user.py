from userbot import bot
from telethon import TelegramClient, events
from config import user

@bot.on(events.NewMessage(**user))
async def getUser(event):
    pattern_string = event.pattern_match.string
    entity = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    try:
        info = await bot.get_entity(entity)
        await event.respond(f"""Username - `{info.username}`
{"User is restricted for " + info.restriction_reason  if info.restricted else "User is not restricted"}
Name - {info.first_name} {info.last_name if info.last_name else ""}
id - {info.id}
""")
    except Exception:
        await event.respond("Cannot find entity with " + entity)