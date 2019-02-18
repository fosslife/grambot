from userbot import bot
from telethon import TelegramClient, events
from plugins import All_PLUGINS

@bot.on(events.NewMessage(pattern='.help()'))
async def help(event):
    commands = open("./plugins/data/commands").read()
    await event.respond(commands)