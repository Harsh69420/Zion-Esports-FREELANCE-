#-------------------------------------------------------

import discord

from discord.ext import commands

#-------------------------------------------------------

bot = commands.Bot(command_prefix=">", case_insensitive=True, intents=discord.Intents.all(), help_command=None)

#-------------------------------------------------------

@bot.event
async def on_ready():
    print("Hello World")

#-------------------------------------------------------

cogs = ['cogs.Moderator', 'cogs.Manager', 'cogs.Information', 
        'cogs.Fun', 'cogs.utility', 'cogs.Images', 'cogs.help',
        'resources.error_handler', 'resources.events']
        
for i in cogs:
    bot.load_extension(i)

#-------------------------------------------------------

bot.run("YOUR TOKEN HERE")

#-------------------------------------------------------