from os import environ

env = environ.get('allowed_chats').split(" ")
chats = list(map(int, env))

weather = {
    "pattern": "\.weather",
    "incoming": True,
    "outgoing": True,
    "chats": chats
}

user = {
    "pattern": "\.user",
    "incoming": True,
    "outgoing": True,
    "chats": chats
}

quote = {
    "pattern": "\.quote",
    "incoming": True,
    "outgoing": True,
    "chats": chats
}

help = {
    "pattern": "\.help",
    "incoming": True,
    "outgoing": True,
    "chats": chats
}

die = {
    "pattern": "\.die",
    "incoming": True,
    "outgoing": True,
    "chats": chats
}

meme = {
    "pattern": "\.meme",
    "incoming": True,
    "outgoing": True,
    "chats": chats
}

id = {
    "pattern": "\.id",
    "incoming": False,
    "outgoing": True,
}

tag = {
    "pattern": "\.tag",
    "incoming": False,
    "outgoing": True,
    "chats": chats
}