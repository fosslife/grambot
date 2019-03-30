from userbot import bot, logger
from telethon import TelegramClient, events
from config import help

@bot.on(events.NewMessage(**help))
async def helpfn(event):
    logger.info("help plugin called")
    commands = open("./plugins/data/commands").read()
    await event.respond(commands)