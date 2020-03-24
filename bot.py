import discord
from discord.ext import commands

TOKEN = 'your_token_here'

description = '''idfk'''
bot = commands.Bot(command_prefix='baconz ', description=description)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="rick astley"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def ping(ctx):
    """later(tm)"""
    await ctx.send("brug moment")

bot.run(TOKEN)