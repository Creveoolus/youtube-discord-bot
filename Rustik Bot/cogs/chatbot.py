import discord
from discord.ext import commands
import asyncio
import random

class ChatBot(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.inv = 'ᅠ'

	@commands.Cog.listener()
	async def on_ready(self):
		print('[Cog] ChatBot был загружен')

	@commands.Cog.listener()
	async def on_message(self, message):
		print(f'{message.author}: {message.content}')

	@commands.command()
	async def hi(self, ctx):
		await ctx.send(f'Привет {ctx.author.mention}!')

	@commands.command(aliases=['rand'])
	async def random(self, ctx, min=1, max=11):
		outuput = random.randrange(min, max)

		await ctx.send(str(outuput))

def setup(client):
	client.add_cog(ChatBot(client))
