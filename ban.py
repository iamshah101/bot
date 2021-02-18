from discord.ext import commands
import discord
import asyncio

class Ban(commands.Cog):
	def __init__(self, bot,):
		self.bot = bot
	@commands.command(help="Bans the User,use this: ban [member] [reason]")
	@commands.has_permissions(ban_members=True)
	async def ban (self, ctx, member:discord.User=None, reason =None):
		if member == None or member == ctx.message.author:
			await ctx.channel.send("You cannot ban yourself")
			return
		if reason == None:
			reason = "For being a jerk!"
		message = f"You have been banned from {ctx.guild.name} for {reason}"
		await member.send(message)
		await ctx.guild.ban(member, reason=reason)
		await ctx.channel.send(f"{member.mention} is banned!")
		#unmuting
class Unban(commands.Cog):
	def __init__(self, bot,):
		self.bot = bot
	@commands.command(help="unbans the user mentioned via ID")
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, id: int):
		member = discord.Object(id=id)

		embed = discord.Embed(
			colour=discord.Colour.default(),
			timestamp=datetime.now()
		)

		embed.add_field(name=f"unbanned {member}", value=f"{member} was unbanned by {ctx.author}")
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

		await ctx.send(embed=embed)

		await ctx.guild.unban(member)


def setup(bot):
	bot.add_cog(Ban(bot))
	bot.add_cog(Unban(bot))