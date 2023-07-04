import discord
import config
from discord.ext import commands
from youtube_dl import YoutubeDL

client = commands.Bot(command_prefix='/')

@client.command
async def play(ctx, url):
    vc = await ctx.message.author.voice.channel.connect()

    with YoutubeDL(config.YDL_OPTIONS) as ydl:
        if 'https://' in url:
            info = ydl.extract_info(url, download=False)
        else:
            info = ydl.extract_info(f"ytsearch:{url}", download=False)['entrise'][0]

    link = info['formats'][0]['url']

    vc.play(discord.FFmpegPCMAudio(executable="./bin/ffmpeg.exe", source=link))

client.run(config.token)