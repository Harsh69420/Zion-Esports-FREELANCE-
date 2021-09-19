#-------------------------------------------------------

import discord
import asyncio

from discord.ext import commands
from resources.functions import *
from aiohttp import request

#-------------------------------------------------------

class Utility(commands.Cog):
    """Utility Commands"""
    def __init__(self, bot):
        self.bot = bot

#-------------------------------------------------------

    @commands.command(help="A alarm which pings you and reminds you in DMS")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def alarm(self, ctx, time, *, reason=None):
        if not reason:
            reason = ":alarm_clock:"

        x = convertTime(time)

        await ctx.reply("Alarm Set :alarm_clock:")
        await asyncio.sleep(x)
        await ctx.send(f"{ctx.author.mention} Your alarm clock is ringing: {reason}")
        try:
            await ctx.author.send(f"{ctx.author.mention} Your alarm clock is ringing: {reason}")
        except discord.Forbidden:
            pass

#-------------------------------------------------------

    @commands.command(help="Get Image of a color using hex")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def color(self, ctx, hex):
        if hex[-1] == "#":
            embed = discord.Embed(description="Don't use `#` before hex", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=hex.upper())
            embed.set_image(url=f"https://some-random-api.ml/canvas/colorviewer?hex={hex}")
            await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Get lyrics of a song")
    async def lyrics(self, ctx, *, name=None):
        if not name:
            embed = discord.Embed(description="Please specify song name", color=discord.Color.red())
            await ctx.send(embed=embed)

        else:
            LINK = f"https://some-random-api.ml/lyrics?title={name}"
            async with request('GET', LINK) as f:
                if f.status == 200:
                    data = await f.json()

            embed = discord.Embed(title=data['title'], description=data['lyrics'], color=discord.Color.random())
            await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Get bot's latency")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.reply(f"Pong!! **{round(self.bot.latency * 1000)}ms**")

#-------------------------------------------------------

def setup(bot):
    bot.add_cog(Utility(bot))

#-------------------------------------------------------