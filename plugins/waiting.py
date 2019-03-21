from userbot import bot, logger
from telethon import TelegramClient, events
from config import waiting
from asyncio import sleep

async def animated_response(event):
    await event.delete()
    sent_message = await event.respond("<code>waiting</code>", parse_mode="html")
    try:
        reply_to_user = event.message.to_id.user_id
    except AttributeError:
        reply_to_user = event.message.to_id.channel_id
    for i in range(0, 2):
        for j in range(0, 6):
            await sleep(0.4)
            await bot.edit_message(reply_to_user,  sent_message.id, f"```waiting{'.'*j}```")

@bot.on(events.NewMessage(**waiting))
async def myname(event):
    logger.info("waiting plugin called")
    await animated_response(event)