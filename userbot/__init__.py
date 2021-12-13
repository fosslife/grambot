from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import sys

import logging
from logging import StreamHandler, log
from logging.handlers import RotatingFileHandler
from telethon import TelegramClient, events
import time
from dotenv import load_dotenv


load_dotenv(".env")


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

STRING_SESSION = os.environ.get("string_session_key", None)

if STRING_SESSION:
    handler = StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

else:
    LOG_FILENAME = "logs/grambot.log"
    if not os.path.exists("logs"):
        os.mkdir("logs")

        needRoll = os.path.isfile(LOG_FILENAME)

        handler = RotatingFileHandler(LOG_FILENAME, backupCount=10)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if needRoll:
            logger.handlers[0].doRollover()


api_id = os.environ["apiid"]
api_hash = os.environ["apihash"]


if STRING_SESSION:
    logger.info("String session exists")
    bot = TelegramClient(StringSession(STRING_SESSION), api_id, api_hash)
else:
    logger.info("String session does not exists")
    bot = TelegramClient("tguserbot", api_id, api_hash)
