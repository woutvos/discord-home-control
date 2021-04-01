import discord
from discord.ext import commands

class NetworkScan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(NetworkScan(bot))