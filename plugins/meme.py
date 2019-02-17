from userbot import bot
from telethon import TelegramClient, events
from time import sleep

@bot.on(events.NewMessage(pattern='.e()'))
async def e(event):
    for i in range(0, 6):
        await event.edit("👉👌")
        sleep(0.5)
        await event.edit("👉  👌")
        sleep(0.5)
        print(i)