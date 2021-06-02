import discord
from discord.ext import commands
import random
import asyncio
from discord import Embed
from discord import utils
from discord import Role, Member
from discord.utils import get
from datetime import datetime

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test2(self , ctx):
        await ctx.send("OK- Event")

   # @commands.Cog.listener()
   # async def on_bot_missing_permissions(self, ctx, error):
   #     if isinstance(error, commands.BotMissingPermissions):
   #       embed = discord.Embed(title=f'❌ I do not have permission to do this! Error: {error}', #colour=discord.Colour.red())
   #       await ctx.send(embed=embed)
   #       
    @commands.Cog.listener()
    async def on_bot_missing_permissions(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
          await ctx.send(f"❌ I do not have permission to do this! Error: {error}")



def setup(bot):
 bot.add_cog(Errors(bot))