import discord
from discord.ext import commands, tasks
import asyncio
import os
import config

intents = discord.Intents.default()

client = commands.Bot(command_prefix='r.', intents=intents)

@client.event
async def on_ready():
	print('Бот онлайн!')

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

client.run(str(config.token))