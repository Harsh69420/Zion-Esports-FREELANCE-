#-------------------------------------------------------

import discord
import asyncio

from discord.ext import commands
from resources.functions import *

#-------------------------------------------------------

class Moderation(commands.Cog):
    """Moderator Commands"""
    def __init__(self, bot):
        self.bot = bot

#-------------------------------------------------------

    @commands.command(aliases=['clear'], help="Delete a channel's messages")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount : int):
        try:
            await ctx.channel.purge(limit=amount+1)
            sent = await ctx.send(f"Purged **{amount} messages**")
            await asyncio.sleep(2)
            await sent.delete()
        except discord.Forbidden:
            await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Kicks a user from the server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *,reason=None):
        if not reason:
            reason = "No reason was provided"

        try:
            await member.kick(reason=f"{reason} | {ctx.author.name}")
            embed = discord.Embed(description=f"Kicked {member.display_name} | **{reason}**", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Bans a user from the server")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *,reason=None):
        if not reason:
            reason = "No reason was provided"

        try:
            await member.ban(reason=f"{reason} | {ctx.author.name}")
            embed = discord.Embed(description=f"Banned {member.display_name} | **{reason}**", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Unbans a user from the server")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id : int):
        try:
            user = await self.bot.fetch_user(id)
            try:
                await ctx.guild.unban(user)
                embed = discord.Embed(description=f"Unbanned {user.name}", color=discord.Color.green())
                await ctx.send(embed=embed)
            except discord.Forbidden:
                await bot_missing_perms(ctx)
        except discord.NotFound:
            embed = discord.Embed(description="ID is not Valid", color=discord.Color.red())
            await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Change the nickname of a user.")
    @commands.has_permissions(manage_nicknames=True)
    async def chnick(self, ctx, member : discord.Member, *,nick):
        try:
            await member.edit(nick=nick)
            embed = discord.Embed(description=f"Changed nickname for {member.display_name}", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Server-mutes a user")
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member : discord.Member, *,reason=None):
        if not reason:
            reason = "No reason was provided"
        try:
            await create_mute_role(ctx.guild)
        except discord.Forbidden:
            await bot_missing_perms(ctx)
            return

        muteRole = discord.utils.get(ctx.guild.roles, name="Muted")
        try:
            if muteRole not in member.roles:
                await member.add_roles(muteRole, reason=f"{reason} | {ctx.author}")
                embed = discord.Embed(description=f"Muted {member.display_name} | **{reason}**", color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f"{member.display_name} is already muted", color=discord.Color.red())
                await ctx.send(embed=embed)
        except discord.Forbidden:
            await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Unmutes a user")
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member : discord.Member):
        try:
            await create_mute_role(ctx.guild)
        except discord.Forbidden:
            await bot_missing_perms(ctx)
            return

        muteRole = discord.utils.get(ctx.guild.roles, name="Muted")


        try:
            if muteRole in member.roles:
                await member.remove_roles(muteRole, reason=str(ctx.author))
                embed = discord.Embed(description=f"Unmuted {member.display_name}", color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f"{member.display_name} is not muted", color=discord.Color.red())
                await ctx.send(embed=embed)
        except discord.Forbidden:
                await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Temporarily server-mutes a user")
    @commands.has_permissions(kick_members=True)
    async def tempmute(self, ctx, member: discord.Member, time, reason=None):
        if not reason:
            reason = "No reason was provided"

        try:
            await create_mute_role(ctx.guild)
        except discord.Forbidden:
            await bot_missing_perms(ctx)
            return

        muteRole = discord.utils.get(ctx.guild.roles, name="Muted")

        u_list = ['s', 'm', 'h', 'd']
        if time[-1].lower() in u_list:
            x = convertTime(time)
            try:
                if muteRole not in member.roles:
                    await member.add_roles(muteRole, reason=f"{reason} | {ctx.author}")
                    embed = discord.Embed(description=f"Muted {member.display_name} for {time} | **{reason}**", color=discord.Color.green())
                    await  ctx.send(embed=embed)
                    await  asyncio.sleep(x)
                    await member.remove_roles(muteRole, reason="Mute duration expired")
                else:
                    embed = discord.Embed(description=f"{member.display_name} is not muted", color=discord.Color.red())
                    await ctx.send(embed=embed)
            except discord.Forbidden:
                await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Lock a channel.")
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel : discord.TextChannel = None):
        if not channel:
            channel = ctx.channel

        try:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            embed = discord.Embed(description=f"Locked  {channel.mention}", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await bot_missing_perms(ctx)

#-------------------------------------------------------

    @commands.command(help="Unlock a channel.")
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        if not channel:
            channel = ctx.channel
        try:
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            embed = discord.Embed(description=f"Unlocked  {channel.mention}", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await bot_missing_perms(ctx)

#-------------------------------------------------------

def setup(bot):
    bot.add_cog(Moderation(bot))

#-------------------------------------------------------