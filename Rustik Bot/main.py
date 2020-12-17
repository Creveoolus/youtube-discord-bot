import discord
from discord.ext import commands, tasks
import asyncio
import os
import config
from itertools import cycle

intents = discord.Intents.default()

client = commands.Bot(command_prefix='r.', intents=intents)

@client.event
async def on_ready():
	print('Бот онлайн!')

	global activity
	activity = cycle([
	discord.Activity(type=discord.ActivityType.listening, name='А4 - KIIDS'),
	discord.Activity(type=discord.ActivityType.watching, name='windy31'),
	discord.Activity(type=discord.ActivityType.listening, name='Shik Music'),
	discord.Game(name='с Discord API')
	])

	change_status.start()

cogs = 0
try:
	cogs = 0
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			cogs += 1
			client.load_extension(f'cogs.{filename[:-3]}')
	print(f'Всего когов загружено: {cogs}')
except:
	print('Когов не обнаружено!')


@tasks.loop(seconds=7)
async def change_status():
	activity_ = next(activity)

	await client.change_presence(status=discord.Status.dnd, activity=activity_)

client.run(str(config.token))