from telethon import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv
import os

load_dotenv(".env")

api_id = os.environ["apiid"]
api_hash = os.environ["apihash"]

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("your session string is:")
    print(client.session.save())
