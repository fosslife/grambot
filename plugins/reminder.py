from userbot import bot, logger
from telethon import TelegramClient, events
from config import reminder
from datetime import timedelta

def get_expiry(timestr: str):
    timeFactor = timestr.split(" ")[1]
    time = int(timestr.split(" ")[0])

    multipliers = {
        "sec": lambda t: t,
        "seconds": lambda t: t,
        "min": lambda t: t * 60,
        "minutes": lambda t: t * 60,
        "hour": lambda t: t * 3600,
        "hours": lambda t: t * 3600,
        "day": lambda t: t * 86400,
        "days": lambda t: t * 86400,
        "week": lambda t: t * 604800,
        "weeks": lambda t: t * 604800,
        "month": lambda t: t * 2.628e6,
        "months": lambda t: t * 2.628e6,
    }
    return multipliers.get(timeFactor)(time)


@bot.on(events.NewMessage(**reminder))
async def reminder(event):
    logger.info("reminder plugin called")
    groups = event.pattern_match
    task = groups.group(3)
    time = groups.group(5)
    duration = groups.group(4)
    unit = groups.group(6)
    fromid = await event.get_sender()
    timestr = f"{time} {unit}"
    expiry_second = get_expiry(timestr)
    logger.info("task=%s time=%s duration=%s unit=%s", task, time, duration, unit)
    await event.respond(f"Ok! will remind you to {task} {duration} {time} {unit}")
    await event.respond(
            f"@{fromid.username} reminding you to {task}",
            schedule=timedelta(seconds=expiry_second),
        )