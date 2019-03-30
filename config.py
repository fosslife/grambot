from os import environ
import re
env = environ.get('allowed_chats').split(" ")
chats = list(map(int, env))

weather = {
    "pattern": "\.weather",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

user = {
    "pattern": "\.user",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

quote = {
    "pattern": "\.quote",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

help = {
    "pattern": "\.help",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

die = {
    "pattern": "\.die",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

meme = {
    "pattern": "\.meme",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

ids = {
    "pattern": "\.id",
    "incoming": False,
    "outgoing": True,
}

tag = {
    "pattern": r"(.*)\[([^\]]+)\]\(([^)]+)\)(.*)",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

myname = {
    "pattern": re.compile(r".*(spark|sparkenstein|sprk|prabhanjan|prabhu)", re.IGNORECASE),
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

waiting = {
    "pattern": "\.wait",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

google = {
    "pattern": "\.google",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

server = {
    "pattern": "\.exec",
    "incoming": False,
    "outgoing": True,
    "chats": 'me'
}

messages = {
    "pattern": "\.say",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

cleanup = {
    "pattern": "\.clean",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

omni = {
    "pattern": "\.omni",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}