from userbot import bot
from telethon import TelegramClient, events
from config import commands

@bot.on(events.NewMessage(pattern=commands["help"]))
async def help(event):
    commands = open("./plugins/data/commands").read()
    await event.respond(commands)