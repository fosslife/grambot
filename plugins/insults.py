from random import choice
from userbot import bot
from telethon import TelegramClient, events

@bot.on(events.NewMessage(pattern='.die()'))
async def insult(event):
    await event.delete()
    pattern_string = event.pattern_match.string
    entity = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    file = open("./plugins/data/insults").read().split("\n")
    insult = choice(file)
    # print(event.message.to_id.stringify())
    try:
        reply_to_user = event.message.to_id.user_id
    except AttributeError:
        reply_to_user = event.message.to_id.channel_id
    reply_to_message = event.message.reply_to_msg_id
    if reply_to_message:
        await bot.send_message(reply_to_user, message=insult, reply_to=reply_to_message)
    else:
        await bot.send_message(reply_to_user, message=insult)

    # await event.respond(insult)