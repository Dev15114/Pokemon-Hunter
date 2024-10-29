import os
import discord
form discord.ext import command
form discord import app_command

form mysever import sever_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())



sever_on()

bot.run(os.getenv('TOKEN'))

