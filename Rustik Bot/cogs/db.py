import discord
from discord.ext import commands
import asyncio
import random
from discord.ext.commands import CommandNotFound
import pyrebase
import config

firebase = pyrebase.initialize_app(config.firebase)
db = firebase.database()

class DB(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.inv = 'ᅠ'

	@commands.Cog.listener()
	async def on_ready(self):
		user = db.child('users').child('1').get()

		print(user.key())
		print(user.val()['class'])


def setup(client):
	client.add_cog(DB(client))
