import discord
import logging
import os
from random import choices as choose
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
    "motivation" : [("**Where's your motivation?**", 1),
                    ("**Show me your motivation!**", 1),
                    ("**Now I'm motivated!**", 1),
                    ("**Now I'm a little motivated!**", 1)],
    "bedtime" : [("**It's past your bedtime!**", 1),
                 ("https://files.herma.moe/vergil/bedtime.jpg", 1)],
    "power" : [("**I've come to retrieve my power.\nYou can't handle it.**", 1),
               ("**This is the power of Sparda.**", 1),
               ("**I need more power!**", 1),
               ("**My power shall be absolute!**", 1),
               ("**Power...**", 1),
               ("**This...**\n**Is...**\n***Power!***", 1)],
    "difficult" : [("**`Easy mode is now selectable.`**", 1),
                   ("https://files.herma.moe/vergil/easymode.jpg", 1)],
    "storm" : [("***I AM THE STORM THAT IS APPROACHING!***", 1)]
}

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in successfully as {client.user}')
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.competing,
        name = 'the Qliphoth'
    ))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if await multi_contains(message.content, ["motivation", "motivatiob", "motivatio", "motivated", "motive", "motiv"]):
        await message.channel.send(choose([i[0] for i in responses["motivation"]],
                                          weights=[i[1] for i in responses["motivation"]])[0])
    if await multi_contains(message.content, ["bedtime", "bedtim", "bed time", "bed", "bed tim", "sleep", "slep", "good night", "goodnight"]):
        await message.channel.send(choose([i[0] for i in responses["bedtime"]],
                                          weights=[i[1] for i in responses["bedtime"]])[0])
    if await multi_contains(message.content, ["power", "powe",]):
        await message.channel.send(choose([i[0] for i in responses["power"]],
                                          weights=[i[1] for i in responses["power"]])[0])
    if await multi_contains(message.content, ["difficult", "hard", "challenge", "challenging"]):
        await message.channel.send(choose([i[0] for i in responses["difficult"]],
                                          weights=[i[1] for i in responses["difficult"]])[0])
    if await multi_contains(message.content, ["storm", "bury the light"]):
        await message.channel.send(choose([i[0] for i in responses["storm"]],
                                          weights=[i[1] for i in responses["storm"]])[0])

async def multi_contains(m="", x=None):
    for i in x:
        if i in m.lower():
            return True
    return False

client.run(open('config/token.txt', 'r').readlines()[0].strip())