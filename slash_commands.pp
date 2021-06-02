import discord
from discord.ext import commands
from discord_slash import SlashCommand

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) 

guild_ids = [826181428147388487, 763669299889831936, 771670448206381068, 807724505144229899]

@client.event
async def on_ready():
    print("Slasher Ready!")

# avatar
@slash.slash(name="mypfp", description="Displays your pfp", guild_ids=guild_ids)
async def pfp(ctx):

    embed = discord.Embed(
        title=f"{ctx.author.display_name}'s avatar",
        color=discord.Color.teal()
    ).set_image(url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

def setup(bot):
 bot.add_cog(slash(bot))