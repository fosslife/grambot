from telethon import TelegramClient, events
import os

import logging
from logging.handlers import RotatingFileHandler
from telethon import TelegramClient, events
import time
import os
from dotenv import load_dotenv

LOG_FILENAME = 'logs/grambot.log'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

needRoll = os.path.isfile(LOG_FILENAME)

handler = RotatingFileHandler(LOG_FILENAME, backupCount=10)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
handler.setFormatter(formatter)
logger.addHandler(handler)
load_dotenv()


if needRoll:    
    logger.handlers[0].doRollover()


api_id = os.environ['apiid']
api_hash = os.environ['apihash']

bot = TelegramClient('tguserbot', api_id, api_hash)
