from telethon import TelegramClient, events
import os

api_id = os.environ['apiid']
api_hash = os.environ['apihash']

client = TelegramClient('tguserbot', api_id, api_hash)
print('client started')


@client.on(events.NewMessage)
async def messagelistener(event):
    if 'hello' in event.raw_text:
        # Can use .reply('Sup') if want to reply as `reply`
        await event.respond('Sup')


# client.send_message('Sparkenstein', 'Hello World from sparks userbot')

client.start()
client.run_until_disconnected()