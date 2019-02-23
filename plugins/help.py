from userbot import bot
from telethon import TelegramClient, events
from config import help

@bot.on(events.NewMessage(**help))
async def help(event):
    commands = open("./plugins/data/commands").read()
    await event.respond(commands)