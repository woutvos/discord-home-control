import discord
from discord.ext import commands
from wakeonlan import send_magic_packet

class Wol(commands.Cog):
    def __init__(self, client):
        self.client = client

# Wol_send
    @commands.command(
        name="Wol_send",
        description="Send a WOL signal to the target.",
        brief="Send a WOL signal"
        )
    async def wol_send(self, ctx):
        await ctx.send("What is the mac addres of the victim?")
        msg = await self.client.wait_for('message',)
        send_magic_packet(msg.content, port=4343)
        await ctx.send(f"Send a magic packet to {msg.content}.")

def setup(client):
    client.add_cog(Wol(client))