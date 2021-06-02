import discord 
import os 
from discord.ext import commands 
from pymongo import MongoClient

conn = MongoClient(os.environ.get("mongo_key"))
db = conn["Falc"]

blacklist = db["blacklist"]

class Blacklist(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def block(self, ctx, user: discord.User = None):
        if user == None:
            await ctx.send("Please enter a user.")
        realUser = blacklist.find_one({"_id": user.id})
        if realUser == None:
            blacklist.insert_one(
                {
                    "_id": user.id
                }
            )
            await ctx.send(f"{user.mention} ({user.id}) can now no longer use any commands.")
        else:
            await ctx.send(f"This user is already in the database, please try again.")

    @commands.command()
    @commands.is_owner()
    async def unblock(self, ctx, user: discord.User = None):
        if user == None:
            await ctx.send("Please enter a user.")
        realUser = blacklist.find_one({"_id": user.id})
        if realUser != None:
            blacklist.delete_one(
                {
                    "_id": user.id
                }
            )
            await ctx.send(f"{user.mention} ({user.id}) can now use all the commands.")
        else:
            await ctx.send(f"This user isn't in the database, please try again.")


def setup(client):
    client.add_cog(Blacklist(client))