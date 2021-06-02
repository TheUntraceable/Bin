import discord
from discord.ext import commands
from datetime import date
import json
import random
import asyncio

class Birthday(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  async def date(self,ctx):
    await ctx.send(str(date.today())[4:])


  @commands.command(aliases=["setbirthday", "birthdayset", "birthday", "bday", "setbday"])
  async def setbdy(self,ctx,datee):
    datee2 = list(datee.split('-'))
    await ctx.send(f'Birthday Set to {int(datee2[0])}-{int(datee2[1])}')
    # with open('bday.json','r') as f:
    #   m = json.load(f)
    #
    # try:
    #   del m[str(ctx.author.id)]
    # except:
    #   pass
    # m[ctx.author.id] = [ctx.channel.id,datee]
    #
    # with open('bday.json','w') as f:
    #   json.dump(m,f)
    check = await self.client.db.fetchrow("SELECT member_id FROM birthday WHERE member_id=$1",ctx.author.id)
    if check:
        await self.client.db.execute("UPDATE birthday SET info=$1 WHERE member_id=$2",f"{ctx.channel.id},{datee}",ctx.author.id)
    else:
        await self.client.db.execute("INSERT INTO birthday (member_id, info) VALUES ($1, $2)", ctx.author.id, f"{ctx.channel.id},{datee}")


  @commands.command(aliases=['upc', "bdays"])
  async def upcoming(self,ctx):
    # with open('bday.json','r') as f:
    #   m = json.load(f)
    l = str(date.today())[5:]
    m = await self.client.db.fetch("SELECT * FROM birthday")
    list_needed = {}
    cool = False
    count=1
    embed=discord.Embed(title='Upcoming birthdays',colour=discord.Colour.blue())
    # for i in m.keys():
    #   channelid = m[i][0]
    #   for d in ctx.guild.channels:
    #     if int(d.id) == channelid:
    #
    #       embed.add_field(name='\u200b',value=f"<@!{(i)}>'s Birthday - {m[i][1]}")
    #       count+=1
    #     else:
    #       continue
    for record in m:
        arr = [data for data in record.values()]
        split = arr[1].split(',')
        embed.add_field(name='\u200b',value=f"<@!{(arr[0])}>'s Birthday - {split[1]}")
    await ctx.send(embed=embed)

  # @setbdy.error
  # async def setbb_error(self,ctx,error):
  #   await ctx.send('Make sure your date is in this format - month-day likke for example if my birthday is 1st feb then i will set my bithday as `02-01`')

  @commands.command()
  async def guess(self,ctx):
    await ctx.send('**Welcome to the guessing game**\nMy number is between 1 - 10, you have 3 guesses to guess my number')
    number = random.randint(1,10)
    guess_count = 0
    while guess_count < 3:
      await ctx.send('What is your guess?')

      def check(m):
        return m.author == ctx.author and m.content.isdigit()
      try:
        msg = await self.client.wait_for('message', timeout=10.0,check=check)
        guess = int(msg.content)
        if guess < number:
          await ctx.send('Your guess is smaller than my number')
        elif guess > number:
          await ctx.send('Your guess is bigger than my number')
        elif guess == number:
          await ctx.send('Your guess is correct!!!')
          break
        guess_count += 1
        if guess_count == 3 and guess != number:
          await ctx.send(f'YOU LOOSE!!! MY NUMBER WAS {number}')
      except asyncio.TimeoutError:
        await ctx.send(f'Game ended with no response, my number was {number}')

def setup(client):
  client.add_cog(Birthday(client))