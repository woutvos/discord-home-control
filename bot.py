from configparser import ConfigParser
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv
import logging
import os

# Logging
config_object = ConfigParser()
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Load and specify some things
load_dotenv()
bot=commands.Bot(command_prefix="!", case_insensitive=True)
slash = SlashCommand(bot, override_type = True)
TOKEN = os.getenv("DISCORD_TOKEN")

# Loading al the cogs
if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)