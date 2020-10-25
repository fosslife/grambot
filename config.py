from os import environ
import re
chats = list(map(int, environ.get('allowed_chats').split(" ")))
aliases = environ.get('my_name_aliases').replace(" ", "|")

async def namefilter(x):
    return not await x.client.is_bot()

cleanup = {
    "pattern": r"\.clean",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}

die = {
    "pattern": r"\.die",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}


generator = {
    "pattern": r"\.generate",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}


google = {
    "pattern": r"\.google",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}

groupinfo = {
    "pattern": r"\.id",
    "incoming": False,
    "outgoing": True,
}

help = {
    "pattern": r"\.help",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}


meme = {
    "pattern": r"\.meme",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}

messages = {
    "pattern": r"\.say",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}

myname = {
    "pattern": re.compile(r".*("+aliases+")", re.IGNORECASE),
    "incoming": True,
    "outgoing": False,
    "func": namefilter
    # "chats": chats
}

omni = {
    "pattern": r"\.omni",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}

quote = {
    "pattern": r"\.quote",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}

server = {
    "pattern": r"\.exec",
    "incoming": False,
    "outgoing": True,
    "chats": 'me'
}

tag = {
    "pattern": r"(.*)\[([^\]]+)\]\(([^)]+)\)(.*)",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}

user = {
    "pattern": r"\.user",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}
waiting = {
    "pattern": r"\.wait",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}

wall = {
    "pattern": r"\.wall",
    "incoming": False,
    "outgoing": True,
}

weather = {
    "pattern": r"\.weather",
    "incoming": False,
    "outgoing": True,
    # "chats": chats
}
