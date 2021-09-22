import os, sys
from discord.ext import commands
from dotenv import load_dotenv

sys.path.append('{}/commands'.format(os.getcwd()))
from roll import roll_cmd

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
  print('Logged in as {}'.format(bot.user))


@bot.event
async def on_command_error(ctx, error):
  await ctx.send(("```%s```" % error))


@bot.command(name='roll', help="roll baby")
async def roll(ctx, arg):
  await roll_cmd(arg, ctx.author, ctx)


load_dotenv()
bot.run(os.getenv('TOKEN'))
