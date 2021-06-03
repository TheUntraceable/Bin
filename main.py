
import discord
from discord.ext import commands
import random
import json
import os
import asyncio
from discord_slash import SlashCommand
from datetime import datetime
import requests
import asyncpg
from dotenv import load_dotenv

load_dotenv()

async def get_prefix(client, message):
    # with open('prefixes.json', 'r') as f:
    #     prefixes = json.load(f)

    # return prefixes[str(message.guild.id)]
    getprefix = await client.db.fetchval("SELECT prefix FROM prefixes WHERE id = $1", message.guild.id)
    if getprefix:
        prefix = getprefix.split(",")
    else:
        prefix = "f!"
    print(prefix)
    return prefix

intents = discord.Intents().all()
client = commands.Bot(command_prefix=get_prefix, intents=intents, case_insensitive=True)
client.remove_command("help")
slash = SlashCommand(client, sync_commands=True)

client.bot = client

async def connectPostgres():
    client.db = await asyncpg.create_pool(os.environ.get("PG_URL"),min_size=5,max_size=5)
    print("connected to DB")
    await client.db.execute("CREATE TABLE IF NOT EXISTS prefixes(id bigint PRIMARY KEY,prefix text)")
    # await client.db.execute("DROP TABLE rrole")
    await client.db.execute("CREATE TABLE IF NOT EXISTS rrole(message_id bigint PRIMARY KEY,list_needed text)")
    await client.db.execute("CREATE TABLE IF NOT EXISTS birthday(member_id bigint PRIMARY KEY,info text)")
    await client.db.execute("CREATE TABLE IF NOT EXISTS tickets(guild_id bigint PRIMARY KEY, channel_id bigint, role_id bigint)")
client.loop.create_task(connectPostgres())

@client.event
async def on_guild_join(guild):
    check = await client.db.fetchrow("SELECT id FROM prefixes WHERE id=$1", guild.id)
    if not check:
        await client.db.execute("INSERT INTO prefixes (id, prefix) VALUES ($1,$2)",guild.id,'f!')
    # with open('prefixes.json', 'r') as f:
    #     prefixes = json.load(f)

    # prefixes[str(guild.id)] = 'f!'

    # with open('prefixes.json', 'w') as f:
    #     json.dump(prefixes, f, indent=4)

@slash.slash(name="pfp", description="Displays your pfp")
async def pfp(ctx):
    embed = discord.Embed(
        title=f"{ctx.author.display_name}'s Avatar",
        color=discord.Color.teal()
    ).set_image(url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

user_id="790525985266597918"

@client.event
async def on_message(message):
  mentions = message.mentions

  # with open("prefixes.json", "r") as f:
  #   prefixes = json.load(f)
  #
  # if str(message.guild.id) not in prefixes:
  #   prefixes[str(message.guild.id)] = 'f!'
  #   with open("prefixes.json", "w") as f:
  #     json.dump(prefixes, f, indent=4)
  #
  # pre = prefixes[str(message.guild.id)]
  pre = await client.db.fetchval("SELECT prefix FROM prefixes WHERE id = $1", message.guild.id) or "f!"
  if message.content in (f"<@{user_id}>", f"<@!{user_id}>"):
    if (message.author.bot):
      return
    else:
      embed = discord.Embed(title=f"Need some help?", description= f"Use the following for help:\n`{pre}help`\nThe prefix for this server is:\n`{pre}`\nIf you would like to change the prefix, use `{pre}setprefix <prefix>`",
      color=discord.Colour.blue())
      await message.channel.send(embed=embed)


  try:
    # if message.mentions[0] == client.user:
    #   with open("prefixes.json", "r") as f:
    #     prefixes = json.load(f)

    #   pre = prefixes[str(message.guild.id)]
    pre = await client.db.fetchval("SELECT prefix FROM prefixes WHERE id = $1", message.guild.id) or "f!"
  except:
    pass

  await client.process_commands(message)


@slash.slash(name="flip", description="Flip a coin")
async def _flip(ctx):
    responses = ['Tails','Heads']
    responses = random.choice(responses)
    await ctx.send(f"🪙 **{ctx.author.name}** flipped a coin and got **{responses}**!")

@slash.slash(name="8ball", description="Ask me a question and get an answer from the ball of wisdom")
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.",
        "My reply is no.", "My sources say no.", "Outlook not so good.",
        "Very doubtful."
    ]
    await ctx.send(
        f':8ball:Question: `{question}`\n:8ball:Answer: {random.choice(responses)}'
    )

@slash.slash(name="rate", description="Rate something")
async def _rate(ctx, *, thing: commands.clean_content):
    rate_amount = random.uniform(0.0, 100.0)
    await ctx.send(f"I'd rate `{thing}` a **{round(rate_amount, 4)} / 100**")


@slash.slash(name="cat", description="Get a cute cat picture")
async def _cat(ctx):
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()

    cat_em = discord.Embed(title=':cat: Meow',colour=discord.Colour.blue())
    cat_em.set_image(url=f'{r[0]["url"]}')

    await ctx.send(embed=cat_em)

@slash.slash(name="dog", description="Get an adorable dog picture")
async def _dog(ctx):
    r = requests.get("https://api.thedogapi.com/v1/images/search").json()

    cat_em = discord.Embed(title=':dog: Woof',colour=discord.Colour.blue())
    cat_em.set_image(url=f'{r[0]["url"]}')

    await ctx.send(embed=cat_em)


@slash.slash(name="panda", description="Get an super cute panda picture")
async def _panda(ctx):
    r = requests.get("https://some-random-api.ml/img/panda").json()

    cat_em = discord.Embed(title=':panda_face: aww',colour=discord.Colour.blue())
    cat_em.set_image(url=f'{r[0]["url"]}')

    await ctx.send(embed=cat_em)

@slash.slash(name="meme", description="Get a dank meme")
async def _meme(ctx):
    value = random.randint(1, 2000)
    embed = discord.Embed(title = "Dank Meme", description = "LMAO", colour = 0x329999)
    embed.set_image(url = f"https://ctk-api.herokuapp.com/meme/{value}")
    await ctx.send(embed=embed)

@slash.slash(name="fox", description="Get a fox picture")
async def _fox(ctx):
    r = requests.get("https://some-random-api.ml/img/fox").json()

    cat_em = discord.Embed(title='fox: what a cute fox!', colour=discord.Colour.blue())
    cat_em.set_image(url=f'{r[0]["link"]}')

    await ctx.send(embed=cat_em)

@client.event
async def on_guild_remove(guild):
    # with open('prefixes.json', 'r') as f:
    #   prefixes = json.load(f)

    # prefixes.pop(str(guild.id))

    # with open('prefixes.json', 'w') as f:
    #     json.dump(prefixes, f, indent=4)
    await client.db.execute("DELETE FROM prefixes where id=$1", guild.id)
for fn in os.listdir('./cogs'):
    if fn.endswith('.py') and fn != 'global_functions.py':
        client.load_extension(f'cogs.{fn[:-3]}')


@client.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, ch : discord.TextChannel = None):
    if ch == None:
        await ctx.send('Specify a channel')
        return
    def check(m):
        return m.author == ctx.message.author and m.channel == ctx.message.channel
    await ctx.send('Enter the title:')
    t = await client.wait_for('message', check=check, timeout=60)
    await ctx.send('Enter the message:')
    msg = await client.wait_for('message', check=check, timeout=120)
    embed = discord.Embed(title = t.content, description = msg.content, color = 0xffff)
    embed.set_footer(text=f"{ctx.guild.name}")
    embed.set_author(name=f"{ctx.author}")
    await ch.send(embed = embed)


@client.command()
async def load(ctx, extension):
  id = str(ctx.author.id)
  if id == '489682676157120513':
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Cog loaded')
  else:
    print("stupid kid tryna use me")

@client.command()
async def restart(ctx, extension):
  id = str(ctx.author.id)
  if id == '489682676157120513':
    client.unload_extension(f'cogs.{extension}')
    await asyncio.sleep(1)
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Cog restarted')
  else:
    print("stupid kid tryna use me")

@client.command()
async def unload(ctx, extension):
  id = str(ctx.author.id)
  if id == '489682676157120513':
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Cog unloaded')
  else:
    print("stupid kid tryna use me")

@client.command()
async def check(ctx, cog_name):
  id = str(ctx.author.id)
  if id == '489682676157120513':
    try:
        client.load_extension(f"cogs.{cog_name}")
    except commands.ExtensionAlreadyLoaded:
        await ctx.send("Cog is loaded")
    except commands.ExtensionNotFound:
        await ctx.send("Cog not found")
    else:
        await ctx.send("Cog is unloaded")
        client.unload_extension(f"cogs.{cog_name}")
  else:
    print("stupid kid tryna use me")



client.launch_time = datetime.utcnow()


@client.command(case_insensitive = True, aliases = ["remind", "remindme", "remind_me"])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def reminder(ctx, time, *, reminder):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)
    prefix = await client.db.fetchval("SELECT prefix FROM prefixes WHERE id = $1", ctx.guild.id)
    # prefix = prefixes[str(ctx.guild.id)]
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7)
    embed.set_footer(text=f"Falc", icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='Error, Invalid Duration',
                        value=f'Please use duration in s|m|h|d format.')
    elif seconds < 10:
        embed.add_field(name='Error',
                        value='You have specified a too short duration!\nMinimum duration is 10 seconds.')
    elif seconds > 7776000:
        embed.add_field(name='Error', value='You have specified a too long duration!\nMaximum duration is 90 days.')
    else:
        await ctx.send(f"Alright, I will remind you about `{reminder}` in {counter}.")
        await asyncio.sleep(seconds)
        await ctx.send(f"Hey there {ctx.author.mention}, you asked me to remind you about `{reminder}` {counter} ago.")
        return
    await ctx.send(embed=embed)

@reminder.error
async def reminder_error(ctx, error):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]
  if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title='❌Error, missing required arguments:', description=f'{prefix}remind [Duration] [Reminder]', colour=discord.Colour.red())
        embed.add_field(name='Example:',value=f'{prefix}remind 10h play games')
        await ctx.send(embed=embed)

# @client.event
# async def on_guild_remove(guild):
#     with open('prefixes.json', 'r') as f:
#         prefixes = json.load(f)

#     prefixes.pop(str(guild.id))

#     with open('prefixes.json', 'w') as f:
#         json.dump(prefixes, f, indent=4)

#@client.listen('on_message')
#async def f(message):
#
#    if message.author == client.user:
#        return
#
#    if message.content == "f":
#        await message.channel.send("f")
#    elif message.content =="im":
#        await message.channel.send("Hi! im dad!")
#    elif message.content =="glowstikk":
#        await message.channel.send("glow the dummy")

@client.listen('on_message')
async def ninenine(message):

    if message.author == client.user:
        return
    brooklyn_99_quotes = [
        'Im the human form of the 💯 emoji.',
        'B\'mngpot!',
        'Hello, unsolved case. Do you bring me joy? No, because you’re boring and you’re too hard. See ya.',
        'I dont want to hang out with some stupid baby whos never met Jake.',
        'Fine but in protest Im walking over there extremely slowly!',
        'Title of your sex tape.',
        'Sarge, with all due respect, I am gonna completely ignore everything you just said.',
        'The English language can not fully capture the depth and complexity of my thoughts, so I’m incorporating emojis into my speech to better express myself. Winky face.',
        'Captain Wuntch, good to see you. But if you’re here, who’s guarding Hades?',
        'Captain? The kids want to know where Paulie the Pigeon is. I told them he got sucked up into an airplane engine. Is that all right?',
        ('Cool. Cool cool cool cool cool cool cool, '
        'no doubt no doubt no doubt no doubt.'),
    ]

    if message.content == 'ninenine':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

@client.command(case_insensitive=True,
                aliases=['suggestion'],
                brief=" | Write your suggestions for the server here")
async def suggest(ctx, *, question=None):
    if question == None:
        await ctx.send('Please write a suggestion!')
    else:
        member = ctx.author
        embed = discord.Embed(title="New Suggestion!",
                              description=f"{question}")
        embed.set_footer(text=f"Suggested by {member.mention}")
        embed.timestamp = datetime.utcnow()

        await client.get_channel(831057920019136563).send(embed=embed)

@client.command(aliases=['quit'])
async def shutdown(ctx):
    id = str(ctx.author.id)
    if id == '489682676157120513':
        await ctx.send('Shutting down the bot!')
        await ctx.bot.logout()
    else:
        await ctx.send(
            "You dont have sufficient permissions to perform this action!")





bot = commands.Bot(command_prefix="f!")


def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]




@client.command()
async def dm(ctx, member: discord.Member = None, *, text: str = ""):
  id = str(ctx.author.id)
  if id == '489682676157120513':
    await member.send(f"{text}")
    await ctx.channel.purge(limit=1)
  else:
    await ctx.send("Imagine thinking that this was an actual command")

@client.event
async def on_ready():
  servers = list(client.guilds)
  users= list(client.users)
  #{len(set(client.get_all_members()))}
  await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name=f"f!help | {str(len(users))} members in {str(len(servers))} servers" ))
  print("READY")

#@client.command(aliases= ["afkset", "setafk"])
#@commands.cooldown(1, 21, commands.BucketType.user)
#@commands.has_permissions(embed_links=True)
#async def afk(ctx, mins: convert, *, reason):
#    current_nick = ctx.author.nick
#    await ctx.message.delete()
#    afk1= discord.Embed(title= ":zzz: MEMBER AFK!", description= f"{ctx.author.mention} HAS GONE AFK!", color = #ctx.author.color)
#    afk1.set_thumbnail(url= ctx.author.avatar_url)
#    afk1.add_field(name= "FOR TIME BEING:", value= f"{mins} MINUTES")
#    afk1.add_field(name= "AFK NOTE:", value= f"{reason}")
#    afk1.set_footer(icon_url= ctx.guild.icon_url, text= f"Falc")
#    await ctx.send(embed=afk1)
#    await ctx.author.edit(nick=f"[AFK] {ctx.author.nick}")
#
#    counter = 0
#    while counter <= int(mins):
#        counter += 1
#        await asyncio.sleep(60)
#
#        if counter == int(mins):
#            await ctx.author.edit(nick=current_nick)
#
#            afk2= discord.Embed(title= ":wave: MEMBER NO LONGER AFK!", description= f"{ctx.author.mention} IS NO #LONGER AFK!", color = ctx.author.color)
#            afk2.set_thumbnail(url= ctx.author.avatar_url)
#            afk2.set_footer(icon_url= ctx.guild.icon_url, text= f"Brought to you by Falc!")
#            await ctx.send(embed=afk2)
#            break
#
#@client.command(aliases= ["afkremove", "removeafk"])
#@commands.has_permissions(embed_links=True)
#async def afkoff(ctx):
#    await ctx.message.delete()
#
#    afk= discord.Embed(title= ":wave: MEMBER NO LONGER AFK!", description= f"{ctx.author.mention} IS NO LONGER AFK!", #color = ctx.author.color)
#    afk.set_thumbnail(url= ctx.author.avatar_url)
#    afk.set_footer(icon_url= ctx.guild.icon_url, text= f"f!vote :)")
#
#    await ctx.send(embed=afk)
#    await ctx.author.edit(nick=f"{ctx.author.name}")
#
#    await ctx.send(embed=afk)
#    await ctx.author.edit(nick=f"{ctx.author.name}")

@slash.slash(name="ping", description= "Shows the bots ping")
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

@client.command()
async def face(ctx):
  FACES=[
    "¢‿¢",
    "©¿© o",
    "ª{•̃̾_•̃̾}ª",
    "¬_¬",
    "¯＼(º_o)/¯",
    "¯\\(º o)/¯",
    "¯\\_(⊙︿⊙)_/¯",
    "¯\\_(ツ)_/¯",
    "°ω°",
    "°Д°",
    "°‿‿°",
    "°ﺑ°",
    "´ ▽ ` )ﾉ",
    "¿ⓧ_ⓧﮌ",
    "Ò,ó",
    "ó‿ó",
    "ô⌐ô",
    "ôヮô",
    "ŎםŎ",
    "ŏﺡó",
    "ʕ•̫͡•ʔ",
    "ʕ•ᴥ•ʔ",
    "ʘ‿ʘ",
    "˚•_•˚",
    "˚⌇˚",
    "˚▱˚",
    "̿ ̿̿'̿'\\̵͇̿̿\\=(•̪●)=/̵͇̿̿/'̿̿ ̿ ̿ ̿",
    "͡° ͜ʖ ͡°",
    "Σ ◕ ◡ ◕",
    "Σ (ﾟДﾟ;)",
    "Σ(ﾟДﾟ；≡；ﾟдﾟ)",
    "Σ(ﾟДﾟ )",
    "Σ(||ﾟДﾟ)",
    "Φ,Φ",
    "δﺡό",
    "σ_σ",
    "д_д",
    "ф_ф",
    "щ（ﾟДﾟщ）",
    "щ(ಠ益ಠщ)",
    "щ(ಥДಥщ)",
    "Ծ_Ծ",
    "أ‿أ",
    "ب_ب",
    "ح˚௰˚づ",
    "ح˚ᆺ˚ว",
    "حᇂﮌᇂ)",
    "٩๏̯͡๏۶",
    "٩๏̯͡๏)۶",
    "٩◔̯◔۶",
    "٩(×̯×)۶",
    "٩(̾●̮̮̃̾•̃̾)۶",
    "٩(͡๏̯͡๏)۶",
    "٩(͡๏̯ ͡๏)۶",
    "٩(ಥ_ಥ)۶",
    "٩(•̮̮̃•̃)۶",
    "٩(●̮̮̃•̃)۶",
    "٩(●̮̮̃●̃)۶",
    "٩(｡͡•‿•｡)۶",
    "٩(-̮̮̃•̃)۶",
    "٩(-̮̮̃-̃)۶",
    "۞_۞",
    "۞_۟۞",
    "۹ↁﮌↁ",
    "۹⌤_⌤۹",
    "॓_॔",
    "१✌◡✌५",
    "१|˚–˚|५",
    "ਉ_ਉ",
    "ଘ_ଘ",
    "இ_இ",
    "ఠ_ఠ",
    "రృర",
    "ಠ¿ಠi",
    "ಠ‿ಠ",
    "ಠ⌣ಠ",
    "ಠ╭╮ಠ",
    "ಠ▃ಠ",
    "ಠ◡ಠ",
    "ಠ益ಠ",
    "ಠ益ಠ",
    "ಠ︵ಠ凸",
    "ಠ , ಥ",
    "ಠ.ಠ",
    "ಠoಠ",
    "ಠ_ృ",
    "ಠ_ಠ",
    "ಠ_๏",
    "ಠ~ಠ",
    "ಡ_ಡ",
    "ತಎತ",
    "ತ_ತ",
    "ಥдಥ",
    "ಥ‿ಥ",
    "ಥ⌣ಥ",
    "ಥ◡ಥ",
    "ಥ﹏ಥ",
    "ಥ_ಥ",
    "ಭ_ಭ",
    "ರ_ರ",
    "ಸ , ໖",
    "ಸ_ಸ",
    "ക_ക",
    "อ้_อ้",
    "อ_อ",
    "โ๏௰๏ใ ื",
    "๏̯͡๏﴿",
    "๏̯͡๏",
    "๏̯͡๏﴿",
    "๏[-ิิ_•ิ]๏",
    "๏_๏",
    "໖_໖",
    "༺‿༻",
    "ლ(´ڡ`ლ)",
    "ლ(́◉◞౪◟◉‵ლ)",
    "ლ(ಠ益ಠლ)",
    "ლ(╹◡╹ლ)",
    "ლ(◉◞౪◟◉‵ლ)",
    "ლ,ᔑ•ﺪ͟͠•ᔐ.ლ",
    "ᄽὁȍ ̪ őὀᄿ",
    "ᕕ( ᐛ )ᕗ",
    "ᕙ(⇀‸↼‶)ᕗ",
    "ᕦ(ò_óˇ)ᕤ",
    "ᶘ ᵒᴥᵒᶅ",
    "‘︿’",
    "•▱•",
    "•✞_✞•",
    "•ﺑ•",
    "•(⌚_⌚)•",
    "•_•)",
    "‷̗ↂ凸ↂ‴̖",
    "‹•.•›",
    "‹› ‹(•¿•)› ‹›",
    "‹(ᵒᴥᵒ­­­­­)›",
    "‹(•¿•)›",
    "ↁ_ↁ",
    "⇎_⇎",
    "∩(︶▽︶)∩",
    "∩( ・ω・)∩",
    "≖‿≖",
    "≧ヮ≦",
    "⊂•⊃_⊂•⊃",
    "⊂⌒~⊃｡Д｡)⊃",
    "⊂(◉‿◉)つ",
    "⊂(ﾟДﾟ,,⊂⌒｀つ",
    "⊙ω⊙",
    "⊙▂⊙",
    "⊙▃⊙",
    "⊙△⊙",
    "⊙︿⊙",
    "⊙﹏⊙",
    "⊙０⊙",
    "⊛ठ̯⊛",
    "⋋ō_ō`",
    "━━━ヽ(ヽ(ﾟヽ(ﾟ∀ヽ(ﾟ∀ﾟヽ(ﾟ∀ﾟ)ﾉﾟ∀ﾟ)ﾉ∀ﾟ)ﾉﾟ)ﾉ)ﾉ━━━",
    "┌∩┐(◕_◕)┌∩┐",
    "┌( ಠ_ಠ)┘",
    "┌( ಥ_ಥ)┘",
    "╚(•⌂•)╝",
    "╭╮╭╮☜{•̃̾_•̃̾}☞╭╮╭╮",
    "╭✬⌢✬╮",
    "╮(─▽─)╭",
    "╯‵Д′)╯彡┻━┻",
    "╰☆╮",
    "□_□",
    "►_◄",
    "◃┆◉◡◉┆▷",
    "◉△◉",
    "◉︵◉",
    "◉_◉",
    "○_○",
    "●¿●\\ ~",
    "●_●",
    "◔̯◔",
    "◔ᴗ◔",
    "◔ ⌣ ◔",
    "◔_◔",
    "◕ω◕",
    "◕‿◕",
    "◕◡◕",
    "◕ ◡ ◕",
    "◖♪_♪|◗",
    "◖|◔◡◉|◗",
    "◘_◘",
    "◙‿◙",
    "◜㍕◝",
    "◪_◪",
    "◮_◮",
    "☁ ☝ˆ~ˆ☂",
    "☆¸☆",
    "☉‿⊙",
    "☉_☉",
    "☐_☐",
    "☜ق❂Ⴢ❂ق☞",
    "☜(⌒▽⌒)☞",
    "☜(ﾟヮﾟ☜)",
    "☜-(ΘLΘ)-☞",
    "☝☞✌",
    "☮▁▂▃▄☾ ♛ ◡ ♛ ☽▄▃▂▁☮",
    "☹_☹",
    "☻_☻",
    "☼.☼",
    "☾˙❀‿❀˙☽",
    "♀ح♀ヾ",
    "♥‿♥",
    "♥╣[-_-]╠♥",
    "♥╭╮♥",
    "♥◡♥",
    "✌♫♪˙❤‿❤˙♫♪✌",
    "✌.ʕʘ‿ʘʔ.✌",
    "✌.|•͡˘‿•͡˘|.✌",
    "✖‿✖",
    "✖_✖",
    "❐‿❑",
    "⨀_⨀",
    "⨀_Ꙩ",
    "⨂_⨂",
    "〆(・∀・＠)",
    "《〠_〠》",
    "【•】_【•】",
    "〠_〠",
    "〴⋋_⋌〵",
    "の� �の",
    "ニガー? ━━━━━━(ﾟ∀ﾟ)━━━━━━ ニガー?",
    "ペ㍕˚\\",
    "ヽ(´ｰ｀ )ﾉ",
    "ヽ(๏∀๏ )ﾉ",
    "ヽ(｀Д´)ﾉ",
    "ヽ(ｏ`皿′ｏ)ﾉ",
    "ヽ(`Д´)ﾉ",
    "ㅎ_ㅎ",
    "乂◜◬◝乂",
    "凸ಠ益ಠ)凸",
    "句_句",
    "Ꙩ⌵Ꙩ",
    "Ꙩ_Ꙩ",
    "ꙩ_ꙩ",
    "Ꙫ_Ꙫ",
    "ꙫ_ꙫ",
    "ꙮ_ꙮ",
    "흫_흫",
    "句_句",
    "﴾͡๏̯͡๏﴿ O'RLY?",
    "¯\\(ºдಠ)/¯",
    "（·×·）",
    "（⌒Д⌒）",
    "（╹ェ╹）",
    "（♯・∀・）⊃",
    "（　´∀｀）☆",
    "（　´∀｀）",
    "（゜Д゜）",
    "（・∀・）",
    "（・Ａ・）",
    "（ﾟ∀ﾟ）",
    "（￣へ￣）",
    "（ ´☣///_ゝ///☣｀）",
    "（ つ Д ｀）",
    "＿☆（ ´_⊃｀）☆＿",
    "｡◕‿‿◕｡",
    "｡◕ ‿ ◕｡",
    "!⑈ˆ~ˆ!⑈",
    "!(｀･ω･｡)",
    "(¬‿¬)",
    "(¬▂¬)",
    "(¬_¬)",
    "(°ℇ °)",
    "(°∀°)",
    "(´ω｀)",
    "(´◉◞౪◟◉)",
    "(´ヘ｀;)",
    "(´・ω・｀)",
    "(´ー｀)",
    "(ʘ‿ʘ)",
    "(ʘ_ʘ)",
    "(˚இ˚)",
    "(͡๏̯͡๏)",
    "(ΘεΘ;)",
    "(ι´Д｀)ﾉ",
    "(Ծ‸ Ծ)",
    "(॓_॔)",
    "(० ्०)",
    "(ு८ு_ .:)",
    "(ಠ‾ಠ)",
    "(ಠ‿ʘ)",
    "(ಠ‿ಠ)",
    "(ಠ⌣ಠ)",
    "(ಠ益ಠ ╬)",
    "(ಠ益ಠ)",
    "(ಠ_ృ)",
    "(ಠ_ಠ)",
    "(ಥ﹏ಥ)",
    "(ಥ_ಥ)",
    "(๏̯͡๏ )",
    "(ღ˘⌣˘ღ) ♫･*:.｡. .｡.:*･",
    "(ღ˘⌣˘ღ)",
    "(ᵔᴥᵔ)",
    "(•ω•)",
    "(•‿•)",
    "(•⊙ω⊙•)",
    "(• ε •)",
    "(∩▂∩)",
    "(∩︵∩)",
    "(∪ ◡ ∪)",
    "(≧ω≦)",
    "(≧◡≦)",
    "(≧ロ≦)",
    "(⊙ヮ⊙)",
    "(⊙_◎)",
    "(⋋▂⋌)",
    "(⌐■_■)",
    "(─‿‿─)",
    "(┛◉Д◉)┛┻━┻",
    "(╥_╥)",
    "(╬ಠ益ಠ)",
    "(╬◣д◢)",
    "(╬ ಠ益ಠ)",
    "(╯°□°）╯︵ ┻━┻",
    "(╯ಊ╰)",
    "(╯◕_◕)╯",
    "(╯︵╰,)",
    "(╯3╰)",
    "(╯_╰)",
    "(╹◡╹)凸",
    "(▰˘◡˘▰)",
    "(●´ω｀●)",
    "(●´∀｀●)",
    "(◑‿◐)",
    "(◑◡◑)",
    "(◕‿◕✿)",
    "(◕‿◕)",
    "(◕‿-)",
    "(◕︵◕)",
    "(◕ ^ ◕)",
    "(◕_◕)",
    "(◜௰◝)",
    "(◡‿◡✿)",
    "(◣_◢)",
    "(☞ﾟ∀ﾟ)☞",
    "(☞ﾟヮﾟ)☞",
    "(☞ﾟ ∀ﾟ )☞",
    "(☼◡☼)",
    "(☼_☼)",
    "(✌ﾟ∀ﾟ)☞",
    "(✖╭╮✖)",
    "(✪㉨✪)",
    "(✿◠‿◠)",
    "(✿ ♥‿♥)",
    "(　・∀・)",
    "(　･ัω･ั)？",
    "(　ﾟ∀ﾟ)o彡゜えーりんえーりん!!",
    "(。・_・。)",
    "(つд｀)",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ益ಠ)ノ彡┻━┻",
    "(ノ ◑‿◑)ノ",
    "(ノ_・。)",
    "(・∀・ )",
    "(屮ﾟДﾟ)屮",
    "(︶ω︶)",
    "(︶︹︺)",
    "(ﺧ益ﺨ)",
    "(；一_一)",
    "(｀・ω・´)”",
    "(｡◕‿‿◕｡)",
    "(｡◕‿◕｡)",
    "(｡◕ ‿ ◕｡)",
    "(｡♥‿♥｡)",
    "(｡･ω..･)っ",
    "(･ｪ-)",
    "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
    "(ﾟДﾟ)",
    "(ﾟДﾟ)y─┛~~",
    "(ﾟ∀ﾟ)",
    "(ﾟヮﾟ)",
    "(￣□￣)",
    "(￣。￣)",
    "(￣ー￣)",
    "(￣(エ)￣)",
    "( °٢° )",
    "( ´_ゝ｀)",
    "( ͡° ͜ʖ ͡°)",
    "( ͡~ ͜ʖ ͡°)",
    "( ಠ◡ಠ )",
    "( •_•)>⌐■-■",
    "( 　ﾟ,_ゝﾟ)",
    "( ･ิз･ิ)",
    "( ﾟдﾟ)､",
    "( ^▽^)σ)~O~)",
    "((((゜д゜;))))",
    "(*´д｀*)",
    "(*..Д｀)",
    "(*..д｀*)",
    "(*~▽~)",
    "(-’๏_๏’-)",
    "(-＿- )ノ",
    "(/◔ ◡ ◔)/",
    "(///_ಥ)",
    "(;´Д`)",
    "(=ω=;)",
    "(=゜ω゜)",
    "(>'o')>♥<('o'<)",
    "(n˘v˘•)¬",
    "(o´ω｀o)",
    "(V)(°,,°)(V)",
    "(\/) (°,,°) (\/) WOOPwoopwowopwoopwoopwoop!",
    "(^▽^)",
    "(`･ω･´)",
    "(~￣▽￣)~",
    "/╲/\\╭ºoꍘoº╮/\\╱\\",
    "<【☯】‿【☯】>",
    "= (ﾟдﾟ)ｳ",
    "@_@",
    "d(*⌒▽⌒*)b",
    "o(≧∀≦)o",
    "o(≧o≦)o",
    "q(❂‿❂)p",
    "y=ｰ( ﾟдﾟ)･∵.",
    "\\˚ㄥ˚\\",
    "\\ᇂ_ᇂ\\",
    "\\(ಠ ὡ ಠ )/",
    "\\(◕ ◡ ◕\\)",
    "^̮^",
    "^ㅂ^",
    "_(͡๏̯͡๏)_",
    "{´◕ ◡ ◕｀}",
    "{ಠ_ಠ}__,,|,",
    "{◕ ◡ ◕}",
  ]
  FACE=random.choice(FACES)
  await ctx.send(FACE)

@client.command()
async def rps(ctx):
    try:
        await ctx.message.delete()
        rpsEmbed = discord.Embed(color=random.randint(
            0, 0xffffff))
        rpsEmbed.add_field(name='Rock', value='\U0001faa8')
        rpsEmbed.add_field(name='Paper', value='\U0001f4dc')
        rpsEmbed.add_field(name='Scissors', value='\U00002702')
        rpsEmbed.set_footer(text='The message will be deleted after 1 minute')
        question_choose = await ctx.send(embed=rpsEmbed)
        await question_choose.add_reaction('\U0001faa8')
        await question_choose.add_reaction('\U0001f4dc')
        await question_choose.add_reaction('\U00002702')
        reaction, user = await client.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and str(reaction.emoji), timeout=60)
        # list of selects 1# scissors 2# rock 3# paper
        selects = [u'\U00002702', u'\U0001faa8', u'\U0001f4dc']
        # choose random sleects from the list
        bot_select = random.choice(selects)
        print(str(bot_select))
        # save the emoji like a var
        user_select = str(reaction.emoji)
        print(str(user_select))
    # if the bot select equal user select its mean is a Tie
        if str(user_select) == str(bot_select):
            await question_choose.delete()
            # change the string select to a emoji
            if str(bot_select) == u'\U00002702':
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{bot_select}**', inline=True)
                choose_embed.set_author(
                    name='Tie!', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=choose_embed)
            # same
            elif str(bot_select) == u'\U0001faa8':
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{bot_select}**', inline=True)
                choose_embed.set_author(
                    name='Tie!', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=choose_embed)
            # same
            elif str(bot_select) == u'\U0001f4dc':
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{bot_select}**', inline=True)
                choose_embed.set_author(
                    name='Tie!', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=choose_embed)
        # if user_select is rock and check if the bot_select
        elif str(user_select) == u'\U0001faa8':
            await question_choose.delete()
            if str(bot_select) == u'\U00002702':
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{bot_select}**', inline=True)
                choose_embed.set_author(
                    name='You Win!', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=choose_embed)
            elif str(bot_select) == u'\U0001f4dc':
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{bot_select}**', inline=True)
                choose_embed.set_author(
                    name='You Lose!', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=choose_embed)
        elif str(user_select) == u'\U0001f4dc':
            await question_choose.delete()
            if str(bot_select) == u'\U0001faa8':
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{bot_select}**', inline=True)
                choose_embed.set_author(
                    name='You Win!', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=choose_embed)
            elif str(bot_select) == u'\U00002702':
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{bot_select}**', inline=True)
                choose_embed.set_author(
                    name='You Lose!', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=choose_embed)
        elif str(user_select) == u'\U00002702':
            await question_choose.delete()
            if str(bot_select) == u'\U0001faa8':
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{bot_select}**', inline=True)
                choose_embed.set_author(
                    name='You Lose!', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=choose_embed)
            elif str(bot_select) == u'\U0001f4dc':
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{bot_select}**', inline=True)
                choose_embed.set_author(
                    name='You Win!', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=choose_embed)
    except asyncio.TimeoutError:
        await question_choose.delete()
        timeout = await ctx.send('Lucky for you I was made for my time to be wasted. Next time **respond**')
        await timeout.delete(delay=10)

@client.command(aliases=['flip', 'flipping'])
async def flip_command(ctx):
    try:
        cancel = False
        await ctx.message.delete()
        EmbedHead = discord.Embed(
            description='What you choose? (Heads/Tails)', color=random.randint(0, 0xffffff))
        EmbedHead.set_footer(text='You have 1 minute to choose!')
        headORtail = await ctx.send(embed=EmbedHead)
        message = await client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=60)
        if str(message.content.lower()) == 'heads':
            user_choose = message.content
            await message.delete()
            fliping = await ctx.send(f'Flipping. ')
            await asyncio.sleep(1)
            await fliping.edit(content=f'Flipping.. ')
            await asyncio.sleep(1)
            await fliping.edit(content=f'Flipping... ')
            chooses = ['heads', 'tails']
            random_select = random.choice(chooses)
            await fliping.delete()
            if user_choose == random_select:
                await headORtail.delete()
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_choose}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{random_select}**', inline=True)
                choose_embed.set_author(
                    name='You Win!', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                await ctx.send(embed=choose_embed)
            else:
                await headORtail.delete()
                choose_embed = discord.Embed(color=0xe74c3c)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_choose}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{random_select}**', inline=True)
                choose_embed.set_author(
                    name='You Lose!', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                await ctx.send(embed=choose_embed)
        if str(message.content.lower()) == 'tails':
            user_choose = message.content
            await message.delete()
            fliping = await ctx.send(f'Flipping. ')
            await asyncio.sleep(1)
            await fliping.edit(content=f'Flipping.. ')
            await asyncio.sleep(1)
            await fliping.edit(content=f'Flipping... ')
            chooses = ['heads', 'tails']
            random_select = random.choice(chooses)
            await fliping.delete()
            if user_choose == random_select:
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_choose}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{random_select}**', inline=True)
                choose_embed.set_author(
                    name='You Win!', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.icon_url)
                await ctx.send(embed=choose_embed)
            else:
                choose_embed = discord.Embed(color=0xe74c3c)
                choose_embed.add_field(
                    name='You Chose :bust_in_silhouette:', value=f'**{user_choose}**', inline=True)
                choose_embed.add_field(
                    name='Falc Chose :robot:', value=f'**{random_select}**', inline=True)
                choose_embed.set_author(
                    name='You Lose!', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.icon_url)
                await ctx.send(embed=choose_embed)
        else:
            try:
                cancel = True
                await headORtail.delete()
                temp_message = await ctx.send('You flip a coin not your mum. Choose **HEADS or TAILS**')
                await temp_message.delete(delay=2)
            except:
                pass
    except asyncio.TimeoutError:
        if not cancel:
            await headORtail.edit(content='Lucky for you I was made for my time to be wasted. Next time **respond**')

#@client.event
#async def on_command_error(ctx, error):
 #   if isinstance(error, commands.MissingPermissions):
  #    embed = discord.Embed(title="Invalid Permisssions!", description="Please make sure you have perms", c#olour=discord.Colour.blue())
    #  await ctx.send(embed=embed)


@client.command(aliases=["pfp"])
async def avatar(ctx):
    embed = discord.Embed(
        title=f"{ctx.author.display_name}'s Avatar",
        color=discord.Color.teal()
    ).set_image(url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

@client.command()
async def truth(ctx):
	truth = ['What are your top three turn-ons?',
			'What is your darkest fear?',
			'Tell me about your first kiss.',
			'Who is the sexiest person here?',
			'What is your biggest regret?',
			'Who is your crush among yourselves?',
			'Tell me about your most awkward date.',
			'When was the last time you peed in bed?',
			'What is the biggest lie you have ever told?',
			'What do most people think is true about you, but isn’t?',
			'What is the biggest thing you’ve gotten away with?',
			'What would you do if you were the opposite sex for a day?',
			'What is the most expensive thing you have stolen?',
			'What is the most childish thing you still do?',
			'What’s the worst time you let someone take the blame for something you did?',
			'Who here would you most like to make out with?',
			'What is something that people think you would never be into, but you are?',
			'What was the worst encounter you had with a police officer?',
			'What is the silliest thing you have an emotional attachment to?',
			'What is the most embarrassing thing your parents have caught you doing?',
			'What is the scariest dream you have ever had?',
			'What is the most embarrassing thing in your room?',
			'What is the stupidest thing you have ever done?',
			'What terrible thing have you done that you lied to cover up?',
			'Who have you loved but they didn’t love you back?',
			'What are the disgusting habits you have?',
			'What was the cruelest joke you played on someone?',
			'What was the most awkward romantic encounter you have had?',
			'What is the most embarrassing nickname you have ever had?',
			'What is the weirdest thing you have done for a boyfriend or girlfriend?',
			'What do you really hope your parents never find out about?',
			'Tell me something you don’t want me to know.'
			'What’s one thing you’d do if you knew there no consequences?',
			'Have you ever lied about your age?',
			'What celebrity do you think is overrated?',
			'Have you ever regifted a present?',
			'What’s the biggest lie you told, without getting caught?',
			'What is your last photo you took on your phone?',
			'Do you sleep with a blanket or stuffed animal?',
			'If you couldnt go to the college or get the job of your dreams, what would you do?'
			'Any special talents? If so, what?',
			'What is your favorite sport?',
			'What would you want your last meal to be?',
			'What is your favorite food?',
			'What is your favorite game?',
			'What is your favorite song?',
			'Do you follow your heart or your head?',
			'If you could have one super power, what would it be?',
			'Do you recycle?',
			'Do you like to dance or sing?'
			'If you could choose a different career, what would it be and why?']
	await ctx.send(f'{random.choice(truth)}')

@client.command()
async def dare(ctx):
	dare = ['Eat five tablespoons of a condiment.',
		'Be someone’s pet for the next 5 minutes.',
		'Let the group give you a new hairstyle.',
		'Curse like sailor for 20 seconds straight.',
		'Break two eggs on your head.',
		'Take a shower with your clothes on.',
		'Put 4 ice cubes down your pants.',
		'Eat one teaspoon of the spiciest thing you have in the kitchen.',
		'Jump up and down as high as you can go for a full minute.'
		'Spin an imaginary hula hoop around your waist for 3 minutes.',
		'Dance with no music for 1 minute.',
		'Put 2 ice cubes down your pants and/or shirt.',
		'Find something to wear as a cape, and act like a superhero.',
		'Go outside, and run around in a circle, 5 times.',
		'Try to lick your elbow.',
		'Make up a random poem and share it with us.',
		'Crack an egg on your head.',
		'Do the macarena for 2 minutes straight.',
		'Wear all your clothing inside-out for an hour.',
		'Try to do a handstand. (Be careful!!)',
		'Go outside and cut the grass with an invisible mower.',
		'Pick the third number on your contacts list and message them a silly poem.',
		'Wait until a dog walks past your house and bark at it.',
		'Knock on someone’s door and try to run away before they answer.']
	await ctx.send(f'{random.choice(dare)}')

@client.command()
async def wyr(ctx):
	wyr = ['Would you rather the aliens that make first contact be robotic or organic?',
	'Would you rather lose the ability to read or lose the ability to speak?',
	'Would you rather have a golden voice or a silver tongue?',
	'Would you rather be covered in fur or covered in scales?',
	'Would you rather be in jail for a year or lose a year off your life?',
	'Would you rather always be 10 minutes late or always be 20 minutes early?',
	'Would you rather have one real get out of jail free card or a key that opens any door?',
	'Would you rather know the history of every object you touched or be able to talk to animals?',
	'Would you rather be married to a 10 with a bad personality or a 6 with an amazing personality?',
	'Would you rather be able to talk to land animals, animals that fly, or animals that live under the water?',
	'Would you rather have all traffic lights you approach be green or never have to stand in line again?',
	'Would you rather spend the rest of your life with a sailboat as your home or an RV as your home?',
	'Would you rather give up all drinks except for water or give up eating anything that was cooked in an oven?',
	'Would you rather be able to see 10 minutes into your own future or 10 minutes into the future of anyone but yourself?',
	'Would you rather have an easy job working for someone else or work for yourself but work incredibly hard?',
	'Would you rather be the first person to explore a planet or be the inventor of a drug that cures a deadly disease?',
	'Would you rather go back to age 5 with everything you know now or know now everything your future self will learn?',
	'Would you rather be able to control animals (but not humans) with your mind or control electronics with your mind?',
	'Would you rather have unlimited international first-class tickets or never have to pay for food at restaurants?',
	'Would you rather see what was behind every closed door or be able to guess the combination of every safe on the first try?',
	'Would you rather be an average person in the present or a king of a large country 2500 years ago?',
	'Would you rather be able to dodge anything no matter how fast it’s moving or be able to ask any three questions and have them answered accurately?',
	'Would you rather be forced to dance every time you heard music or be forced to sing along to any song you heard?',
	'Would you rather have all your clothes fit perfectly or have the most comfortable pillow, blankets, and sheets in existence?',
	'Would you rather 5% of the population have telepathy, or 5% of the population have telekinesis? You are not part of the 5% that has telepathy or telekinesis.',
	'Would you rather be an unimportant character in the last movie you saw or an unimportant character in the last book you read?',
	'Would you rather move to a new city or town every week or never be able to leave the city or town you were born in?',
	'Would you rather be completely insane and know that you are insane or completely insane and believe you are sane?',
	'Would you rather travel the world for a year on a shoestring budget or stay in only one country for a year but live in luxury?',
	'Would you rather suddenly be elected a senator or suddenly become a CEO of a major company? (You won’t have any more knowledge about how to do either job than you do right now.)',
	'Would you rather live in virtual reality where you are all powerful or live in the real world and be able to go anywhere but not be able to interact with anyone or anything?',
	'Would you rather have whatever you are thinking to appear above your head for everyone to see or have absolutely everything you do live streamed for anyone to see?',
	'Would you rather wake up as a new random person every year and have full control of them for the whole year or once a week spend a day inside a stranger without having any control of them?',
	'Would you rather know how above or below average you are at everything or know how above or below average people are at one skill/talent just by looking at them?',
	'Would you rather every shirt you ever wear be kind of itchy or only be able to use 1 ply toilet paper?']
	await ctx.send(f'{random.choice(wyr)}')

response = requests.post(f'https://space-bot-list.xyz/api/bots/{489682676157120513}', headers = {"Authorization": "942292990d0fe954c70e539429ee8ac6e3cb55100bcfb798acb6b3046120c233f243b2417b6fe49e21303c2cac30860a", "Content-Type": "application/json"})

my_secret = os.environ.get("TOKEN")
client.run(my_secret)