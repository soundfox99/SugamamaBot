# Title: Sugamama(Bot)
# Custon Bot for the HAIKYUU in COLOR!! discord server.
# Author: TDXPQ (Aditya Jindal)

import sys      #So we can import custom python folders from other folders
sys.path.insert(1, '../Tokens/')

#Import custom python files
from TokenVariables import token
#Import external libraries
import discord
from discord.ext import commands, tasks
#Import Python libraries
import datetime
import asyncio
from pytz import timezone
import pytz
import time

#Define hard coded variables
TOKEN = token
client = commands.Bot(command_prefix = '~')


#Project Code
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Setter and Team Mom'))        #Change status of the bot to online
    print('Bot is ready.')


@client.command()
async def start_clock(ctx, id, zone):
    if time_change.is_running() == True:        #If the bot is running the task restart the task with new parameters instead of starting multiple tasks.
        time_change.restart(zone, int(id))
    else:
        time_change.start(zone, int(id))


@client.command()
async def ping(ctx):
    await ctx.send(f'Nice Receive {round(client.latency * 1000)}ms')


#Define background tasks
@tasks.loop(minutes=10.0)
async def time_change(zone, channel_id):
    tz = pytz.timezone(zone)        #Converts the users time zone preference into a variable usefull for the pytz library.

    current_time = datetime.datetime.utcnow() + tz.utcoffset(datetime.datetime.utcnow())        #Calculates the time in the time zone by adding the offset to the current local time.
    current_time = current_time.strftime('%H:%M:%S')
        
    await client.get_channel(channel_id).edit(name=(zone + ": " + current_time))

    
client.run(TOKEN)