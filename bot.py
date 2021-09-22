import discord, os, sys
from dotenv import load_dotenv

sys.path.append('{}/commands'.format(os.getcwd()))
from roll import roll_cmd

client = discord.Client()


@client.event
async def on_ready():
  print('Logged in as {}'.format(client.user))


@client.event
async def on_message(message):

  # Don't register if the message is from the client
  if message.author == client.user:
    return
  
  async def sendMsg(txt):
    await message.channel.send(txt)

  # Someone uses the '/' to input a commands
  if message.content.startswith('/'):
    input = message.content.lower()

    if input == '/help':
      await sendMsg("I can't help you until my developer implements me!")
      return

    elif input.startswith('/roll'):
      await roll_cmd(message.content, message.author, sendMsg)
      return

    else:
      await sendMsg('Unrecognized command. type /help for commands')
      return

load_dotenv()
client.run(os.getenv('TOKEN'))
