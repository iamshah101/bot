from discord.ext import commands
import discord
import asyncio

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(description="Mutes the specified user.",aliases= ['m'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title="Muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" you have been muted from: {guild.name} reason: {reason}")

        #unmuting
class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Unmutes a specified user.",aliases= ['um'])
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
       mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

       await member.remove_roles(mutedRole)
       await member.send(f" you have unmuted from: - {ctx.guild.name}")
       embed = discord.Embed(title="Unmuted", description=f" unmuted {member.mention} since I Forgave You",colour=discord.Colour.light_gray())
       await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Mute(bot))
    bot.add_cog(Unmute(bot))
