#-------------------------------------------------------

import asyncio
import discord

from discord.ext import commands
from resources.functions import *

#-------------------------------------------------------

class Manager(commands.Cog):
    """Manager Commands"""
    def __init__(self, bot):
        self.bot = bot
        
#-------------------------------------------------------

    @commands.command(help="Create a channel")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def create_channel(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        Questions = ["What should be channel name ?", "Is it private channel ?"]
        Answers = []

        for i in Questions:
            await ctx.send(i)

            try:
                message = await self.bot.wait_for('message', check=check, timeout=15)
            except asyncio.TimeoutError:
                embed = discord.Embed(description="Timed out! Please be quicker next time", color=discord.Color.red())
                await ctx.send(embed=embed)
            else:
                Answers.append(message.content)

        if Answers[1].lower() == "no":
            try:
                await ctx.guild.create_text_channel(name=str(Answers[0]))
                embed = discord.Embed(description="Channel created successfully", color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await bot_missing_perms(ctx)
        elif Answers[1].lower() == "yes":
            try:
                channel = await ctx.guild.create_text_channel(name=str(Answers[0]))
                await channel.set_permissions(ctx.guild.default_role, view_channel=False)
                embed = discord.Embed(description="Channel created successfully", color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await bot_missing_perms(ctx)
        else:
            embed = discord.Embed(description="Please answer in Yes/No", color=discord.Color.red())
            await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Delete a channel")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def delete_channel(self, ctx, channel: discord.TextChannel):
        try:
            await channel.delete(reason=f"{str(ctx.author)}")
            embed = discord.Embed(description="Channel deleted successfully", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Create a role")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def create_role(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        Questions = ["What should be role name ?", "Is it admin role ?"]
        Answers = []

        for i in Questions:
            await ctx.send(i)

            try:
                message = await self.bot.wait_for('message', check=check, timeout=15)
            except asyncio.TimeoutError:
                embed = discord.Embed(description="Timed out! Please be quicker next time", color=discord.Color.red())
                await ctx.send(embed=embed)
            else:
                Answers.append(message.content)

        if Answers[1].lower() == "no":
            try:
                await ctx.guild.create_role(name=str(Answers[0]))
                embed = discord.Embed(description="Role created successfully", color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await bot_missing_perms(ctx)
        elif Answers[1].lower() == "yes":
            try:
                role = await ctx.guild.create_role(name=str(Answers[0]))
                perms = discord.Permissions()
                perms.update(administrator=True)
                await role.edit(permissions=perms)
                embed = discord.Embed(description="Role created successfully", color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await bot_missing_perms(ctx)
        else:
            embed = discord.Embed(description="Please answer in Yes/No", color=discord.Color.red())
            await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Delete a role")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def delete_role(self, ctx, role: discord.Role):
        try:
            await role.delete(reason=f"{str(ctx.author)}")
            embed = discord.Embed(description="Role deleted successfully", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Add/Remove role from a user")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def role(self, ctx, member : discord.Member, role : discord.Role):
        if role in member.roles:
            try:
                await member.remove_roles(role, reason=f"{str(ctx.author)}")
                embed = discord.Embed(description=f"Removed role from  {member.mention} | {role.mention}", color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await bot_missing_perms(ctx)
        else:
            try:
                await member.add_roles(role, reason=f"{str(ctx.author)}")
                embed = discord.Embed(description=f"Added role for {member.mention} | {role.mention}", color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await  bot_missing_perms(ctx)
                
#-------------------------------------------------------

def setup(bot):
    bot.add_cog(Manager(bot))

#-------------------------------------------------------