from userbot import bot
from telethon import TelegramClient, events

@bot.on(events.NewMessage(pattern='\.help'))
async def help(event):
    commands = open("./plugins/data/commands").read()
    await event.respond(commands)