from userbot import bot, logger
from telethon import TelegramClient, events
from config import server
import subprocess


allowed_commands = [
    'ls',
    'ls -l',
    'cd',
    'mkdir',
]

@bot.on(events.NewMessage(**server))
async def serverfn(event):
    logger.info("server plugin called")    
    pattern_string = event.pattern_match.string
    command = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    logger.info(f"command to execute - {command}")
    parametrize = command.split(" ")
    pipe = subprocess.check_output(parametrize, stderr=subprocess.PIPE)
    message = pipe.decode('utf-8')
    if command in allowed_commands:
        logger.info("command is in allowed_commands")
        await event.respond(f"```{message}```")