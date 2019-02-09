from telethon import TelegramClient, events
import os
import requests

api_id = os.environ['apiid']
api_hash = os.environ['apihash']

client = TelegramClient('tguserbot', api_id, api_hash)
print('client started')

# Reply to any message from any chat
# If it contains 'hello'
@client.on(events.NewMessage)
async def messagelistener(event):
    if 'hello' in event.raw_text:
        # Can use .reply('Sup') if want to reply as `reply`
        await event.respond('Sup')

# reply only if the incoming message is from @Sparkenstein
@client.on(events.NewMessage(chats=('Sparkenstein')))
async def fromsecondaccound(event):
    if 'fp' in event.raw_text:
        await event.respond('Functional Programming')

# Similarly, you can use incoming=True for messages that you receive
@client.on(events.NewMessage(pattern='quote()'))
async def sendQute(event):
    quotes_api_url = "https://opinionated-quotes-api.gigalixirapp.com/v1/quotes"
    data = requests.get(quotes_api_url).json()
    quote = data['quotes'][0]['quote']
    author = data['quotes'][0]['author']
    await event.reply(f'`{quote}`\n                       - __{author}__')

# client.send_message('Sparkenstein', 'Hello World from sparks userbot')

client.start()
client.run_until_disconnected()