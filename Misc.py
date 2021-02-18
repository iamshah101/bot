from discord.ext import commands
import discord
import asyncio


class Misc(commands.Cog):
    def __init__(self, bot,):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is Online')
        await self.bot.change_presence(activity=discord.Game(name=f"Annoying people in {len(self.bot.guilds)} servers"))

def setup(bot):
    bot.add_cog(Misc(bot))
