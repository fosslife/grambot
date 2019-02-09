from telethon import TelegramClient, events
import os

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

# reply only if the incoming message is from @abcd
@client.on(events.NewMessage(chats=('abcd')))
async def fromsecondaccound(event):
    if 'fp' in event.raw_text:
        await event.respond('Functional Programming')    

# client.send_message('Sparkenstein', 'Hello World from sparks userbot')

client.start()
client.run_until_disconnected()