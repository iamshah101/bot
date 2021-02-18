from discord.ext import commands
import discord
import asyncio

class MiscText(commands.Cog):
    def __init__(self, bot,):
        self.bot = bot
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")

    @commands.command(aliases= ['online?'])
    async def online(self, ctx):
        await ctx.send("Yes Master")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(MiscText(bot))
