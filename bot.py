import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='https://shock.atshop.io/'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!ufa':
        await client.send_message(message.channel,'Hi! We currently do not have any UFA'S in stock!')
    if message.content.startswith('!coinflip'):
        randomlist = ['heads','tails',]
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run('NjEzMTE1OTUyNTQzOTU3MDEy.XVtBRw.uOHTm99YoybSXsRSOpaywpMY6q8')
