from userbot import bot
from plugins import All_PLUGINS
import importlib
from userbot import logger


for plugin in All_PLUGINS:
    logger.info("importing " + plugin)
    importlib.import_module("plugins." + plugin)

logger.info("All plugins loaded, starting bot")

bot.start()
logger.info("bot started")

bot.run_until_disconnected()