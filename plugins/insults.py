from random import choice
from userbot import bot
from telethon import TelegramClient, events
from os import getcwd
from telethon.client.messages import MessageMethods

@bot.on(events.NewMessage(pattern='.die()'))
async def insult(event):
    pattern_string = event.pattern_match.string
    entity = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    file = open("./plugins/data/insults").read().split("\n")
    insult = choice(file)
    # print(dir(event.message.to_id))
    reply_to_user = event.message.to_id.channel_id or event.message.to_id.user_id
    reply_to_message = event.message.reply_to_msg_id
    print("Replying to ", reply_to_user, reply_to_message)

    await event.delete()
    await event.respond(insult)