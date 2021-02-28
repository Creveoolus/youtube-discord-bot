import discord
from discord.ext import commands
import asyncio
import random

class Embeds(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.inv = 'ᅠ'

	@commands.command(alieses=['newembed'])
	async def embed(self, ctx):
		footer_text = f'Запрошено {ctx.author.name}'
		footer_icon = ctx.author.avatar_url

		e = discord.Embed(color=discord.Color.green(), title='I am a title!', description='I am a description!', timestamp=ctx.message.created_at, url='https://youtube.com/c/creveoolus')
		e.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url, url='https://youtube.com/c/creveoolus')
		e.add_field(name='Field name #1', value='Field value\nInline: True', inline=True)
		e.add_field(name='Field name #2', value='Field value\nInline: True', inline=True)
		e.add_field(name='Field name #3', value='Field value\nInline: False', inline=False)
		e.set_thumbnail(url=ctx.guild.icon_url)
		e.set_image(url='https://images-ext-2.discordapp.net/external/qYOd3lmRMjoGuWqae7hCp260oqK1gfkbWzcmJ1k8EAg/https/cdn.nekos.life/wallpaper/65VgtPyweCc.jpg?width=475&height=672')
		e.set_footer(text=footer_text, icon_url=footer_icon)

		await ctx.send(embed=e)


def setup(client):
	client.add_cog(Embeds(client))
