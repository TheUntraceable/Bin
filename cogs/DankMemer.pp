import discord
from discord.ext import commands
import random
import asyncio
from discord import Embed
import embed

class DankMemer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['multis'])
    async def multilist(self, ctx):
        embed = discord.Embed(title=f"Dank Memer's Secret Multipliers", description="**Personal Multis**\n• Upvoted [`+3%`]\n• Upvoted on Top.gg recently [`+5%]`\n• Patron [`+5`%]\n• Purchased lootbox [`+3%`]\n• Levelup rewards [`+10%`]: This increases to a max of 10% as you level up\n• Gifted 500 items [`+2%`]\n• Gifting Daddy [`+5%`]\n• SANTA BUT BETTER [`+10%`]: Gifted 100,000+ items\n• Shared 10k coins [`+2%`]\n• Sharing is caring [`+5%`]\n• Sharing LORD [`+10%`]\n• Sharing GOD [`+15%`]\n• Pepe trophy [`+15%`]")
        embed.add_field(name="**Prestige Multis**", value="• Prestige 1-19 [`+75%`]: Prestige 1-18 gives +4% per prestige, Prestige 19 gives 3%\n• 69+ Pink phallic objects [`+2%`]\n• Fidget spinner [`5-25%`]: Do pls use spinner\n• Tidepod [`+25%`]: Do pls use tide\n• Level 69, nice [`+69%`]: Only lasts for this level\n• Cupids big toe [`+69%`]: Using this gives a 69% multi for 69 seconds\n• 7d streak [`+2%`]: Have a 7 day daily streak\n• 69d streak [`+5%`]\n• 3mo streak [+10%]\n \n• 6mo streak [`+15%`]\n• Tips enabled [`+5%`]: Do pls settings tips true\n• Staff pet [`+1%`]: Name your pet after a DMO staff member\n• Won lottery [`+3%`]: Won the Dank Memer lottery with pls lottery\n• DM Notifications on [`+3%`]: Do pls settings dmNotifications true\n• Vote reminder on [`+3%`]: Do pls settings voteReminder true\n• Level 30+ pet [`+5%`]: Having a level 30 or higher pet\n• 1 badge [`5%`]: Owning 1 badge\n \n• 500+ GTN wins [`+5%`]: 500+ wins on pls guess\n• 500+ Trivia wins [`+5%`]: 500+ wins on pls trivia\n• 500+ TTT wins [`+5%`]: 500+ wins on pls tictactoe\n• 500+ Fight wins [`+5%`]: 500+ wins on pls fight\n• Worked 3+ times TODAY [`+3%`]: Work 3 times today with pls work\n• Worked 69+ times [`+5%`]: Work 69 or more times with pls work\n• Passive on [`-25%`]: Having passive mode enabled\n• Previously blacklisted [`-2%`]: Don't try getting this")
        await ctx.send(embed=embed)

    @commands.command(aliases=['multis2'])
    async def multilist2(self, ctx):
        embed = discord.Embed(title=f"Dank Memer's Level Up Rewards", description="Level 1 -> ⏣ 5,000 & Normie Title\nLevel 5 -> Reposter Title\nLevel 10 -> 2% Multiplier & Memer Title\nLevel 15 -> Original Memer Title\nLevel 20 -> ⏣ 10,000 & Total Memer Title\nLevel 25 -> ⏣ 5,000 & Dank Memer Title\nLevel 30 -> ⏣ 6,000\nLevel 40 -> ⏣ 5,000 & 1 Bank Note\nLevel 50 -> 2% Multiplier & Good Meme Title\nLevel 60 -> ⏣ 8,000 & 1 Bank Note\nLevel 69 -> ⏣ 4,000, 69% Temporary Multiplier & 69 Nice Title\nLevel 75 -> 1 Pizza Slice\nLevel 85 -> ⏣ 8,000\nLevel 100 -> 2% Multiplier & Kek Lord Title\nLevel 120 -> ⏣ 10,000\nLevel 140 -> ⏣ 10,000 & 1 Bank Note\nLevel 150 -> ⏣ 10,000\nLevel 175 -> ⏣ 12,000\nLevel 200 -> ⏣ 20,000 & 1 Bank Note\nLevel 225 -> 2 Alcohols\nLevel 250 -> ⏣ 7,000\nLevel 275 -> ⏣ 7,000\nLevel 300 -> ⏣ 12,000 & Amazing Cute Memer Title\nLevel 350 -> 2 Alcohols\nLevel 375 -> ⏣ 12,000\nLevel 400 -> ⏣ 12,000, 2 Bank Notes & Wow Memer Title\nLevel 425 -> ⏣ 13,000\nLevel 450 -> ⏣ 12,000\nLevel 500 -> ⏣ 15,000 & God of Memes Title\nLevel 550 -> ⏣ 12,000\nLevel 600 -> ⏣ 17,000 & 1 Bank Note\nLevel 650 -> 2% Multiplier\nLevel 700 -> ⏣ 10,000 & Literally Dank Memer Title\nLevel 750 -> ⏣ 120,000 & 2% Multiplier\nLevel 1000 -> ⏣ 120,000, 1 Pepe Coin & God Title\nLevel 1250 -> ⏣ 120,000 & 10 Bank Notes\nLevel 1500 -> ⏣ 120,000, 1 Robbers Wishlist & Biggest Brain Title\nLevel 1750 -> ⏣ 120,000 & 10 Bank Notes\nLevel 2000 -> ⏣ 150,000, 100 Hunting Rifles & Tryhard Gamer Title\nLevel 2500 -> ⏣ 150,000 & 1 Pepe Medal\nLevel 3000 -> ⏣ 150,000 & 100 Fishing Poles\nLevel 3500 -> ⏣ 150,000, 69,420 Pink Phallic Objects & Sweatlord Title\nLevel 4000 -> ⏣ 180,000 & 1 Pepe Medal\nLevel 4500 -> ⏣ 180,000 & 1 Cupid’s Big Toe\nLevel 5000 -> ⏣ 500,000, 1 Bolt Cutters & God’s Dad Title")
        embed.add_field(name="**Server Multis**", value="• Premium server [`+10%`]: Has Dank Memer Premium\n• Partner server [`+10%`]: Partnered with DMO (`pls partners`)\n• Dank Memer Support Booster [`+10%`]: Server boost [this server](discord.gg/meme)\n• DMC Booster [+10%]: Server boost [this server](discord.gg/memers)\n• DMC Giveaway donor [`5%`]: Donate ⏣ 50m+ in [this server](discord.gg/memers)\n• DMC Max level [`+10%`]: Reach level 250 in [this server](discord.gg/memers)(discord.gg/memers)\n• #dank-memer [`+5%]`: The channel name has `dank-memer` in it")
        await ctx.send(embed=embed)

    @commands.command(aliases=['multis2'])
    async def taxcalc(self, ctx):
      yes=3

def setup(bot):
  bot.add_cog(DankMemer(bot))
  print("Dank Memer is ready")