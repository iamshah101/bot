import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=">", status="online")


class Music(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#error handling

@bot.event
async def on_command_error(ctx, error):
    print(ctx.command.name + " was invoked incorrectly")
    print(error)

bot.load_extension('Cogs.mute')
bot.load_extension('Cogs.clear')
bot.load_extension('Cogs.Misc')
bot.load_extension('Cogs.MiscText')
bot.load_extension('Cogs.ban')
bot.load_extension('jishaku')
bot.load_extension('Cogs.music')
#Kick Members

#random


bot.run('ODA5MTAzMTM2NDg3NjM3MDMz.YCQOBA.Sht4TL9UiMbgb6_r6WMVQ0-Bbrc')
