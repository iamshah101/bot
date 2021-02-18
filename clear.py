from discord.ext import commands
import asyncio

class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        description="Deletes the given amount of messages", aliases= ['c'])
    @commands.has_permissions(manage_channels=True)
    async def clear(self, ctx, amount=5):
        if amount > 200:
            await ctx.send(
                '**Big limit**')
        else:
            await ctx.channel.purge(limit=amount + 1)
            await asyncio.sleep(2)
            await ctx.message.delete()
    #--------------------------------------------------------------------------------------------------------

def setup(bot):
    bot.add_cog(clear(bot))
