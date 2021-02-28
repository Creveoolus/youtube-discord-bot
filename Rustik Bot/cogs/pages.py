import discord
from discord.ext import commands
import asyncio
import random
from discord.ext.commands import CommandNotFound
from Cybernator import Paginator

class Pages(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.inv = 'ᅠ'

	@commands.command()
	async def pages(self, ctx):
		e1 = discord.Embed(color=discord.Color.green(), title='Команды [1/4]')
		e2 = discord.Embed(color=discord.Color.green(), title='Команды [2/4]')
		e3 = discord.Embed(color=discord.Color.green(), title='Команды [3/4]')
		e4 = discord.Embed(color=discord.Color.green(), title='Команды [4/4]')

		embeds = [e1, e2, e3, e4]

		msg = await ctx.send(embed=e1)
		page = Paginator(self.client, msg, only=ctx.author, embeds=embeds)

		await page.start()


def setup(client):
	client.add_cog(Pages(client))
