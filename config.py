from os import environ
import re
chats = list(map(int, environ.get('allowed_chats').split(" ")))
aliases = environ.get('my_name_aliases').replace(" ", "|")

cleanup = {
    "pattern": "\.clean",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

dad = {
    "pattern": re.compile(r".*(I\'m\ *|i am\ )(.*)", re.IGNORECASE),
    "incoming": True,
    "outgoing": False,
    "chats": chats
}

die = {
    "pattern": "\.die",
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

groupinfo = {
    "pattern": "\.id",
    "incoming": False,
    "outgoing": True,
}

help = {
    "pattern": "\.help",
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

messages = {
    "pattern": "\.say",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

myname = {
    "pattern": re.compile(r".*("+aliases+")", re.IGNORECASE),
    "incoming": True,
    "outgoing": True,
    # "chats": chats
}

omni = {
    "pattern": "\.omni",
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

server = {
    "pattern": "\.exec",
    "incoming": False,
    "outgoing": True,
    "chats": 'me'
}

tag = {
    "pattern": r"(.*)\[([^\]]+)\]\(([^)]+)\)(.*)",
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
waiting = {
    "pattern": "\.wait",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}

weather = {
    "pattern": "\.weather",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}
