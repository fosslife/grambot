from userbot import bot
from telethon import TelegramClient, events
from time import sleep

@bot.on(events.NewMessage(pattern='.anim()'))
async def anim(event):
    pattern_string = event.pattern_match.string
    animes = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    lst = animes.split(",")
    before = lst[0].strip()
    after = lst[1].strip()
    for i in range(0, 2):
        await event.edit(before)
        sleep(0.5)
        await event.edit(after)
        sleep(0.5)