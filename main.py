import os
import discord
form discord.ext import command
form discord import app_command

form mysever import sever_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Token สำหรับรันบอท
Token = 'MTMwMDc0ODE5ODY3MDg5MzEzNw.GjgkP8.2SR_iDZ-EjaNj6Rlnj4wX65dnGT51EyLAN5aHc'

sever_on()
bot.run(os.getenv('TOKEN'))

