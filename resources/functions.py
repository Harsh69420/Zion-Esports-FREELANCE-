#-------------------------------------------------------

import discord
from discord.ext import commands

#-------------------------------------------------------

async def bot_missing_perms(ctx):
    embed = discord.Embed(description="Bot is missing permissions", color=discord.Color.red())
    await ctx.send(embed=embed)

#-------------------------------------------------------

async def create_mute_role(guild):
    muteRole = discord.utils.get(guild.roles, name="Muted")
    if not muteRole:
        muteRole = await guild.create_role(name="Muted")
        perms = discord.Permissions()
        perms.update(send_messages=False)
        muteRole.edit(permissions=perms)

#-------------------------------------------------------

def convertTime(time):
    u = time[-1]
    duration = int(time[:-1])

    timeDict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

    return duration * timeDict[u]

#-------------------------------------------------------