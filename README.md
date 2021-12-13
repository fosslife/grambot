# Grambot

## What is it

It's a telegram userbot. if you don't know what a userbot is, it's a normal user account but backed by the power of programming. Think it like, a programming language is handling your account and that's all. It knows when someone sends you a message, what is the message, if you want to send something to someone etc etc. Thus, automation!

## How does it work?

This bot is written in Python, with a famous telegram MTProto framework known as [Telethon](https://github.com/LonamiWebs/Telethon). With the help of Telethon, we can keep the server in `listening` mode for events such as New Incoming message etc etc and then for a specific type of message, take a specific action.

## Deploy

<p style="text-align: left;"><a href="https://heroku.com/deploy"> <img style="float: left;" src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" /></a></p>

> Note that heroku deploys the bot successfully, but somehow doesn't start the bot automatically. I am not good
> with heroku. if someone knows the issue feel free to open PR. otherwise, for now, once bot is deployed with above
> button, go to following section from heroku dashboard, and toggle it to turn dyno on.

![heroku](./heroku.png)

to get the `string_session` key, just clone the repo, get apiid and apikey from telegram (see steps below), paste them in .env file.
then run `stringsession.py` it will output the key for you, paste it in heroku deploy dashboard you see after you click above button.

to check logs:

```
heroku logs -a heroku-app-id --tail
```

it's always a good idea to connect heroku with repository, so just fork the repo and connect it with github, for manual deploys

## Example

[See full list [Here](./Plugins.md)]

for this bot I have enabled `commands` such as `.help` and `.weather`.
When the bot encounters a new message on telegram that matches exact `.weather` i.e start from `(dot)(weather)`, it executes a special coroutine that fetches weather from open weather API of given city. thus

```
.weather(Berlin) => weather details of berlin
.help => help message on how to use other commands
```

These output are sent to the same channel the command was sent on, by YOUR account.

[![Demo](https://img.youtube.com/vi/wybDkn1q3mA/0.jpg)](https://www.youtube.com/watch?v=wybDkn1q3mA)

## Installation:

- Pull the latest source. Clone the repo or download zip and extract it, whatever works for you
- get apiid and apihash from telegram (free). [Instructions](https://core.telegram.org/api/obtaining_api_id)
- get openweather api key (free). [Instructions](https://openweathermap.org/appid)
- rename `sample.env` to `.env` at the root of folder. and edit it accordingly
- if you have pipenv installed
  - run `pipenv shell`
  - run `pipenv install`
  - run `python3 -m userbot`
  - it should start the bot.
- if you don't have pipenv
  - use virtualenv if possible
  - run `pip install -r requirements.txt`
  - run `python3 -m userbot`

if you face any issues contact me on Telegram or feel free to open issue :D

## License

grambot is licensed under MIT. Please see LICENSE file for more information
