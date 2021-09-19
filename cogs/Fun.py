#-------------------------------------------------------

import discord
import random

from discord.ext import commands
from resources.assets.kill import killSent
from resources.assets.roast import roastSent
from aiohttp import request

#-------------------------------------------------------

class Fun(commands.Cog):
    """Fun Commands"""
    def __init__(self, bot):
        self.bot = bot

#-------------------------------------------------------

    @commands.command(help="See how gay you are (100% real) :gay_pride_flag:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def gayrate(self, ctx, member : discord.Member=None):
        if not member:
            member = ctx.author
        x = random.randint(0, 100)
        embed = discord.Embed(title="Gay Rate Machine", color=discord.Color.random())
        embed.add_field(name=f"{member.display_name}'s Gayrate", value=f"{member.display_name} is {x}% gay :gay_pride_flag:")
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="See how simp you are (100% real)")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def simprate(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        x = random.randint(0, 100)
        embed = discord.Embed(title="Simp Rate Machine", color=discord.Color.random())
        embed.add_field(name=f"{member.display_name}'s Simprate",
                        value=f"{member.display_name} is {x}% simp")
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="See how epic gamer you are (100% real) :video_game:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def epicgamerrate(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        x = random.randint(0, 100)
        embed = discord.Embed(title="Epic Gamer Rate Machine", color=discord.Color.random())
        embed.add_field(name=f"{member.display_name}'s Epic Gamer Rate",
                        value=f"{member.display_name} is {x}% epic gamer")
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(aliases=['8ball'], help="Ask question and get advice from me :8ball:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def _8ball(self, ctx, *, question):
        ch = ['Yes', 'No', 'Maybe', "I'm not sure"]
        x = random.choice(ch)
        await ctx.reply(x)

#-------------------------------------------------------

    @commands.command(help="Press F to pay respect :regional_indicator_f:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def f(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send(f"{ctx.author.mention} has paid their respects :regional_indicator_f:")
        else:
            await ctx.send(f"{ctx.author.mention} has paid their respects for {member.mention} :regional_indicator_f:")

#-------------------------------------------------------

    @commands.command(help="Coinflip! :coin:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def coinflip(self, ctx):
        ch = ['Heads', 'Tails']
        x = random.choice(ch)
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{x}**!")

#------------------------------------------------------

    @commands.command(help="Sick of someone? Easy! Just kill them! :knife:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def kill(self, ctx, member : discord.Member=None):
        if not member:
            await ctx.send("Whom are we trying to kill ?")

        else:
            x = killSent()
            await ctx.send(f"{member.mention} {x}")

#------------------------------------------------------

    @commands.command(help="Sick of someone? Easy! Just roast them!")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def roast(self, ctx, member : discord.Member=None):
        if not member:
            await ctx.send("You can't roast yourself lol! Mention a member")
        else:
            x = roastSent()
            await ctx.send(f"{member.mention} {x}")

#-------------------------------------------------------

    @commands.command(help="See a funny joke. :joy:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def joke(self, ctx):
        LINK = "https://some-random-api.ml/joke"
        async with request('GET', LINK) as f:
            if f.status == 200:
                data = await f.json()

        await ctx.send(data['joke'])

#-------------------------------------------------------

    @commands.command(help="Make the bot say whatever you want with emojis!")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def emojify(self, ctx, *,arg : str):
        numDict = {"1": ":one:", "2": ":two:", "3": ":three:", "4": ":four:", "5": ":five:", "6": ":six:", "7": ":seven:", "8": ":eight:", "9": ":nine:", "0": ":zero:"}
        myL = []
        for i in arg:
            if i.isdigit():
                myL.append(numDict[i])
            elif i.isalpha():
                myL.append(f":regional_indicator_{i}:")
            else:
                myL.append(" ")
        await ctx.send(" ".join(myL))

#-------------------------------------------------------

    @commands.command(help="Check your PP size (Actually you have 0cm)")
    @commands.cooldown(1,1, commands.BucketType.user)
    async def pp(self, ctx, member : discord.Member=None):
        if not member:
            member = ctx.author
        x = random.randint(0, 20)
        embed = discord.Embed(title="PP Size Machine", color=discord.Color.random())
        embed.add_field(name=f"{member.display_name}'s PP", value=f"8{'=' * x}D")
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Make the bot say whatever you want! :speaking_head: ")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def say(self, ctx, *,arg=None):
        if not arg:
            await ctx.send("What do you want me to say lol ?")
        else:
            await ctx.send(f"{arg}\n\n- **{ctx.author}**")

#-------------------------------------------------------

    @commands.command(help="Make the bot say whatever you want in annoying spoiler form! ||:speaking_head: ||")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def spoiler(self, ctx, *,arg=None):
        if not arg:
            await ctx.send("What do you want me to say bruh ?")
        else:
            myL = []
            for i in arg:
                myL.append(f"||{i}||")
        await ctx.send("".join(myL))
        
#-------------------------------------------------------

def setup(bot):
    bot.add_cog(Fun(bot))

#-------------------------------------------------------