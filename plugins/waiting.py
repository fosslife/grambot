from userbot import bot
from telethon import TelegramClient, events
from config import waiting
from imgurpython import ImgurClient
from asyncio import sleep


def picture_response():
    "picture waiting"

async def animated_response(event):
    sent_message = await event.respond("```waiting```")
    await event.delete()
    try:
        reply_to_user = event.message.to_id.user_id
    except AttributeError:
        reply_to_user = event.message.to_id.channel_id
    for i in range(0, 2):
        await sleep(0.4)
        await bot.edit_message(reply_to_user,  sent_message.id, "```waiting.```")
        await sleep(0.4)
        await bot.edit_message(reply_to_user, sent_message.id, "```waiting..```")
        await sleep(0.4)
        await bot.edit_message(reply_to_user, sent_message.id, "```waiting...```")
        await sleep(0.4)
        await bot.edit_message(reply_to_user, sent_message.id, "```waiting....```")
        await sleep(0.4)
        await bot.edit_message(reply_to_user, sent_message.id, "```waiting.....```")

@bot.on(events.NewMessage(**waiting))
async def myname(event):
    pattern_string = event.pattern_match.string
    type_of_reply = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    if type_of_reply == "card":
        await picture_response()
    elif type_of_reply == "text":
        await animated_response(event)