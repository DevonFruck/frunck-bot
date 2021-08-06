import discord
from dotenv import load_dotenv
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}.format(client)')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.content.startswith('!')):
        if (message.content.contains('hi')):
            await message.channel.send("Don't say hi to me!")
        else:
            await message.channel.send('Hello!')

load_dotenv()
client.run(os.getenv('TOKEN'))
