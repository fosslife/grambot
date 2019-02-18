from userbot import bot
from telethon import TelegramClient, events
from plugins import All_PLUGINS

@bot.on(events.NewMessage(pattern='.help()'))
async def help(event):
    print(All_PLUGINS)
    loaded_modules = ""
    for modulename in All_PLUGINS:
        loaded_modules += "." + modulename + "()\n"
    await event.respond(loaded_modules)