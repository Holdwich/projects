import asyncio
import discord
from discord import app_commands
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl
import asyncio


intents = discord.Intents.all()
intents.message_content = True

load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!!", intents=intents)
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

async def load():
  for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
          await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load()
    await bot.start(token)

asyncio.run(main())