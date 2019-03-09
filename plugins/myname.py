from userbot import bot
from telethon import TelegramClient, events
from config import myname
from os import environ
from datetime import datetime

@bot.on(events.NewMessage(**myname))
async def myname(event):
    if event.is_group:
        users = environ.get("my_name_aliases", "").split(' ')
        present = [x for x in users if x.lower() in event.raw_text.lower()]
        if present:
            group_id = event.message.to_id.channel_id
            group_entity = await bot.get_entity(group_id)
            group_title = group_entity.username
            link = "["+group_entity.title+"](http://t.me/"+group_title + ")" if group_title else group_entity.title
            print(link)
            # get user
            from_id = event.message.from_id
            user_entity = await bot.get_entity(from_id)
            current_time = datetime.now().strftime("%d-%B-%Y at %H:%M")
            message = f"{user_entity.username} from {link} group said something about you on {current_time}\nThe text was:\n{event.raw_text}"
            await bot.send_message('me', message=message, link_preview=False)