import discord
from discord.ext import commands
from phue import Bridge
from dotenv import load_dotenv
import os

# Connect to the bridge
load_dotenv()
BRIDGE_IP = os.getenv("BRIDGE_IP")
b = Bridge(BRIDGE_IP)
b.connect()
b.get_api()

class Hue(commands.Cog):
    def __init__(self, client):
        self.client = client

# Hue_toggle
    @commands.command(
        name="Hue_toggle",
        description="Toggle the state of a light or group.",
        brief="Toggle the state of a light or group"
        )
    async def hue_toggle(self, ctx):
        await ctx.send("What do you want to control, a light or group?")

        msg = await self.client.wait_for('message',)

        if msg.content == "light" or msg.content == "Light":
            await ctx.send("What is the name of the light? (for a list of available lights do !hue_get_list)")
            msg = await self.client.wait_for('message',)
            if b.get_light(msg.content, 'on') == True:
                b.set_light(msg.content ,'on', False)
                await ctx.send(f"{msg.content} has been turned off.")
            elif b.get_light(msg.content, 'on') == False:
                b.set_light(msg.content ,'on', True)
                await ctx.send(f"{msg.content} has been turned on.")
                
        elif msg.content == "group" or msg.content == "Group":
            await ctx.send("What is the name of the group? (for a list of available groups do !hue_get_list)")
            msg = await self.client.wait_for('message',)
            if b.get_group(msg.content, 'on') == True:
                b.set_group(msg.content ,'on', False)
                await ctx.send(f"{msg.content} has been turned off.")
            elif b.get_group(msg.content, 'on') == False:
                b.set_group(msg.content ,'on', True)
                await ctx.send(f"{msg.content} has been turned on.")

        else:
            await ctx.send("This isn't a valid option choose between group or light.")

# Hue_get_list
    @commands.command(
        name="Hue_get_list",
        description="Returns a list of the lights or groups connected to your hue bridge.",
        brief="Get a list of groups and lights"
        )
    async def hue_get_list(self, ctx):
        await ctx.send("Where do you want to get a list from, lights or groups?")

        msg = await self.client.wait_for('message',)

        if msg.content == "light" or msg.content == "lights":
            lights = b.lights
            lights_list = ""
            for l in lights:
                lights_list += str(l.name) + "\n"
            await ctx.send(lights_list)

        elif msg.content == "group" or msg.content == "groups":
            groups = b.groups
            groups_list = ""
            for g in groups:
                groups_list += str(g.name) + "\n"
            await ctx.send(groups_list)
        
        else:
            await ctx.send("This isn't a valid option choose between groups or lights.")

def setup(client):
    client.add_cog(Hue(client))