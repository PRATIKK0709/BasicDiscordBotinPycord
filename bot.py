import discord
from discord.ext import commands
import os 

import sys
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Bot is ready")

@bot.command()
async def ping(ctx):
    bot_ping = round(bot.latency * 1000, 2)
    await ctx.send(f"Bot latency is {bot_ping}ms")

bot.run("TOKEN") # run the bot with the token
