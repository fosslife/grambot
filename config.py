from os import environ
import re

allowed_chats = environ.get("allowed_chats")
blacklist_chats_env = environ.get("blacklist_chats")

if allowed_chats:
    chats = list(map(int, allowed_chats.split(" ")))
else:
    chats = []

# aliases = environ.get("my_name_aliases").replace(" ", "|")
aliases_env = environ.get("my_name_aliases")
if aliases_env:
    aliases = aliases_env.replace(" ", "|")
else:
    aliases = None

if blacklist_chats_env:
    blacklist_chats = list(map(int, blacklist_chats_env.split(" ")))
else:
    blacklist_chats = []


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
    # "pattern": if aliases  re.compile(r".*(" + aliases + ")", re.IGNORECASE) else "",
    "incoming": True,
    "outgoing": False,
    "func": namefilter,
    "blacklist_chats": blacklist_chats
    # "chats": chats
}
if aliases and len(aliases) > 0:
    myname["pattern"] = re.compile(r".*(" + aliases + ")", re.IGNORECASE)

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

reminder = {
    "pattern": r"(.remindme)\s(to)\s(.*)\s(in|after|every)\s(\d+){1,2}\s(sec|seconds|min|minutes|hour|hours|day|days|week|weeks|month|months)",
    "incoming": True,
    "outgoing": True,
    "chats": chats,
}

server = {"pattern": r"\.exec", "incoming": False, "outgoing": True, "chats": "me"}

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
    "incoming": True,
    "outgoing": True,
    # "chats": chats
}
