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
		await message.channel.send('Hello!')

#client.run('ODcxNzYwOTUwMzAxMTc5OTM0.YQgApw.L0T8IzpiYeea2rXpIiK2aC7lKp8')
load_dotenv()
client.run(os.getenv('TOKEN'))
