import discord
from dotenv import load_dotenv
import os


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as ' + str(client.user))

@client.event
async def on_message(message):
    async def sendMsg(txt):
        await message.channel.send("```{}```".format(txt))

    # Don't register if the message is from the bot
    if message.author == client.user:
        return

    # Someone uses the '/' to input a commands
    elif message.content.startswith('/'):
        
        if message.content == '/help':
            await sendMsg('you need help')
            return

        elif message.content.startswith('/roll'):
            await sendMsg('Rollin...')

            parsedText = message.content.split(' ')
            
            if len(parsedText) != 2:
                await sendMsg('Improper use of command')
                return
            
            rollParse = parsedText[1].split('d')

            rolls = []

            for x in range(0, int(rollParse[0])):
                rolls.append(rollParse[1])
            
            await sendMsg(rolls)
            return

        elif message.content.startswith('/what'):
            await sendMsg('What do you want')
            return
        else:
            await sendMsg('Unrecognized command. type /help for commands')
            return

load_dotenv()
client.run(os.getenv('TOKEN'))
