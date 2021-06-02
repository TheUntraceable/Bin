import discord
from discord.ext import commands
from prsaw import RandomStuff

api_key = 'LyQw1aCdSQcL' #Get an API Key at https://api-info.pgamerx.com/register.html/ for free
rs = RandomStuff(async_mode=True, api_key=api_key)

class ai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['chatbot', 'chat', 'talk'])
    async def ai(self, ctx,*,message):
        async with ctx.typing():
            response = await rs.get_ai_response(message)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(ai(bot))