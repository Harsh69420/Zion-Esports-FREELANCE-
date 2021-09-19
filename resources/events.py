#-------------------------------------------------------

import discord

from discord.ext import commands

#-------------------------------------------------------

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

#-------------------------------------------------------

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        x =  message.author.guild_permissions.mention_everyone
        if message.content == "@everyone":
            if x == False:
                await message.reply("Why do you think that would work ?")
                return

#-------------------------------------------------------        
        
def setup(bot):
    bot.add_cog(Events(bot))

#-------------------------------------------------------