import discord
from discord.ext import commands
import os
import json
import urllib.request
from errorembed import ErrorEmbed as ee
import datetime

class API(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.animal_facts = ['dog', 'cat', 'panda', 'fox', 'bird', 'koala', 'kangaroo', 'racoon', 'elephant', 'giraffe', 'whale']
    self.animal_images = ['dog', 'cat', 'panda', 'red_panda', 'fox', 'bird', 'koala', 'kangaroo', 'raccoon', 'whale', 'pikachu']

  @commands.command(aliases=['animalfact'])
  async def fact(self, ctx, *, animal = None):
    """Get a random fact about an animal."""
    if animal == None:
      embed = ee.error("Missing Command Arguments", "You need to specify an animal to get a fact about.  Currently you can get facts about a `dog`, `cat`, `panda`, `fox`, `bird`, `koala`, `kangaroo`, `racoon`, `elephant`, `giraffe`, and `whale`.")
      await ctx.send(embed=embed)
    else:
      if animal.lower() not in self.animal_facts:
        embed = ee.error("Missing Command Arguments", "You need to specify an animal to get a fact about.  Currently you can get facts about a `dog`, `cat`, `panda`, `fox`, `bird`, `koala`, `kangaroo`, `racoon`, `elephant`, `giraffe`, and `whale`.")
        await ctx.send(embed=embed)
      else:
        animal = animal.lower()
        url = f"https://some-random-api.ml/facts/{animal}"
        response = urllib.request.urlopen(url).read().decode()
        obj = json.loads(response)

        embed = discord.Embed(
          title = f"Random {animal.title()} Fact",
          description = obj["fact"],
          color = 0x5f10a3,
          timestamp = datetime.datetime.utcnow()
        )
        await ctx.send(embed=embed)

  @commands.command(aliases=['animalimage', 'animimg'])
  async def image(self, ctx, *, animal = None):
    """Get a random animal image."""
    if animal == None:
      embed = ee.error("Missing Command Arguments", "You need to specify an animal to get an image for.  Currently you can get images for a `dog`, `cat`, `panda`, `red_panda`, `fox`, `bird`, `koala`, `kangaroo`, `racoon`, `whale`, and `pikachu`.")
      await ctx.send(embed=embed)
    else:
      if animal.lower() not in self.animal_images:
        embed = ee.error("Missing Command Arguments", "You need to specify an animal to get an image for.  Currently you can get images for a `dog`, `cat`, `panda`, `red_panda`, `fox`, `bird`, `koala`, `kangaroo`, `racoon`, `whale`, and `pikachu`.")
        await ctx.send(embed=embed)
      else:
        animal = animal.lower()
        url = f"https://some-random-api.ml/img/{animal}"
        response = urllib.request.urlopen(url).read().decode()
        obj = json.loads(response)

        embed = discord.Embed(
          title = f"Random {animal.title()} Image",
          description = obj["link"],
          color = 0x5f10a3,
          timestamp = datetime.datetime.utcnow()
        )
        embed.set_image(url=obj["link"])
        await ctx.send(embed=embed)
  
  @commands.command(aliases=['winkgif'])
  async def wink(self, ctx):
    """Get a random winking gif."""
    url = "https://some-random-api.ml/animu/wink"
    response = urllib.request.urlopen(url).read().decode()
    obj = json.loads(response)
    embed = discord.Embed(
      title = "Random Winking Gif",
      description = obj["link"],
      color = 0x5f10a3,
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_image(url=obj["link"])
    await ctx.send(embed=embed)

  @commands.command(aliases=['patgif'])
  async def patt(self, ctx):
    """Get a random patting gif."""
    url = "https://some-random-api.ml/animu/pat"
    response = urllib.request.urlopen(url).read().decode()
    obj = json.loads(response)
    embed = discord.Embed(
      title = "Random Patting Gif",
      description = obj["link"],
      color = 0x5f10a3,
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_image(url=obj["link"])
    await ctx.send(embed=embed)

  @commands.command(aliases=['huggif'])
  async def hugg(self, ctx):
    """Get a random hugging gif."""
    url = "https://some-random-api.ml/animu/pat"
    response = urllib.request.urlopen(url).read().decode()
    obj = json.loads(response)
    embed = discord.Embed(
      title = "Random Hugging Gif",
      description = obj["link"],
      color = 0x5f10a3,
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_image(url=obj["link"])
    await ctx.send(embed=embed)

  @commands.command(aliases=['face-palm'])
  async def facepalm(self, ctx):
    """Get a random face palming gif."""
    url = "https://some-random-api.ml/animu/face-palm"
    response = urllib.request.urlopen(url).read().decode()
    obj = json.loads(response)
    embed = discord.Embed(
      title = "Random Face-Palming Gif",
      description = obj["link"],
      color = 0x5f10a3,
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_image(url=obj["link"])
    await ctx.send(embed=embed)

  @commands.command(aliases=['pokedex', 'poke', 'pokesearch', 'searchpoke', 'pokefilter'])
  async def pokemon(self, ctx, pokemon = None):
    """Search Pokedex for a pokemon and get all of it's stats."""
    if pokemon == None:
      embed = ee.error("Missing Command Arguments", "You need to specify a Pokémon to search for!")
      await ctx.send(embed=embed)
    else:
        url = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
        try:
          response = urllib.request.urlopen(url).read().decode()
        except:
          embed = ee.error("Pokemon Search Failed", "We coudn't find that pokemon!")
          await ctx.send(embed=embed)
          return
        response = urllib.request.urlopen(url).read().decode()
        obj = json.loads(response)
        embed = discord.Embed(
          title = obj["name"].title(),
          description = obj["description"],
          color = 0x5f10a3,
          timestamp = datetime.datetime.utcnow()
        )
        embed.add_field(name="ID", value=obj["id"])
        embed.add_field(name="Type", value=", ".join(obj["type"]))
        embed.add_field(name="Species", value = ", ".join(obj["species"]))
        embed.add_field(name="Abilities", value=", ".join(obj["abilities"]))
        embed.add_field(name="Height", value=obj["height"], inline=False)
        embed.add_field(name="Weight", value=obj["weight"])
        embed.add_field(name="Base Experience", value=obj["base_experience"])
        embed.add_field(name="Gender", value = ", ".join(obj["gender"]))
        embed.add_field(name="Egg Groups", value=", ".join(obj["egg_groups"]), inline=False)
        embed.add_field(name="꧁༺ 𝓢𝓽𝓪𝓽𝓼 ༻꧂", value="◤✞ --------------- ✞◥", inline=False)
        embed.add_field(name="HP", value=obj["stats"]["hp"], inline=False)
        embed.add_field(name="Attack", value=obj["stats"]["attack"])
        embed.add_field(name="Defense", value=obj["stats"]["defense"])
        embed.add_field(name="Special Attack", value=obj["stats"]["sp_atk"])
        embed.add_field(name="Special Defense", value=obj["stats"]["sp_def"])
        embed.add_field(name="Speed", value=obj["stats"]["speed"])
        embed.add_field(name="꧁༺ 𝓕𝓪𝓶𝓲𝓵𝔂 ༻꧂", value="◤✞ ------------------- ✞◥", inline=False)
        embed.add_field(name="Evolution Stage", value=obj["family"]["evolutionStage"], inline=False)
        embed.add_field(name="Pokémon Evolutions", value = ", ".join(obj["family"]["evolutionLine"]) if obj["family"]["evolutionLine"] else None)
        embed.add_field(name="Generation", value=obj["generation"])
        embed.set_thumbnail(url=obj["sprites"]["normal"])
        embed.set_image(url=obj["sprites"]["animated"])
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name = f"Pokemon Information for {pokemon.title()}", icon_url = obj["sprites"]["normal"])
        await ctx.send(embed=embed)

def setup(client):
  client.add_cog(API(client))