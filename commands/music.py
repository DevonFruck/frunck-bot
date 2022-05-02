import discord
from discord.ext import commands
import youtube_dl
#import PyNaCl

class music(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.queue = []
        print("music cog is set up")

    @commands.command()
    async def connect(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('```You must join a voice channel so I can connect!```')
            return

        print(ctx.author)
        voice_channel = ctx.author.voice.channel
        
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        
    @commands.command()
    async def disconnect(self, ctx):
        ctx.voice_client.disconnect()
    
    
    @commands.command()
    async def clear(self):
        self.queue = []

    @commands.command()
    async def play(self, ctx, url : str):
        FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
        }
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download= False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

def setup(client):
  client.add_cog(music(client))