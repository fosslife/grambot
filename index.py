from telethon import TelegramClient, events
import os
import requests

api_id = os.environ['apiid']
api_hash = os.environ['apihash']

client = TelegramClient('tguserbot', api_id, api_hash)
print('client started')

# Similarly, you can use incoming=True for messages that you receive
@client.on(events.NewMessage(pattern='.quote()'))
async def sendQute(event):
    print(event)
    quotes_api_url = "https://opinionated-quotes-api.gigalixirapp.com/v1/quotes"
    data = requests.get(quotes_api_url).json()
    quote = data['quotes'][0]['quote']
    author = data['quotes'][0]['author']
    await event.reply(f'`{quote}`\n                       - __{author}__')


client.start()
client.run_until_disconnected()