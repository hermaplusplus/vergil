import discord
import logging
import os
from random import choice as choose
from datetime import datetime

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
if not os.path.exists("logs"):
    os.makedirs("logs")
handler = logging.FileHandler(filename='logs/vergil-' + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.messages = True

responses = {
    "motivation" : ["**Where's your motivation?**",
                    "**Show me your motivation!**",
                    "**Now I'm motivated!**",
                    "**Now I'm a little motivated!**"],
    "bedtime" : ["**It's past your bedtime!**",
                 "https://files.herma.moe/vergil/bedtime.jpg"],
    "power" : ["**I've come to retrieve my power.\nYou can't handle it.**",
               "**This is the power of Sparda.**",
               "**I need more power!**",
               "**My power shall be absolute!",
               "**Power...**",
               "**This...**\n**Is...**\n***Power!***"],
    #"challenge" : ["**You are not worthy as my opponent.**"],
    "difficult" : ["**`Easy mode is now selectable.`**",
                   "https://files.herma.moe/vergil/easymode.jpg"],
    "storm" : ["***I AM THE STORM THAT IS APPROACHING!***"]
}

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in successfully as {client.user}')
    client.activity = discord.Activity(type=discord.ActivityType.competing, name='the Qliphoth')
    await client.change_presence(activity=client.activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if await multi_contains(message.content, ["motivation", "motivatiob", "motivatio", "motivated", "motive", "motiv"]):
        await message.channel.send(choose(responses["motivation"]))
    if await multi_contains(message.content, ["bedtime", "bedtim", "bed time", "bed", "bed tim", "sleep", "slep", "good night", "goodnight"]):
        await message.channel.send(choose(responses["bedtime"]))
    if await multi_contains(message.content, ["power", "powe",]):
        await message.channel.send(choose(responses["power"]))
    #if await multi_contains(message.content, ["challenge", "challege"]):
    #    await message.channel.send(choose(responses["challenge"]))
    if await multi_contains(message.content, ["difficult", "hard", "challenge", "challenging"]):
        await message.channel.send(choose(responses["difficult"]))
    if await multi_contains(message.content, ["storm", "bury the light"]):
        await message.channel.send(choose(responses["storm"]))

async def multi_contains(m="", x=None):
    for i in x:
        if i in m.lower():
            return True
    return False

client.run(open('config/token.txt', 'r').readlines()[0].strip())