import discord
from discord.ext import commands
import asyncio
import random

class Ban_kick(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.inv = 'ᅠ'

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member:discord.Member=None, *, reason='Причина не указана'):
		if member is None:
			await ctx.send('**Укажите кого мне забанить!**')
		else:
			try:
				if member.bot:
					await ctx.send('**Я не могу банить ботов!**')
				else:
					await member.ban(reason=f'Модератор: {ctx.author}; Причина: {reason}')
			except Forbidden:
				await ctx.send('**У меня не достаточно прав! (ban_members)**')

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member:discord.Member=None, *, reason='Причина не указана'):
		if member is None:
			await ctx.send('**Укажите кого мне кикнуть!**')
		else:
			try:
				if member.bot:
					await ctx.send('**Я не могу кикать ботов!**')
				else:
					await member.kick(reason=f'Модератор: {ctx.author}; Причина: {reason}')
			except Forbidden:
				await ctx.send('**У меня не достаточно прав! (kick_members)**')

			except Exception as e:
				await ctx.send(f'```bash\n{e}\n```')

def setup(client):
	client.add_cog(Ban_kick(client))
