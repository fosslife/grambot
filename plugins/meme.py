from userbot import bot
from telethon import TelegramClient, events
from config import meme

images_dir = "./plugins/data/images/"

file_path_mapping = {
    "help": "./plugins/data/memes",
    "pys": images_dir + "played_yourself.gif",
    "nou": images_dir + "nou.jpg",
    "ret": images_dir + "retarded.jpg",
    "moc": images_dir + "moc.jpg",
    "hoe": images_dir + "hoe.jpg",
    "sgh": images_dir + "get_some_help.gif",
}

@bot.on(events.NewMessage(**meme))
async def memes(event):
    await event.delete()
    pattern_string = event.pattern_match.string
    meme_name = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    file_to_send = file_path_mapping.get(meme_name)
    if meme_name=="help":
        await event.respond(open(file_to_send).read(), reply_to=event.reply_to_msg_id)
    else:
        try:
            await event.respond("", reply_to=event.reply_to_msg_id, file=file_to_send)
        except Exception:
            await event.respond("No U")
