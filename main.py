import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='vergil.log', encoding='utf-8', mode='w')
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
    "challenge" : ["**You are not worthy as my opponent.**"],
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

client.run(open('config/token.txt', 'r').readlines()[0].strip())