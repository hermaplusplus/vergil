import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)



client.run(open('config/token.txt', 'r').readlines()[0].strip())