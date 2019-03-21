from telethon import TelegramClient, events
import os


import logging
from telethon import TelegramClient, events
import time
import os
from dotenv import load_dotenv

logging.basicConfig(
    filename="logs/grambot.log",
    filemode='a',
    datefmt='%H:%M:%S',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

load_dotenv()

logger = logging.getLogger(__name__)

api_id = os.environ['apiid']
api_hash = os.environ['apihash']

bot = TelegramClient('tguserbot', api_id, api_hash)
