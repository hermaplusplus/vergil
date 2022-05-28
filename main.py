import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='vergil.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in successfully as {client.user}')
    client.activity = discord.Activity(type=discord.ActivityType.competing, name='the Qliphoth')
    await client.change_presence(activity=client.activity)

client.run(open('config/token.txt', 'r').readlines()[0].strip())