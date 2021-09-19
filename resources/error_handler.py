#-------------------------------------------------------

import discord

from discord.ext import commands
from discord.ext.commands.errors import *

#-------------------------------------------------------

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#-------------------------------------------------------

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, CommandNotFound):
            return
        elif isinstance(error, MissingRequiredArgument):
            embed = discord.Embed(description="Missing Required Argument", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, CommandOnCooldown):
            message = ctx.message
            await message.add_reaction("⏳")
        elif isinstance(error, MissingPermissions):
            embed = discord.Embed(description="Why do you think that would work ?", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, MemberNotFound):
            embed = discord.Embed(description="Member Not Found", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, UserNotFound):
            embed = discord.Embed(description="User Not Found", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, RoleNotFound):
            embed = discord.Embed(description="Role Not Found", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, ChannelNotFound):
            embed = discord.Embed(description="Channel Not Found", color=discord.Color.red())
            await ctx.send(embed=embed)
        
        else:
            raise error

#-------------------------------------------------------

def setup(bot):
    bot.add_cog(ErrorHandler(bot))

#-------------------------------------------------------