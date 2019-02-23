from userbot import bot
from telethon import TelegramClient, events
from time import sleep
import re

# both regex and parse() Coutesy of @ceda_ei
reg = r"^\.anim\((?P<q>\"|')?(?(q)((?:(?!(?P=q)).)+)(?P=q)|([^,)]+)),\s*(?P<r>\"|')?(?(r)((?:(?!(?P=r)).)+)(?P=r)|([^,)]+))\)$"
compiled = re.compile(reg)

def parse(text):
    x = compiled
    match = x.match(text)
    if match:
        if match.group(2):
            first_param = match.group(2)
        else:
            first_param = match.group(3)
        if match.group(5):
            second_param = match.group(5)
        else:
            second_param = match.group(6)
        return (first_param, second_param)
    return None

@bot.on(events.NewMessage(pattern=compiled, chats=(-1001335202320, 1377536264), incoming=False, outgoing=True))
async def anim(event):
    matched = parse(event.pattern_match.string)
    before = matched[0]
    after = matched[1]
    if before and after:
        try:
            reply_to_user = event.message.to_id.user_id
        except AttributeError:
            reply_to_user = event.message.to_id.channel_id
        sent = await event.respond(after, reply_to=event.reply_to_msg_id)
        for i in range(0, 2):
            await bot.edit_message(reply_to_user, sent.id, before)
            sleep(0.5)
            await bot.edit_message(reply_to_user, sent.id, after)
            sleep(0.5)
