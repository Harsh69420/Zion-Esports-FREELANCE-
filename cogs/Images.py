#-------------------------------------------------------
import random
import discord

from discord.ext import commands
from aiohttp import request

#-------------------------------------------------------

class Images(commands.Cog):
    """ Roast From Images  """
    def __init__(self, bot):
        self.bot = bot

#-------------------------------------------------------

    @commands.command(help="Very bad memes :joy:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def meme(self, ctx):
        LINK = "https://some-random-api.ml/meme"

        async with request('GET', LINK) as f:
            if f.status == 200:
                data = await f.json()

        embed = discord.Embed(title=data['caption'], color=discord.Color.random())
        embed.set_image(url=data['image'])
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Show your gay pride :gay_pride_flag:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def gay(self, ctx, member : discord.Member=None):
        if not member:
            member = ctx.author

        embed = discord.Embed(title="GAY", color=discord.Color.random())
        embed.set_image(url=f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='png')}")
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="You've successfully wasted your life !!")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def wasted(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        embed = discord.Embed(title="WASTED", color=discord.Color.random())
        embed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}")
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Go to Jail :police_officer:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def jail(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        embed = discord.Embed(title="JAIL", color=discord.Color.random())
        embed.set_image(url=f"https://some-random-api.ml/canvas/jail?avatar={member.avatar_url_as(format='png')}")
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Welcome back comrade")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def comrade(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        embed = discord.Embed(title="COMRADE", color=discord.Color.random())
        embed.set_image(url=f"https://some-random-api.ml/canvas/comrade?avatar={member.avatar_url_as(format='png')}")
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Respect+")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def missionpassed(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        embed = discord.Embed(title="MISSION PASSED", color=discord.Color.random())
        embed.set_image(url=f"https://some-random-api.ml/canvas/passed?avatar={member.avatar_url_as(format='png')}")
        await ctx.send(embed=embed)

#-------------------------------------------------------

    @commands.command(help="Wink someone to flirt !!")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def wink(self, ctx, member: discord.Member=None):
        if not member:
            await ctx.send("Who do you want to wink ?")
        else:
            x = [
                f'{ctx.author.name} winks {member.display_name} UwU',
                f'{ctx.author.name} winks {member.name}!'
            ]

            LINK = "https://some-random-api.ml/animu/wink"
            async with request('GET', LINK) as f:
                if f.status == 200:
                    data = await f.json()

            embed = discord.Embed(color=discord.Color.random())
            embed.set_image(url=data['link'])
            embed.set_author(icon_url=ctx.author.avatar_url, name=random.choice(x))
            await ctx.send(embed=embed)

#-------------------------------------------------------
    
    @commands.command(help="Hug someone :people_hugging:")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("Who do you want to hug ?")
        else:
            x = [
                f'{ctx.author.name} hugs {member.display_name} UwU',
                f'{ctx.author.name} gives {member.name} a big hug!'
            ]

            LINK = "https://some-random-api.ml/animu/hug"
            async with request('GET', LINK) as f:
                if f.status == 200:
                    data = await f.json()

            embed = discord.Embed(color=discord.Color.random())
            embed.set_image(url=data['link'])
            embed.set_author(icon_url=ctx.author.avatar_url, name=random.choice(x))
            await ctx.send(embed=embed)

#-------------------------------------------------------
    
    @commands.command(help="Pat someone to motivate!!")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("Who do you want to pat ?")
        else:
            x = [
                f'{ctx.author.name} pats {member.display_name} :3',
                f'{ctx.author.name} pats {member.name}! So motivating'
            ]

            LINK = "https://some-random-api.ml/animu/pat"
            async with request('GET', LINK) as f:
                if f.status == 200:
                    data = await f.json()

            embed = discord.Embed(color=discord.Color.random())
            embed.set_image(url=data['link'])
            embed.set_author(icon_url=ctx.author.avatar_url, name=random.choice(x))
            await ctx.send(embed=embed)

#-------------------------------------------------------

def setup(bot):
    bot.add_cog(Images(bot))

#-------------------------------------------------------