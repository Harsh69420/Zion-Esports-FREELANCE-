#-------------------------------------------------------

from functools import total_ordering
import discord

from discord.ext import commands
from aiohttp import request

#-------------------------------------------------------

class Info(commands.Cog):
    """Info Commands"""
    def __init__(self, bot):
        self.bot = bot

#-------------------------------------------------------

    @commands.command(help="Get pfp of a user")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author

        embed = discord.Embed(title=f"{member.display_name}'s Avatar", description=f"Link as\n[png]({member.avatar_url_as(format='png')}) | [jpg]({member.avatar_url_as(format='jpg')}) | [webp]({member.avatar_url_as(format='webp')})", color=discord.Color.random())
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(aliases=["whois"], help="Get information about a particular user")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=discord.Colour.random(), timestamp=ctx.message.created_at, title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)
        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(aliases=['channelstats'], help="Get information about a particular channel")
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def channel_info(self, ctx: commands.Context, channel: discord.TextChannel):
        channel = channel or ctx.channel
        nsfw = self.bot.get_channel(channel.id).is_nsfw()
        news = self.bot.get_channel(channel.id).is_news()
        embed = discord.Embed(title='Channel Infromation: ' + str(channel), colour=discord.Color.random(), timestamp=ctx.message.created_at)
        embed.add_field(name='Channel Name: ', value=str(channel.name))
        embed.add_field(name="Channel's NSFW Status: ", value=str(nsfw))
        embed.add_field(name="Channel's id: ", value=str(channel.id))
        embed.add_field(name='Channel Created At: ', value=str(channel.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.add_field(name='Channel Type: ', value=str(channel.type))
        embed.add_field(name="Channel's Announcement Status: ", value=str(news))
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Get information about the current server")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def server(self, ctx):
        findbots = sum(1 for member in ctx.guild.members if member.bot)
        embed = discord.Embed(title=f'Server Info: {ctx.guild.name} ', colour=discord.Color.random(), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.add_field(name="Guild's name: ", value=ctx.guild.name)
        embed.add_field(name="Guild's owner: ", value=str(ctx.guild.owner))
        embed.add_field(name="Guild's verification level: ", value=str(ctx.guild.verification_level))
        embed.add_field(name="Guild's id: ", value=str(ctx.guild.id))
        embed.add_field(name="Guild's member count: ", value=f"Humans: {str(ctx.guild.member_count)})\nBots: {findbots}")
        embed.add_field(name="Guild created at: ", value=str(ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
        
#-------------------------------------------------------

def setup(bot):
    bot.add_cog(Info(bot))

#-------------------------------------------------------