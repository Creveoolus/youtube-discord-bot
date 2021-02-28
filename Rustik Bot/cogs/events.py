import discord
from discord.ext import commands
import asyncio
import random
from discord.ext.commands import CommandNotFound

class Events(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.inv = 'ᅠ'

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		error = getattr(error, "original", error)

		if isinstance(error, CommandNotFound):
			print('Да, да')
		else:
			print(error)

def setup(client):
	client.add_cog(Events(client))
