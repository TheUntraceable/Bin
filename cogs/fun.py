import discord
from discord.ext import commands
import random
import asyncio
import discord, requests
import aiohttp
from random import choice
import secrets
import requests
from discord.ext import commands
from discord.ext.commands import BucketType
import base64
import cyberformat, paginator
from async_timeout import timeout

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test3(self , ctx):
        await ctx.send("OK- Fun")


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(
        aliases=['8ball', '8b'],
        brief=" | Ask me a question and get an answer from the ball of wisdom")
    async def eightball(self, ctx, *, question):
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
            f'🎱 Answer: {random.choice(responses)}'
        )


    @eightball.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "You Dum Dum, you need to include a question for me to work")

    @commands.command()
    async def fuckslt(self, ctx):
        await ctx.send("https://tenor.com/view/who-gives-afuck-who-gives-who-cares-dont-care-screw-that-gif-16131453")
        await ctx.send("**LOOKING FOR PEOPLE WHO GIVE A FUCK ABOUT SLT AND HIS CRAPPY DEAD BOTS**")        
        await ctx.channel.trigger_typing()
        await ctx.send("**FOUND IT!**")
        await ctx.send("SIKE NO ONE GIVES A FUCK")
        await asyncio.sleep(200)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(brief=" | Repeat a message")
    async def say(self, ctx, *, saymsg=None):
        if saymsg == None:
            return await ctx.send('You need to give me a message to repeat!')
        sayEmbed = discord.Embed(title=f"{ctx.author} Says",
                                 description=f"{saymsg}",
                                 color=discord.Color.blue())
        await ctx.send(embed=sayEmbed)

    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.command(aliases = ["ctr"])
    async def countdown_to_rickroll(self, ctx, time:int):
        if time > 1000:
            await ctx.send("O-oni-chan... I can't wait that long-")
            return
        one = await ctx.send(f"Rickrolling you in {time}")
        for i in range(time):
            time -= 1
            await asyncio.sleep(1)
            await one.edit(content=f"Rickrolling you in {time}")
        await one.edit(content="https://www.youtube.com/watch?v=DLzxrzFCyOs")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases= ["fakeban", "bon"])
    async def fban(self, ctx, member : discord.Member = None,*, reason="Not given"):
    
        if member == None:
            await ctx.send("mention the person to ban retard")
            return 
        embed = discord.Embed(title = f"*{member} banned successfully   :white_check_mark:*", description = f"Reason:     {reason}", colour=0x8c9eff, timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def comment(self, ctx, *, msg=None):
        if msg == None:
            await ctx.message.reply(embed=discord.Embed(
                title="Error!",
                description=f"Incorrect Usage! Use like this: `f!comment <text>`",
                color=discord.Color.red()
            ))
            return
        url = f"https://some-random-api.ml/canvas/youtube-comment?avatar={ctx.author.avatar_url_as(format='png')}&username={ctx.author.name}&comment={msg}"
        url = url.replace(" ", "%20")
        await ctx.send(url)

    @commands.command()
    async def clap(self, ctx, *, text):
        length = len(text)
        part1 = text[:length//2]
        part2 = text[length//2:]

        await ctx.send(f"{part1} :clap: {part2}")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def wasted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        url = f"https://some-random-api.ml/canvas/wasted?avatar={user.avatar_url_as(format='png')}"
        await ctx.send(url)

    @commands.command()
    async def type(self, ctx):
        await ctx.send("lol ok")
        await ctx.channel.trigger_typing()
        await asyncio.sleep(200)

    @commands.command()
    async def tableflip(self, ctx):
        message = await ctx.send("(\\\\°□°)\\\\  ┬─┬')")
        await asyncio.sleep(1)
        await message.edit(content="(-°□°)-  ┬─┬")
        await asyncio.sleep(1)
        await message.edit(content="(╯°□°)╯    ]")
        await asyncio.sleep(1)
        await message.edit(content="(╯°□°)╯  ︵  ┻━┻")
        await asyncio.sleep(1)
        await message.edit(content="(╯°□°)╯      ┻━┻")


    @commands.command(aliases=['gayrate',])
    async def howgay(self, ctx , member: discord.Member=None):
     if member == None:
      gay = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
      gay = random.choice(gay)
      await ctx.send(f":rainbow_flag:You are `{gay}%` gay")
     else:
      gay = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
      gay = random.choice(gay)
      await ctx.send(f":rainbow_flag:{member.name} is `{gay}%` gay")

    @commands.command(aliases=['simprate','simp'])
    async def howsimp(self, ctx , member: discord.Member=None):
     if member == None:
      simp = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
      simp = random.choice(simp)
      await ctx.send(f":smirk:You are `{simp}%` simp")
     else:
      simp = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
      simp = random.choice(simp)
      await ctx.send(f":smirk:{member.name} is `{simp}%` simp")

    @commands.command(aliases=['stupidrate','stupid'])
    async def howstupid(self, ctx , member: discord.Member=None):
     if member == None:
      stupid = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
      stupid = random.choice(stupid)
      await ctx.send(f":zany_face:You are `{stupid}%` stupid")
     else:
      stupid = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
      stupid = random.choice(stupid)
      await ctx.send(f":zany_face:{member.name} is `{stupid}%` stupid")

    @commands.command()
    async def punch(self, ctx, user: discord.Member):
        if user == ctx.author:
            punchEmbed = discord.Embed(
                title="Punch a User",
                description=
                f" {ctx.author.mention} punched themselves... just fucking... WHY!?"
            )
        else:
            punchEmbed = discord.Embed(
                title="Punch a User",
                description=f" {ctx.author.mention} punched {user.mention}")
        punchEmbed.set_image(
            url=
            "https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446"
        )
        punchEmbed.set_footer(text="Run f!about for more info")
        await ctx.send(embed=punchEmbed)

    @commands.command()
    async def choose(self, ctx, *, choices : str):
        await ctx.send(f"currently offline due to the ability to nuke")

    @commands.command()
    async def cuddle(self, ctx, member:discord.Member):
        await ctx.send(f"OWO :heart: {ctx.author.mention} cuddled with {member.mention} cuuuute")


    #@commands.command()
    #async def fight(self, ctx, opponent: discord.Member):
    #    responses = [
    #        "was hit on the head by",
    #        "was kicked by",
    #        "was slammed into a wall by",
    #        "was dropkicked by",
    #        "was DDoSed by",
    #        "was chokeslammed by",
    #        "was run over with a robot by",
    #        "had their IQ dropped 15 points by",
    #        "had a heavy object dropped on them by",
    #        "was beat up by"
    #    ]
#
    #    damages = [100, 150, 200, 300, 50, 250, 420]
    #    players = [ctx.author, opponent]
    #    hps = [1000, 1000]
    #    turn = random.randint(0, 1)
#
    #    messages = []
    #    while hps[0] > 0 and hps[1] > 0:
    #        opp_idx = (turn + 1) % 2
    #        damage = random.choice(damages)
    #        hps[opp_idx] = max(hps[opp_idx] - damage, 0)
    #        messages.append(
    #            await ctx.send("**{opponent}** {response} **{attacker}**! *[-{dmg} hp] [{hp} HP remaining]*".format(
    #                opponent=players[opp_idx].name,
    #                attacker=players[turn].name,
    #                response=random.choice(responses),
    #                dmg=damage,
    #                hp=hps[opp_idx]
    #            )))
    #        await asyncio(1.5)
    #        turn = opp_idx
    #    await ctx.send(
    #        "{loser} lost! GG {winner}!".format(loser=players[turn].mention, winner=players[(turn + 1) % 2].mention))
    #    await asyncio(5)
    #    if ctx.channel.permissions_for(ctx.me).manage_messages:
    #        await ctx.channel.delete_messages(messages)
    #    else:
    #        for msg in messages:
    #            await msg.delete()
    '''
@commands.command
async def insult(self, ctx, member: discord.Member = None):
    insult = await get_momma_jokes
    await ctx.send(insult)
    

    @commands.command()
    async def hack(self, ctx):
        message = await ctx.send("**[13.2%]** Hacking...")
        await asyncio.sleep(2)
        await message.edit(content="**[24.8%]** Getting the IP address")
        await asyncio.sleep(2)
        await message.edit(content="**[42.5%]** IP address: 127.0.0.1:8573")
        await asyncio.sleep(2)
        await message.edit(content="**[50.0%]** Selling their data to FaceBook")
        await asyncio.sleep(2)
        await message.edit(content="**[64.2%]** Gaining remote access to their device")
        await asyncio.sleep(2)
        await message.edit(content="**[81.9%]** Sending pp pics to all their friends")
        await asyncio.sleep(2)
        await message.edit(content="**[94.3%]** Deleting their discord account...")
        await asyncio.sleep(2)
        await message.edit(content="**[100%]** The *totally* real and *dangerous* hack is complete")
    '''
    @commands.command()
    async def shreshta(self, ctx):
        message = await ctx.send("Shreshta fucking Sanyam")
        await asyncio.sleep(2)
        await message.edit(content="8======D ()")
        await asyncio.sleep(2)
        await message.edit(content="8======D   ()")
        await asyncio.sleep(2)
        await message.edit(content="8===(==)=D ")
        await asyncio.sleep(2)
        await message.edit(content="8======D ()")
        await asyncio.sleep(2)
        await message.edit(content="8===(==)=D ")
        await asyncio.sleep(2)
        await message.edit(content="AH SANYAM IM GONNA CUM")
        await asyncio.sleep(2)
        await message.edit(content="8======D---()")
        await asyncio.sleep(2)
        await message.edit(content="OH DADDY SHRESHTA GOT HIS JUICE ALL OVER ME")

    @commands.command()
    async def reverse(self, ctx, *, msg:str):
        await ctx.send(msg[::-1])

    @commands.command(aliases = ["spell"])
    async def spellout(self, ctx, *, msg:str):
        await ctx.send(" ".join(list(msg.upper())))


    @commands.command()
    async def dice(self, ctx, number=1):
        '''Rolls a certain number of dice'''
        if number > 20:
            number = 20

        fmt = ''
        for i in range(1, number + 1):
            fmt += f'`Dice {i}: {random.randint(1, 6)}`\n'
            color = discord.Color.green()
        em = discord.Embed(color=color, title='Roll a certain number of dice', description=fmt)
        await ctx.send(embed=em)

    @commands.command(aliases=['trump', 'trumpquote'])
    async def asktrump(self, ctx, *, question):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q={question}') as resp:
                file = await resp.json()
        quote = file['message']
        em = discord.Embed(color=discord.Color.green())
        em.title = "What does Trump say?"
        em.description = quote
        em.set_footer(text="Made possible by whatdoestrumpthink.com", icon_url="http://www.stickpng.com/assets/images/5841c17aa6515b1e0ad75aa1.png")
        await ctx.send(embed=em)

    @commands.command(aliases=['joke'])
    async def badjoke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://official-joke-api.appspot.com/random_joke') as resp:
                data = await resp.json()
        em = discord.Embed(color=discord.Color.green())
        em.title = data['setup']
        em.description = data['punchline']
        await ctx.send(embed=em)

    @commands.command(aliases=['howhot', 'hot'])
    async def hotcalc(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")


    @commands.command()
    async def beer(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ Give someone a beer! 🍻 """
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"**{ctx.author.name}**: paaaarty!🎉🍺")
        if user.id == self.bot.user.id:
            return await ctx.send("*drinks beer with you* 🍻")
        if user.bot:
            return await ctx.send(f"I would love to give beer to the bot **{ctx.author.name}**, but I don't think it will respond to you :/")

        beer_offer = f"**{user.name}**, you got a 🍺 offer from **{ctx.author.name}**"
        beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await self.bot.wait_for('raw_reaction_add', timeout=30.0, check=reaction_check)
            await msg.edit(content=f"**{user.name}** and **{ctx.author.name}** are enjoying a lovely beer together 🍻")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"well, doesn't seem like **{user.name}** wanted a beer with you **{ctx.author.name}** ;-;")
        except discord.Forbidden:
            # Yeah so, bot doesn't have reaction permission, drop the "offer" word
            beer_offer = f"**{user.name}**, you got a 🍺 from **{ctx.author.name}**"
            beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)

    @commands.command()
    async def rate(self, ctx, *, thing: commands.clean_content):
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.send(f"I'd that a **{round(rate_amount, 4)} / 100**")

    @commands.command(aliases=['meow'])
    @commands.cooldown(per=3, rate=1)
    async def cat(self, ctx):
        r = requests.get("https://api.thecatapi.com/v1/images/search").json()

        cat_em = discord.Embed(title=':cat: Meow',colour=discord.Colour.blue())
        cat_em.set_image(url=f'{r[0]["url"]}')

        await ctx.send(embed=cat_em)

    @commands.command(aliases=['puppy', 'woof'])
    @commands.cooldown(per=3, rate=1)
    async def dog(self, ctx):
        r = requests.get("https://api.thedogapi.com/v1/images/search").json()

        dog_em = discord.Embed(title=':dog: woof',colour=discord.Colour.blue())
        dog_em.set_image(url=f'{r[0]["url"]}')

        await ctx.send(embed=dog_em)
    
    @commands.command()
    @commands.cooldown(per=3, rate=1)
    async def panda(self, ctx):
        r = requests.get("https://some-random-api.ml/img/panda").json()

        dog_em = discord.Embed(title=':panda_face: aww',colour=discord.Colour.blue())
        dog_em.set_image(url=f'{r["link"]}')

        await ctx.send(embed=dog_em)
    
    @commands.command()
    @commands.cooldown(per=3, rate=1)
    async def fox(self, ctx):
        r = requests.get("https://some-random-api.ml/img/fox").json()

        dog_em = discord.Embed(title=":fox: what a cute fox!",colour=discord.Colour.blue())
        dog_em.set_image(url=f'{r["link"]}')

        await ctx.send(embed=dog_em)

    @commands.command()
    async def password(self, ctx, nbytes: int = 18):
        if nbytes not in range(3, 1401):
            return await ctx.send("I only accept any numbers between 3-1400")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"Sending you a private message with your random generated password... **{ctx.author.name}**")
        await ctx.send("Password sent! ||btw the emoji means secret in japanese||")
        await ctx.author.send(f":secret: **Here is your password:**\n{secrets.token_urlsafe(nbytes)}")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases = ['bait', 'freenitro', 'nitrobait', 'keknitro'])
    async def jebait(self, ctx):
        embed = discord.Embed(title = "FREE NITRO", description = f"[https://discord.gift/NBnj8bySBWr63Q99](https://discord.gg/euBuYefshR)", color = 0x00FFFF)

        try:
            await ctx.message.delete()
        except:
            pass

        await ctx.send(embed = embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases = ['simpfor'])
    async def simp_for(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send(f"Please enter a user you want simp for.")
            return

        embed = discord.Embed(title = "New Simp", description = f"{ctx.author.mention} just simped for {user.mention} <a:q_simp:698816481781350411>.", color = 0xFFC0CB)
        embed.set_thumbnail(url = user.avatar_url)
        await ctx.message.reply(embed = embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def mock(self, ctx, *,text=None):

        if text == None:
            await ctx.message.reply("Please enter some text!")
        else:

            filter = ['@here', '@everyone', '<@&', '<@!']

            for word in filter:
                if text.count(word) > 0:
                    await ctx.message.reply(f"Sorry, I won't ping anyone. Try something else. LIKE TEXT!?")
                    return

            res = ""
            for c in text:
                chance = random.randint(0,1)
                if chance:
                    res += c.upper()
                else:
                    res += c.lower()
            await ctx.message.reply(res)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def advice(self, ctx):
        url = "https://api.adviceslip.com/advice"
        response = requests.get(url)
        advice = response.json()
        real_advice = advice['slip']['advice']
        await ctx.message.reply(real_advice)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def quote(self, ctx):
        results = requests.get('https://type.fit/api/quotes').json()
        num = random.randint(1, 1500)
        content = results[num]['text']
        await ctx.message.reply(content)


    @commands.command()
    async def aaron(self, ctx):
        results = (
          'https://cdn.discordapp.com/attachments/771670448710483981/831450860545769492/unknown.png', 'https://cdn.discordapp.com/attachments/771670448710483981/836616062933270538/unknown.png', 'https://cdn.discordapp.com/attachments/771670448710483981/836616045070254120/unknown.png'
          )
        resultss = f"{random.choice(results)}"
        await ctx.message.reply(resultss)
        await ctx.send("**<@490867362430713876> fuck off 7 year old pussy ass tik tok consuming scum mallu scamming filth bloody bastard bitch begging motherfucker pedophile cunt**")

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command()
    async def hack(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.message.reply(embed=discord.Embed(
                title = "BRUH!",
                description = "You didn't mention who to hack. Please try again!",
                color = 0xFFC0CB
            ))

        elif user == ctx.author:
            await ctx.message.reply("You shouldn't hack yourself.")

        else:
            email_fun = ['69420', '8008135', 'eatsA$$', 'PeekABoo',
                            'TheShire', 'isFAT', 'Dumb_man', 'Ruthless_gamer',
                            'Sexygirl69', 'Loyalboy69', 'likesButts']

            email_address = f"{user.name.lower()}{random.choice(email_fun).lower()}@gmail.com"
                            
            passwords = ['animeislife69420', 'big_awoogas', 'red_sus_ngl',
                            'IamACompleteIdiot', 'YouWontGuessThisOne',
                            'yetanotherpassword', 'iamnottellingyoumypw',
                            'SayHelloToMyLittleFriend', 'ImUnderYourBed',
                            'TellMyWifeILoveHer', 'P@$$w0rd', 'iLike8008135', 'IKnewYouWouldHackIntoMyAccount',
                            'BestPasswordEver', 'JustARandomPassword']
                            
            password = f"{random.choice(passwords)}"

            DMs = ["send nudes please", "i invited falc and i got a cookie",
                    "i hope my mum doesn't find my nudes folder",
                    "please dont bully me", "https://youtu.be/oHg5SJYRHA0", 
                    "i like bananas", "black jellybeans are the best jellybeans",
                    "i use discord in light mode", "i forgot to feed the kids in my basement", "i have a micro penis"]

            latest_DM = f"{random.choice(DMs)}"

            ip_address = f"690.4.2.0:{random.randint(1000, 9999)}"

            Discord_Servers = ["Sons of Virgins", "Small Benis Gang", "Gamers United",
                                    "Anime_Server_69420", "CyberDelayed 2077", "I love Corn"]

            Most_Used_Discord_Server = f"{random.choice(Discord_Servers)}"


            msg1 = await ctx.send("Initializing Hack.exe... <a:3859_Loading:754710375446085754>")
            await asyncio.sleep(2)

            real_msg1 = await ctx.channel.fetch_message(msg1.id)
            await real_msg1.edit(content = f"Successfully initialized Hack.exe, beginning hack on {user.name}... <a:3859_Loading:754710375446085754>")
            await asyncio.sleep(2)

            real_msg2 = await ctx.channel.fetch_message(msg1.id)
            await real_msg2.edit(content = f"Logging into {user.name}'s Discord Account... <a:3859_Loading:754710375446085754>")
            await asyncio.sleep(2)

            real_msg3 = await ctx.channel.fetch_message(msg1.id)
            await real_msg3.edit(content = f"<a:discord_loading~1:745047586552938516> Logged into {user.name}'s Discord:\nEmail Address: `{email_address}`\nPassword: `{password}`")
            await asyncio.sleep(2)

            real_msg4 = await ctx.channel.fetch_message(msg1.id)
            await real_msg4.edit(content = f"Fetching DMs from their friends(if there are any)... <a:3859_Loading:754710375446085754>")
            await asyncio.sleep(2)

            real_msg5 = await ctx.channel.fetch_message(msg1.id)
            await real_msg5.edit(content = f"Latest DM from {user.name}: `{latest_DM}`")
            await asyncio.sleep(2)

            real_msg6 = await ctx.channel.fetch_message(msg1.id)
            await real_msg6.edit(content = f"Getting IP address... <a:3859_Loading:754710375446085754>")
            await asyncio.sleep(2)

            real_msg7 = await ctx.channel.fetch_message(msg1.id)
            await real_msg7.edit(content = f"IP address found: `{ip_address}`")
            await asyncio.sleep(2)

            real_msg11 = await ctx.channel.fetch_message(msg1.id)
            await real_msg11.edit(content = f"Fetching the Most Used Discord Server... <a:3859_Loading:754710375446085754>")
            await asyncio.sleep(2)

            real_msg10 = await ctx.channel.fetch_message(msg1.id)
            await real_msg10.edit(content = f"Most used Discord Server in {user.name}'s Account: `{Most_Used_Discord_Server}`")
            await asyncio.sleep(2)

            real_msg8 = await ctx.channel.fetch_message(msg1.id)
            await real_msg8.edit(content = f"Selling data to the dark web... <a:3859_Loading:754710375446085754>")
            await asyncio.sleep(2)

            real_msg9 = await ctx.channel.fetch_message(msg1.id)
            await real_msg9.edit(content = f"Hacking complete.")
            await ctx.send(f"{user.name} has successfully been hacked. <a:Tick:827851647463718963>\n\n**{user.name}**'s Data:\nDiscord Email: `{email_address}`\nDiscord Password: `{password}`\nMost used Discord Server: `{Most_Used_Discord_Server}`\nIP Address: `{ip_address}`\nLatest DM: `{latest_DM}`")

    @commands.command()
    async def coffee(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"☕ | {ctx.author.name} Enjoying Coffee alone :smirk: ")
        if user.id == self.bot.user.id:
            return await ctx.send("☕ | {ctx.author.name} Enjoying Coffee alone :smirk: ")
        if user.bot:
            return await ctx.send(f"I would love to give beer to the bot **{ctx.author.name}**, but I don't think it will respond to you :/")
        elif user == self.client.user:
            await ctx.send(embed=discord.Embed(description="☕ | Don't worry I will drink coffee with you  *sips*"))
            return

        beer_offer = f"☕ | {user.mention}, you got a coffee offer from {ctx.author.name}"
        beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "☕":
                return True
            return False

        try:
            await msg.add_reaction("☕")
            await self.bot.wait_for('raw_reaction_add', timeout=30.0, check=reaction_check)
            await msg.edit(content=f"**{user.name}** and **{ctx.author.name}** are enjoying a lovely coffee together ☕")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"well, doesn't seem like **{user.name}** wanted a coffee with you **{ctx.author.name}** ;-;")
        except discord.Forbidden:
            # Yeah so, bot doesn't have reaction permission, drop the "offer" word
            beer_offer = f"**{user.name}**, you got a ☕ from **{ctx.author.name}**"
            beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)

    '''   @commands.command()
    async def coffee(self, ctx, member: discord.Member):
            if member == ctx.author:
                await ctx.send(embed=discord.Embed(description=f"☕ | {ctx.author.name} Enjoying Coffee alone :smirk: ", color=random.choice(self.colours)))
                return
            elif member == self.client.user:
                await ctx.send(embed=discord.Embed(description="☕ | Don't worry I will drink coffee with you  *sips*", color=random.choice(self.colours)))
                return
            elif member.bot: return;

            coffee_offer = f"☕ | {member.mention}, you got a coffee offer from {ctx.author.name}"
            coffee_msg = await ctx.send(embed=discord.Embed(description=coffee_offer,color=random.choice(self.colours)))
            await coffee_msg.add_reaction('☕')

            def check(reaction, user):
                return user == member and str(reaction.emoji) == '☕'

            try:
                await self.client.wait_for('reaction_add', timeout=600.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send(embed=discord.Embed(description=f"Looks like {member.name} are busy", color=random.choice(self.colours)))
            else:
                await coffee_msg.delete()
                await ctx.send(embed=discord.Embed(description=f"☕ | Yay! {ctx.author.name} and {member.name} are enjoying coffee together!", color=random.choice(self.colours)))
    

    @commands.command(aliases = ['triv'])
    @commands.cooldown(3, 30, commands.BucketType.channel)
    @commands.max_concurrency(1, commands.BucketType.channel, wait = False)
    async def trivia(self, ctx):
        data = requests.get(f'https://opentdb.com/api.php?amount=1').json()
        results = data['results'][0]
        embed = discord.Embed(
            title = ":question:  Trivia",
            description = f"Category: {results['category']} | Difficulty: {results['difficulty'].capitalize()}",
            color = ctx.author.color
        )
        embed2 = embed
        def decode(answers):
            new = []
            for i in answers:
                new.append(html.unescape(i))
            return new
        if results['type'] == 'boolean':
            if results['correct_answer'] == "False":
                answers = results['incorrect_answers'] + [results['correct_answer']]
            else:
                answers = [results['correct_answer']] + results['incorrect_answers']
            answers = decode(answers)
            embed.add_field(name = html.unescape(results['question']), value = f"True or False")
            available_commands = ['true', 'false', 't', 'f']
        else:
            pos = random.randint(0, 3)
            if pos == 3:
                answers = results['incorrect_answers'] + [results['correct_answer']]
            else:
                answers = results['incorrect_answers'][0:pos] + [results['correct_answer']] + results['incorrect_answers'][pos:]
            answers = decode(answers)
            embed.add_field(name = html.unescape(results['question']), value = f"A) {answers[0]}\nB) {answers[1]}\nC) {answers[2]}\nD) {answers[3]}")
            available_commands = ['a', 'b', 'c', 'd'] + [x.lower() for x in answers]
        question = await ctx.send(embed = embed)
        correct_answer = html.unescape(results['correct_answer'])
        def check(m):
            return m.channel == ctx.channel and m.content.lower() in available_commands and not m.author.bot
        try:
            msg = await self.client.wait_for('message', timeout = 30.0, check = check)
        except asyncio.TimeoutError:
            return
        correct = False
        if results['type'] == 'boolean':
            if msg.content.lower() == correct_answer.lower() or msg.content.lower() == correct_answer.lower()[0]:
                correct = True
            answer_string = f"The answer was **{correct_answer}**"
        else:
            letters = ['a', 'b', 'c', 'd']
            if msg.content.lower() == correct_answer.lower() or msg.content.lower() == letters[pos]:
                correct = True
            answer_string = f"The answer was **{letters[pos].upper()}) {correct_answer}**"
        if correct:
            name = ":white_check_mark:  Correct"
            if results['difficulty'] == 'easy':
                self.add_xp(ctx.author.id, 0.25)
            elif results['difficulty'] == 'medium':
                self.add_xp(ctx.author.id, 0.5)
            else:
                self.add_xp(ctx.author.id, 1)
        else:
            name = ":x:  Incorrect"
        embed2.clear_fields()
        embed2.add_field(name = name, value = answer_string)
        await question.edit(embed = embed2)

    @trivia.error
    async def trivia_error(self, ctx, error):
        await ctx.send(error)
'''
    @commands.command(aliases = ["slurp_juice", 'slurpjuice'])
    async def slurp(self, ctx):
        e = discord.Embed(title = "Summer Time", color = 0xff8648)
        e.set_footer(text="Recipes by Party Jammer")
        o = discord.Embed(title="Slurp Punch", description="**To start of by making this juicy juice you will be needing the following:** \n \n **(1) Green [Hawaiian Punch](https://www.amazon.com/Hawaiian-Punch-Singles-Packets-Servings/dp/B005LURCVY/ref=as_li_ss_tl?keywords=green+hawaiian+punch&qid=1549660066&sr=8-3&th=1&linkCode=sl1&tag=simplisticlivin-20&linkId=a8771b7efeacb7ebe5c4a8a120325641&language=en_US)** (you can use the singles packets or the gallon size pre-made juiceSugar Free or Low Sugar) \n **(2) Blue Gatorade or PoweradeBlue \n (3) Food Coloring \n (4) Lastly some ice**", color = 0x008cb4, url = "https://www.simplisticallyliving.com/fortnite-slurp-juice-recipe/")
        o.add_field(name="How to add up the drinks ?", value="The Hawaiian Punch is a great choice because it has a higher sugar content and is heavier causing it to ‘sink’.  The sugar free/low sugar sports drinks are less dense and will ‘float’ on top. \n Eg: Gatorade , Powerade ", inline = False)
        o.add_field(name="Instructions", value = "(1) In the bottle of Gatorade or Powerade, pour a few drops of blue food coloring and shake to mix.  This will help the blue turn the perfect Slurp Juice shade! \n (2) Fill a glass with ice. \n (3) Pour in ¾ of the glass green Hawaiian Punch.  \n (4) Slowly pour the blue Gatorade or Powerade on top.  (I turn a spoon upside down and slowly pour it over the spoon to slow down the pour even more.)  \n (5) The blue should float on top of the green!  \n (6) Serve! \n \n Thats all ehh !")
        o.set_image(url="https://cdn.discordapp.com/attachments/791664210550456330/819489955918905354/7577D114-AA81-4E23-862E-E5E0B83150F3.webp")
        o.set_footer(text="Click the title to get the detailed version.")
        pog = await ctx.send(embed=e)
        await asyncio.sleep(1)
        await pog.edit(embed=o)

    @commands.command(aliases = ['emojitext', 'emojify'])
    async def textmojify(self, ctx, *, msg):
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass

        if msg != None:
            out = msg.lower()
            text = out.replace(' ', '    ').replace('10', '\u200B:keycap_ten:')\
                      .replace('ab', '\u200B🆎').replace('cl', '\u200B🆑')\
                      .replace('0', '\u200B:zero:').replace('1', '\u200B:one:')\
                      .replace('2', '\u200B:two:').replace('3', '\u200B:three:')\
                      .replace('4', '\u200B:four:').replace('5', '\u200B:five:')\
                      .replace('6', '\u200B:six:').replace('7', '\u200B:seven:')\
                      .replace('8', '\u200B:eight:').replace('9', '\u200B:nine:')\
                      .replace('!', '\u200B❗').replace('?', '\u200B❓')\
                      .replace('vs', '\u200B🆚').replace('.', '\u200B🔸')\
                      .replace(',', '🔻').replace('a', '\u200B🅰')\
                      .replace('b', '\u200B🅱').replace('c', '\u200B🇨')\
                      .replace('d', '\u200B🇩').replace('e', '\u200B🇪')\
                      .replace('f', '\u200B🇫').replace('g', '\u200B🇬')\
                      .replace('h', '\u200B🇭').replace('i', '\u200B🇮')\
                      .replace('j', '\u200B🇯').replace('k', '\u200B🇰')\
                      .replace('l', '\u200B🇱').replace('m', '\u200B🇲')\
                      .replace('n', '\u200B🇳').replace('ñ', '\u200B🇳')\
                      .replace('o', '\u200B🅾').replace('p', '\u200B🅿')\
                      .replace('q', '\u200B🇶').replace('r', '\u200B🇷')\
                      .replace('s', '\u200B🇸').replace('t', '\u200B🇹')\
                      .replace('u', '\u200B🇺').replace('v', '\u200B🇻')\
                      .replace('w', '\u200B🇼').replace('x', '\u200B🇽')\
                      .replace('y', '\u200B🇾').replace('z', '\u200B🇿')
            try:
                await ctx.send(text)
            except Exception as e:
                await ctx.send(f'```{e}```')
        else:
            await ctx.send('Write something, reee!', delete_after=3.0)

    '''
    @commands.command(aliases = ['ttt'])
    async def tictactoe(self, ctx, *, opponent: discord.Member):
        print(f"{ctx.guild.name} - #{ctx.channel.name} - {ctx.author.name} - {ctx.message.content}")
        if opponent.id == ctx.author.id:
            await ctx.send("You played yourself. Oh wait, you can't.")
            return
        if opponent.bot:
            await ctx.send("You played a bot. Oh wait, you can't.")
            return
        await ctx.send('Tictactoe has started. Type the number of the square you want to go in. Type "end_game" to end the game.')
        player1 = ctx.author
        player2 = opponent

        commands = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'end_game']

        def check(m):
            return m.channel == ctx.channel and (m.content in commands) and not m.author.bot

        def endgame(board):
            for k in range(3):
                if board[k][0] == board[k][1] and board[k][1] == board[k][2]:
                    if board[k][0] > 0:
                        return board[k][0]
                elif board[0][k] == board[1][k] and board[1][k] == board[2][k]:
                    if board[0][k] > 0:
                        return board[0][k]
            if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
                if board[1][1] > 0:
                    return board[1][1]
            counter = 0
            for l in range(3):
                for m in range(3):
                    if board[l][m] == 0:
                        counter += 1
            if counter == 0:
                return 3
            else:
                return 0

        board = [[0] * 3 for n in range(3)]
        end = False
        player = 1
        while not end:
            out = '```'
            for i in range(3):
                for j in range(3):
                    out += ' '
                    if board[i][j] == 0:
                        out += str(i * 3 + j + 1)
                    elif board[i][j] == 1:
                        out += 'X'
                    elif board[i][j] == 2:
                        out += 'O'
                    out += ' '
                    if j != 2:
                        out += '|'
                out += '\n'
                if i != 2:
                    out += '---+---+---\n'
            out += '```'
            await ctx.send(out)
            result = endgame(board)
            if result != 0:
                if result == 1:
                    await ctx.send(f'{player1.display_name} wins!')
                    return
                elif result == 2:
                    await ctx.send(f'{player2.display_name} wins!')
                    return
                else:
                    await ctx.send('Tie!')
                    return
            if player == 1:
                await ctx.send("{0}'s turn".format(player1.display_name))
            else:
                await ctx.send("{0}'s turn".format(player2.display_name))
            valid = False
            while not valid:
                try:
                    msg = await self.client.wait_for('message', timeout = 300.0, check = check)
                except asyncio.TimeoutError:
                    await ctx.send('Game timed out.')
                    return
                if (player == 1 and msg.author == player1) or (player == 2 and msg.author == player2):
                    if msg.content == 'end_game':
                        await ctx.send('Game ended.')
                        return
                    input = int(msg.content)
                    a = int((input - 1) / 3)
                    b = int((input - 1) % 3)
                    if board[a][b] == 0:
                        board[a][b] = player
                        player = 3 - player
                        valid = True
	
    @tictactoe.error
    async def tictactoe_error(self, ctx, error):
        print(error)
        await ctx.send('Please follow format: `f!tictactoe {opponent}`')
   '''

    @commands.command()
    async def lick(self, ctx, user: discord.Member):
        gifs = ["https://images-ext-2.discordapp.net/external/AqmvPrnwsYvvxn5kgJH9Bd-J7mKkl3ka-jpVCwOiMyQ/https/cdn.weeb.sh/images/Sk15iVlOf.gif",
                "https://media1.tenor.com/images/6b701503b0e5ea725b0b3fdf6824d390/tenor.gif?itemid=12141727", "https://cdn.weeb.sh/images/ryGpGsnAZ.gif"]
        embed = discord.Embed(description=f"Woah {ctx.author.mention} stop licking {user.mention} like he/she is icecream",
                              color=discord.Color.blue())
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} Licks himself. ||How do you even lick yourself?||",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)    

   # @commands.command()
   # async def slap(self, ctx, user: discord.Member):
   #     gifs = ["https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943",
   #        "https://media1.tenor.com/images/e8f880b13c17d61810ac381b2f6a93c3/tenor.gif?itemid=17897236"]
   #     embed = discord.Embed(description=f"Woa {ctx.author.mention} chill bro... You slapped {user.mention} so hard #he/she is now in hospital...",color=random.randint(0x000000, 0xFFFFFF))
   #     embed.set_image(url=f"{random.choice(gifs)}")
   #     if user == ctx.author:
   #         embed = discord.Embed(description=f"{ctx.author.mention} You wont slap yourself hard enough come HERE!",#color=random.randint(0x000000, 0xFFFFFF))
   #         embed.set_image(url=f"{random.choice(gifs)}")
   #     await ctx.send(embed=embed)
   #     

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        gifs = ["https://cdn.weeb.sh/images/H1ui__XDW.gif", "https://cdn.weeb.sh/images/B11CDkhqM.gif", "https://cdn.weeb.sh/images/rJv2H5adf.gif", "https://cdn.weeb.sh/images/SywetdQvZ.gif", "https://cdn.weeb.sh/images/BJCCd_7Pb.gif", "https://cdn.weeb.sh/images/Bk5haAocG.gif"]
        embed = discord.Embed(description=f"{ctx.author.mention} hugs {user.mention} ",
                              color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} Why you hugging yourself come here lemme hug you!",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)
     
    @commands.command()
    async def kiss(self, ctx, user: discord.Member):
        gifs = ["https://media1.tenor.com/images/558f63303a303abfdddaa71dc7b3d6ae/tenor.gif?itemid=12879850",
                "https://i.gifer.com/PCUi.gif", "https://cdn.weeb.sh/images/B13D2aOwW.gif","https://cdn.weeb.sh/images/B1yv36_PZ.gif", "https://cdn.weeb.sh/images/Sk5P2adDb.gif", "https://media.discordyui.net/reactions/kiss/234082934.gif"]
        embed = discord.Embed(description=f"Woah {ctx.author.mention} stop kissing {user.mention} so passionately",
                              color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} Why you kissing yourself come here lemme kiss you!",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def pat(self, ctx, user: discord.Member):
        gifs = ["https://i1.wp.com/gifimage.net/wp-content/uploads/2017/07/head-pat-gif-9.gif?fit=800,450", 
                 "https://media1.tenor.com/images/6ee188a109975a825f53e0dfa56d497d/tenor.gif?itemid=17747839"
                 "https://64.media.tumblr.com/cadf248febe96afdd6869b7a95600abb/tumblr_onjo4cGrZE1vhnny1o1_500.gifv"]
        embed = discord.Embed(description=f"{ctx.author.mention} pats {user.mention}", color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} Why you patting yourself come here lemme pat you!",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)    

    @commands.command(aliases=['number'])
    async def numberfact(self, ctx, number: int):
        '''Get a fact about a number.'''
        if not number:
            await ctx.send(f'Usage: `{ctx.prefix}numberfact <number>`')
            return
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://numbersapi.com/{number}?json') as resp:
                    file = await resp.json()
                    fact = file['text']
                    await ctx.send(f"**Did you know?**\n*{fact}*")
        except KeyError:
            await ctx.send("No facts are available for that number.")

    @commands.command(aliases=['xkcd', 'comic'])
    async def randomcomic(self, ctx):
        '''Get a comic from xkcd.'''
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://xkcd.com/info.0.json') as resp:
                data = await resp.json()
                currentcomic = data['num']
        rand = random.randint(0, currentcomic)  # max = current comic
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://xkcd.com/{rand}/info.0.json') as resp:
                data = await resp.json()
        em = discord.Embed(color=discord.Color.green())
        em.title = f"XKCD Number {data['num']}- \"{data['title']}\""
        em.set_footer(text=f"Published on {data['month']}/{data['day']}/{data['year']}")
        em.set_image(url=data['img'])
        await ctx.send(embed=em)



    @commands.command()
    @commands.guild_only()
    async def roast(self, ctx, user: discord.Member = None):
        '''Roast someone! If you suck at roasting them yourself.'''
        msg = f"Hey, {user.mention}!" if user is not None else ""
        roasts = ["I'd give you a nasty look but you've already got one.", "If you're going to be two-faced, at least make one of them pretty.", "The only way you'll ever get laid is if you crawl up a chicken's ass and wait.", "It looks like your face caught fire and someone tried to put it out with a hammer.", "I'd like to see things from your point of view, but I can't seem to get my head that far up your ass.", "Scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons.", "Why is it acceptable for you to be an idiot but not for me to point it out?", "Just because you have one doesn't mean you need to act like one.", "Someday you'll go far... and I hope you stay there.", "Which sexual position produces the ugliest children? Ask your mother.", "No, those pants don't make you look fatter - how could they?", "Save your breath - you'll need it to blow up your date.", "If you really want to know about mistakes, you should ask your parents.", "Whatever kind of look you were going for, you missed.", "Hey, you have something on your chin... no, the 3rd one down.", "I don't know what makes you so stupid, but it really works.", "You are proof that evolution can go in reverse.", "Brains aren't everything. In your case they're nothing.", "I thought of you today. It reminded me to take the garbage out.", "You're so ugly when you look in the mirror, your reflection looks away.", "Quick - check your face! I just found your nose in my business.", "It's better to let someone think you're stupid than open your mouth and prove it.", "You're such a beautiful, intelligent, wonderful person. Oh I'm sorry, I thought we were having a lying competition.", "I'd slap you but I don't want to make your face look any better.", "You have the right to remain silent because whatever you say will probably be stupid anyway., your ass must be pretty jealous of all the shit that comes out of your mouth.","some day you'll go far, and I hope you stay there.","I'm trying my absolute hardest to see things from your perspective, but I just can't get my head that far up my ass.","I'm not a protocolgist, but I know an asshole when I see one.","Do yourself a favor and ignore anyone who tels you to be yourself. Bad idea in your case.","Everyone's entitled to act stupid once in awhile, but you really abuse the privilege.","Can you die of constipation? I ask because I'm worried about how full of shit you are.","Sorry, I didn't get that. I don't speak bullshit.","There are some remarkably dumb people in this world. Thanks for helping me understand that.","I could eat a bowl of alphabet soup and shit out a smarter statement than whatever you just said.","You always bring me so much joy, as soon as you leave the room.","I'd tell you how I really feel, but I wasn't born with enough middle fingers to express myself in this case.","You have the right to remain silent because whatever you say will probably be stupid anyway.","your family tree must be a cactuss because you're all a bunch of pricks.","You'll never be the man your mom is.","If laughter is the best medicine, your face must be curing the world.","scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons, as you are one.","if you really want to know about mistakes, you should ask your parents.","I thought of you today. It reminded me to take the garbage out.","you're such a beautiful, intelligent, wonderful person. Oh I'm sorry, I thought we were having a lying competition.","I may love to shop but I'm not buying your bullshit.","I just stepped in something that was smarter than you, and smelled better too."]
        await ctx.send(f"{msg} {random.choice(roasts)}")



    @commands.command()
    async def dad(self, ctx, *, message: str = None):
        if message == None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send('I cant name you anything.')
        embed = discord.Embed(
            color=discord.Color.red()
        )
        embed.add_field(name='Daddo Machine 9000', value=f'Hello {message}, Im Dad')
        await ctx.send(embed=embed)

    @commands.command()
    async def iq(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        iq = ['130 and above (Very Superior)',
              '120–129 (Superior)',
              '110–119 (High Average)',
              '90–109 (Average)',
              '80–89 (Low Average)',
              '70–79 (Borderline)',
              '69 and below	(Extremely Low)']
        e = discord.Embed(color=discord.Colour.red()).set_author(
            name=self.bot.user,
            icon_url=self.bot.user.avatar_url)
        e.add_field(name='**IQ Machine 9000**', value=f"{user.display_name}'s IQ is {random.choice(iq)}")
        await ctx.send(embed=e)

    @commands.command(aliases=['penis'], name='pp')
    async def pp(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        former = ['8', 'D']
        for i in range(random.randrange(10)):
            former.insert(1, '=')
        e = discord.Embed(title="", description="__**Penis Machine!**__", color=0x50C878)
        e.add_field(name="**{}'s penis is:**".format(user),
                    value=''.join(map(str, former)))
        await ctx.send(embed=e)

    @commands.command(aliases=['murder'])
    async def kill(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author
        died = ['rolling out of the bed and the demon under the bed ate them.',
                'getting impaled on the bill of a swordfish.',
                'falling off a ladder and landing head first in a water bucket.',
                'his own explosive while trying to steal from a condom dispenser.',
                'a coconut falling off a tree and smashing there skull in.',
                'taking a selfie with a loaded handgun shot himself in the throat.',
                'shooting himself to death with gun carried in his breast pocket.',
                'getting crushed while moving a fridge freezer.',
                'getting crushed by his own coffins.',
                'getting crushed by your partner.',
                'laughing so hard at The Goodies Ecky Thump episode that he died of heart failure.',
                'getting run over by his own vehicle.',
                'car engine bonnet shutting on there head.',
                'tried to brake check a train.',
                'dressing up as a cookie and cookie monster ate them.',
                'tried to react Indiana Jones, died from a snake bite.',
                'tried to short circuit me, not that easy retard'
                ]
        await ctx.send(embed=discord.Embed(
            colour=discord.Colour.red(),
            description='{} was killed by {}'.format(user.display_name, random.choice(died))
        ).set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url))


    @commands.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def annoy(self, ctx, member: discord.Member = None):
        if not member:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send('Please ping a user.')

        if ctx.message.content == '<@!{}>'.format(member.id):
          return await ctx.send('I will have to ping him for you!\n{}'.format(member.mention))
        await ctx.send('You have successfully pinged {}'.format(member))

    #@commands.command()
    #@commands.cooldown(1, 20, commands.BucketType.user)
    #@commands.bot_has_guild_permissions(manage_messages=True, embed_links=True)
    #async def fight(self, ctx, user: discord.Member = None):
    #    global user2, user1, go_first
    #    if not user or user == ctx.author:
    #        ctx.command.reset_cooldown(ctx)
    #        return await ctx.send(embed=discord.Embed(
    #            description='Need to give a user to fight!',
    #            colour=discord.Colour.red()
    #        ))
    #    if user.bot:
    #        ctx.command.reset_cooldown(ctx)
    #        return await ctx.send(embed=discord.Embed(
    #            description='You have to fight an actual user!',
    #            colour=discord.Colour.red()
    #        ))
#
    #    msg = await ctx.send(embed=discord.Embed(
    #        description='Setting up the match! {} VS {}'.format(ctx.author, user),
    #        colour=discord.Colour.red()
    #    ))
    #    await msg.add_reaction('👊'), await msg.add_reaction('🛡️'), await msg.add_reaction('🚪')
    #    holder = []
    #    user1 = 100
    #    user2 = 100
#
#
    #    def check1(m):
    #        if m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) in ['🚪', '🛡️', '👊']:
    #            holder.append(str(m.emoji))
    #            return True
    #        return False
#
    #    def check2(m):
    #        if m.user_id == user.id and m.message_id == msg.id and str(m.emoji) in ['🚪', '🛡️', '👊']:
    #            holder.append(str(m.emoji))
    #            return True
    #        return False
    #    
    #    async def user_2():
    #        global user2, user1
    #        try:
    #            await self.bot.wait_for('raw_reaction_add', timeout=20.0, check=check2)
    #        except asyncio.TimeoutError:
    #            await msg.clear_reactions()
    #            return await msg.edit(embed=discord.Embed(
    #                description='Looks like **{}** doesn\'t want to fight...'.format(user),
    #                colour=discord.Colour.red()
    #            ))
    #        emoji = holder.pop(0)
    #        if emoji == '🚪':
    #            await msg.clear_reactions()
    #            return await msg.edit(embed=discord.Embed(
    #                description='Looks like **{}** doesn\'t want to fight...'.format(user),
    #                colour=discord.Colour.red()
    #            ))
    #        elif emoji == '🛡️':
    #            if user2 == 100:
    #                await user_2()
    #                await msg.edit(embed=discord.Embed(
    #                    description='Your still on **100** HP! Retry again...',
    #                    colour=discord.Colour.red()
    #                ))
    #                await msg.remove_reaction(emoji, ctx.author)
    #            else:
    #                increase = random.randrange(100-user2)
    #                user2 += increase
    #                await msg.edit(embed=discord.Embed(
    #                    description='You gained **{}** HP'.format(increase),
    #                    colour=discord.Colour.green()
    #                ))
    #                await msg.remove_reaction(emoji, ctx.author)
    #        elif emoji == '👊':
    #            dmg = random.randrange(15, 30)
    #            if user1 - dmg < 0:
    #                await msg.clear_reactions()
    #                return await msg.edit(embed=discord.Embed(
    #                    description='**{}** smacked up **{}** and won!'.format(user, ctx.author),
    #                    colour=discord.Colour.green()
    #                ))
    #            else:
    #                user1 -= dmg
    #                await msg.edit(embed=discord.Embed(
    #                    description='**{}** smacks **{}** and deals **{}** damage.'.format(user, ctx.author, dmg)
    #                ))
    #            await msg.remove_reaction(emoji, ctx.author)
#
    #    async def user_1():
    #        global user2, user1
    #        try:
    #            await self.bot.wait_for('raw_reaction_add', timeout=20.0, check=check1)
    #        except asyncio.TimeoutError:
    #            await msg.clear_reactions()
    #            return await msg.edit(embed=discord.Embed(
    #                description='Looks like **{}** doesn\'t want to fight...'.format(ctx.author),
    #                colour=discord.Colour.red()
    #            ))
    #        emoji = holder.pop(0)
    #        if emoji == '🚪':
    #            await msg.clear_reactions()
    #            return await msg.edit(embed=discord.Embed(
    #                description='Looks like **{}** doesn\'t want to fight...'.format(ctx.author),
    #                colour=discord.Colour.red()
    #            ))
    #        elif emoji == '🛡️':
    #            try:
    #                increase = random.randrange(100-user1)
    #            except ValueError:
    #                await msg.edit(embed=discord.Embed(
    #                    description='Your still on **100** HP! Retry again...',
    #                    colour=discord.Colour.red()
    #                ))
    #                await asyncio.sleep(2)
    #                await user_2()
    #            user1 += increase
    #            await msg.edit(embed=discord.Embed(
    #                description='You gained **{}** HP'.format(increase),
    #                colour=discord.Colour.green()
    #            ))
    #            await msg.remove_reaction(emoji, ctx.author)
    #        elif emoji == '👊':
    #            dmg = random.randrange(15, 30)
    #            if user2 - dmg <= 0:
    #                await msg.clear_reactions()
    #                return await msg.edit(embed=discord.Embed(
    #                    description='**{}** smacked up **{}** and won!'.format(ctx.author, user),
    #                    colour=discord.Colour.green()
    #                ))
#
    #            else:
    #                user2 -= dmg
    #                await msg.edit(embed=discord.Embed(
    #                    description='**{}** smacks **{}** and deals **{}** damage.'.format(ctx.author, user, dmg)
    #                ))
    #            await msg.remove_reaction(emoji, ctx.author)
#
    #    go_first = True
    #    if random.choice(['y', 'n']) == 'y':
    #        go_first = False
#
    #    async def game_loop():
    #        x = 0
    #        await msg.edit(embed=discord.Embed(
    #            description='**{}** Your up.'.format(user if x % 2 == 0 else ctx.author)
    #        ).set_footer(text='{}: {} | {}: {}'.format(ctx.author, user1, user, user2)))
    #        while True:
    #            if x % 2 == 0:
    #                await user_2()
    #            else:
    #                await user_1()
    #            x += 1
    #            await asyncio.sleep(2)
    #            await msg.edit(embed=discord.Embed(
    #                description='**{}** Your up.'.format(user if x % 2 == 0 else ctx.author)
    #            ).set_footer(text='{}: {} | {}: {}'.format(ctx.author, user1, user, user2)))
    #    self.bot.loop.create_task(game_loop())

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def wide(self, ctx, *, text):
      """Widen your text"""
      await ctx.send(' '.join([x for x in text]))

    @commands.command()
    async def beerparty(self, ctx): 
        em = discord.Embed(title = "Beer Invitation 🍻", color = ctx.author.color)
        em.add_field(name = "Time Left to join:", value = f"`10s`")
        em.add_field(name=  "Inviter:", value = f"{ctx.author.mention}")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        msg = await ctx.send(embed = em)
        await msg.add_reaction("🍺")
        await asyncio.sleep(10)
        users = await msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        if len(users) == 0:
            em = discord.Embed(title = '<:fail:761292267360485378> Beer Party Failed', color = ctx.author.color)
            em.add_field(name = "Reason:", value = "No one joined D:")
            em.add_field(name = "Next steps:", value = "Dont make a party which you don't enter!")
            await ctx.channel.send(embed = em)
            return        
        msg = f"```diff\n+ {ctx.author.name} hosts a beer party\n\n"
        for user in users:
            died = random.randint(0, 1)
            if died == 0:
                msg += f"- {ctx.name} died cause of drinking too much\n"
            if died == 1:
                msg += f"- {user.name} had a nice time at the bar\n"
        msg += "```"

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def respect(self, ctx, *, reason = None):
        em = discord.Embed(title = f'{ctx.author.name} gives respect!', color = ctx.author.color)
        em.add_field(name = "Reason:", value = f"{choice(['🤎','🧡', '💚', '💙', '💜'])} {reason}")
        em.add_field(name = "Respected Command Author:", value = f"{ctx.author.name}")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def thank(self, ctx, member: discord.Member = None, *, reason = None):
        if member is None:
            return await ctx.send("Provide a valid member!")
        elif reason is None:
            return await ctx.send("Provide a valid reason after the member!")
        elif member == ctx.author:
            return await ctx.send('You cannot thank yourself!')
        
        thanks = discord.Embed(title = f"{ctx.author.name} thanks someone!", color = ctx.author.color)
        thanks.add_field(name = "Member:", value = f"{member.mention}")
        thanks.add_field(name = 'Reason:', value = f"{reason}")
        thanks.add_field(name = 'User:', value = f"{ctx.author.mention}")
        return await ctx.send(embed = thanks)


    @commands.command(aliases=['F'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ff(self, ctx, *, message: str = None):
        if message == None:
            await ctx.send('<:f_key:585955067010744320>')
            return await ctx.send('**{} Has Paid Their Respects.**'.format(ctx.author.display_name))
        await ctx.send('<:f_key:585955067010744320>')
        await ctx.send('**{} Has Paid Their Respects:** {}'.format(ctx.author.display_name, message.title()))

    @commands.command(aliases=['spin'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def colorspin(self, ctx):
      self.msg_id = 0
      emojis = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴",   "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢",   "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤",   "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠",  "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵",  "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫",   "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡",   "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣",   "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "🔴",  "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫"]
  
      i = 0
  
      embed = discord.Embed(
        title = "COLORSPIN",
        description = f"{emojis[0 + i]} {emojis[1 + i]} {emojis[2 + i]} {emojis[3 + i]} {emojis[4 + i]} {emojis[5 + i]}   {emojis[6 + i]} {emojis[7 + i]}"
      )
      embed.set_footer(text="Just delete this embed to stop the colorspin ;)")
      msg = await ctx.send(embed=embed)
      await asyncio.sleep(0.5)
      self.msg_id = msg.id
  
      for i in range(100):
        i += 1
        embed = discord.Embed(
        title = "COLORSPIN",
        description = f"{emojis[0 + i]} {emojis[1 + i]} {emojis[2 + i]} {emojis[3 + i]} {emojis[4 + i]} {emojis[5 + i]}   {emojis[6 + i]} {emojis[7 + i]}"
        )
        embed.set_footer(text="Just delete this embed to stop the colorspin ;)")
        await msg.edit(embed=embed)
        await asyncio.sleep(0.5)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def bird(self,ctx):
      url = "https://some-random-api.ml/img/birb"
      response = requests.request("GET", url).json()
      final_dog =  response['link']
      embed=discord.Embed(title='Bird',description='AWWWWWW',colour=discord.Colour.blue())
      embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
      embed.set_image(url=final_dog)
      await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def koala(self,ctx):    
      url = "https://some-random-api.ml/img/koala"    
      response = requests.request("GET", url).json()    
      final_dog =  response['link']
      embed=discord.Embed(title='Koala',description='AWWWWWW',colour=discord.Colour.blue())
      embed.set_footer(text=f'{ctx.author.name} asked me...Dont Blame me',icon_url=f'{ctx.author.avatar_url}')
      embed.set_image(url=final_dog)
      await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def parent(self, ctx):
        parents = ['Left you when they were young',
                   'There still with you.',
                   'Dad went to  get the milk. idk were hes gone',
                   'Mommys boy. HAHAHA',
                   'Idk mate. You were adopted',
                   ]
        await ctx.send(f'{random.choice(parents)}')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Wobbler(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        else:
            pass
        number = random.randint(1, 101)
        embed = discord.Embed(
            title='**Do {} walk straight??**'.format(user),
            color=discord.Color.purple()
        )
        embed.add_field(name='‏‏‎ ‎', value=f'{number}% a Wobbler.')
        if number > 50:
            embed.add_field(name='‏‏‎ ‎', value='\n\nLearn to walk. LMFAO')
        else:
            embed.add_field(name='‏‏‎ ‎', value='\n\n{} parents did a good job. I think. ;-;'.format(user))
        await ctx.send(embed=embed)


    @commands.command(aliases=['diprate', 'dip',])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stabrate(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        else:
            pass
        chance = random.randint(1, 101)
        embed = discord.Embed(
            title='**Chances of {} getting stabbed:**'.format(user),
            color=discord.Color.blue()
        )
        embed.add_field(name='‏‏‎ ', value='The chance of {} getting stabbed is {}%.'.format(user, chance))
        if chance < 50:
            embed.add_field(name='‏‏‎ ', value='\nLooks like {} gonna live another day..'.format(user), inline=False)
        else:
            embed.add_field(name='‏‏‎ ', value='\nWell Good luck.', inline=False)
        await ctx.send(embed=embed)


    @commands.command(aliases=['begr', 'Brate'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def begrate(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        else:
            pass
        begrate = random.randint(1, 101)
        embed = discord.Embed(
            title='**How much of a beg are {}!!!!**'.format(user),
            color=discord.Color.blue()
        )
        embed.add_field(name='‏‏‎ ', value=f'{user} are **{begrate}%** a beg')
        if begrate < 50:
            embed.add_field(name='‏‏‎ ', value='{} is not a beg.'.format(user))
        else:
            embed.add_field(name='‏‏‎ ', value='Watch out {} is a beg!'.format(user))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def odds(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        else:
            pass
        odd = ['homeless', 'a chippie', 'lost', 'rich', 'disabled', 'unwanted', 'loved', 'wanted']
        counter = random.randint(1, 101)
        emoji = ['😭','😰','<:trashcan:744626891948032124>','😥','😬','🤐','<:you_wot:748867944649588776>','<:birdonem:744615651645063219>','👍']
        embed = discord.Embed(
            title=f'The odds of {user} becoming {random.choice(odd)}',
            color=discord.Color.purple(),
            description=f'**{counter}%** {random.choice(emoji)}'
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['le'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lifeexpectancy(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        else:
            pass
        counter = random.randint(1, 150)
        embed = discord.Embed(
            title="{}'s life expectancy is:".format(user),
            color=discord.Color.red(),
            description=f'**{counter} yrs old!**'
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["boxingweight"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def BWeight(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        else:
            pass
        weight = ['Pinweight\t(44 - 46 Kg)', 'Light Flyweight\t(Below 48Kg)', 'Flyweight\t(49 - 52 Kg)', 'Bantamweight\t(52 - 53.5 Kg)', 'Featherweight\t(54 - 57 Kg)', 'Lightweight\t(59 - 61 Kg)', 'Lighter welterweight\t(54 - 67 Kg)', 'Welterweight\t(64 - 69 Kg)', 'Middleweight\t(70 - 73 Kg)', 'Light heavyweight\t(76 - 80 Kg)', 'Heavyweight\t(Above 81 Kg)', 'Super Heavyweight\t(Above 91 Kg)']
        choice = random.choice(weight)
        embed = discord.Embed(
            title='What is {} boxing weight?'.format(user),
            color=discord.Color.red(),
            description=f'{choice}'
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['Weight', 'WI'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def WeighIn(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        else:
            pass
        weight = random.randint(1, 200)
        if weight > 150:
            msg = 'Loose some weight bruv!'
        embed = discord.Embed(
            title='How much do you weigh?',
            color=discord.Color.red(),
            description=f'**`{weight}` Kg**'
        )
        await ctx.send(embed=embed)
        await ctx.send(msg)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def PunchMachine(self, ctx):
        answer = random.randint(0, 999)

        responce = ['**Nice shot bro**',
                    '**Did you miss the machine**',
                    '**DAHM HAVE SOME MERCY**',
                    '**Even a baby can hit harder**',
                    '**Weakling lmfao**',
                    '**You wasted money to get that score**',
                    ]
        embed = discord.Embed(
            title='',
            color=discord.Color.default()
        )
        embed.add_field(name='**Punch MACHINE**',
                        value=f'\n\n*You swing and hit*\n\n**{answer}**\n\n*The crowd around you:*\n\n{random.choice(responce)}')
        await ctx.send(embed=embed)

    @commands.command()
    async def horror(self, ctx, limit: int = 5):
        """spoopy"""
        posts = []
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://www.reddit.com/r/twosentencehorror/hot.json") as r:
                res = await r.json()
            for i in res['data']['children']:
                posts.append(i['data'])
            counter = 0
            embeds = []
            async with ctx.typing():
                for s in random.sample(posts, len(posts)):
                    text = cyberformat.shorten(f"{s['title']}\n{s['selftext']}")
                    embeds.append(discord.Embed(description=text[:2000], colour=self.client.colour))
                    counter += 1
                    if counter == limit:
                        break
                    else:
                        continue
        p = paginator.CatchAllMenu(paginator.EmbedSource(embeds))
        await p.start(ctx)
    
    @commands.has_permissions(manage_guild=True)
    @commands.command()
    async def echo(self, ctx, channel: discord.TextChannel, *, message):
        await channel.send(
            cyberformat.hyper_replace(text=message, old=['@everyone', '@here'], new=['@\u200beveryone', '@\u200bhere']))
        await ctx.message.add_reaction(emoji="<:tickYes:845618396007759893>")

    @commands.command(aliases=['gt'])
    async def greentext(self, ctx):
        """Write a greentext story"""
        story = []
        await ctx.send(
            f"Greentext story starting! Type `{ctx.prefix}quit` or `{ctx.prefix}exit` to stop the session, or `{ctx.prefix}finish` to see your final story!")
        try:
            while True:
                message = await self.client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=500)
                async with timeout(500):
                    if message.content == f"{ctx.prefix}quit":
                        await ctx.send("Session exited.")
                        return
                    elif message.content == f"{ctx.prefix}exit":
                        await ctx.send("Session exited.")
                        return
                    elif message.content == f"{ctx.prefix}finish":
                        final_story = "\n".join(story)
                        await ctx.send(f"**{ctx.author}**'s story\n```css\n" + final_story + "```")
                        return
                    else:
                        story.append(">" + message.content)
                        await message.add_reaction(emoji=self.tick)
        except asyncio.TimeoutError:
            final_story = "\n".join(story)
            await ctx.send(f"**{ctx.author}**'s story\n```css\n" + final_story + "```")

    @commands.command(name='paginated_help', aliases=['phelp'])
    async def phelp(self, ctx, *, command=None):
        """
        If you don't like the regular help command
        """
        embeds = []
        use = self.client.get_command(command) if command else None
        lcogs = [str(cog) for cog in self.client.cogs]
        if not command:
            for name, obj in self.client.cogs.items():
                embed = discord.Embed(title=f"{name} Commands", colour=self.client.colour)
                cmds = []
                for cmd in obj.get_commands():
                    cmds.append(f"→ `{cmd.name} {cmd.signature}` | {cmd.help}")
                embed.description = '\n'.join(cmds)
                if cmds:
                    embeds.append(embed)
                else:
                    continue
            pages = paginator.CatchAllMenu(paginator.EmbedSource([discord.Embed(colour=self.client.colour,
                                                                                title=f'{self.client.user.name} Help',
                                                                                description=f'Do `{ctx.prefix}help command/cog` for more info').set_image(
                url=self.client.user.avatar_url)] + embeds))
            await pages.start(ctx)
        elif command in lcogs:
            embed = discord.Embed(colour=self.client.colour, title=f'{command.capitalize()} Help')
            embed.description = '\n'.join(
                [f"→ `{cmd.name} {cmd.signature}` | {cmd.help}" for cmd in self.client.cogs[command].get_commands()])
            await ctx.send(embed=embed)
        elif command and use:
            help_msg = use.help or "No help provided for this command"
            parent = use.full_parent_name
            if len(use.aliases) > 0:
                aliases = '|'.join(use.aliases)
                cmd_alias_format = f'{use.name}|{aliases}'
                if parent:
                    cmd_alias_format = f'{parent} {cmd_alias_format}'
                alias = cmd_alias_format
            else:
                alias = use.name if not parent else f'{parent} {use.name}'
            embed = discord.Embed(title=f"{alias} {use.signature}", description=help_msg, colour=self.client.colour)
            if isinstance(use, commands.Group):
                embed = discord.Embed(title=f"{alias} {use.signature}", description=help_msg,
                                      colour=self.client.colour)
                for sub_cmd in use.commands:
                    u = '\u200b'
                    embed.add_field(
                        name=f"{use.name} {sub_cmd.name}{'|' if sub_cmd.aliases else u}{'| '.join(sub_cmd.aliases)} {sub_cmd.signature}",
                        value=f"{sub_cmd.help}", inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=embed)
        elif command not in lcogs or command and not use:
            await ctx.send("not found")

    @commands.command()
    async def story(self, ctx):
        channel = ctx.message.channel
        author = ctx.message.author
        def check(m):
            return m.channel == channel and m.author == author
        await ctx.send("Enter a body organ")
        Organ = await self.client.wait_for('message', check=check)
        await ctx.send("Enter an adjective")
        Adj1 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a verb")
        Verb1 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a plural noun")
        plNoun1 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another plural noun")
        plNoun2 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another plural noun")
        plNoun3 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj2 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj3 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another plural noun")
        plNoun4 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a container")
        Container = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj4 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a noun")
        Noun1 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj5 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj6 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a number")
        Number = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj7 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter an adverb")
        Adverb = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another noun")
        Noun2 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another verb")
        Verb2 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj8 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter an event")
        Event = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another verb")
        Verb3 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj9 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter an exclamation")
        Excl = await self.client.wait_for('message', check=check)
        mainStory = "Many say that " + str(Organ.clean_content) + " storming is " + str(Adj1.clean_content) + " and does not "\
                    + str(Verb1.clean_content) + ". However, with the combination of the right " + str(plNoun1.clean_content) + \
                    ", " + str(plNoun2.clean_content) + " and " + str(plNoun3.clean_content) + " anyone can lead a " + \
                    str(Adj2.clean_content) + " session. When you have pulled together a " + str(Adj3.clean_content) + " group of " +\
                    str(plNoun4.clean_content) + " brought together in a " + str(Container.clean_content) + " that is " + \
                    str(Adj4.clean_content) + " and have a " + str(Noun1.clean_content) + " that is " + str(Adj5.clean_content) \
                    + " for the participants to suggest " + str(Adj6.clean_content) + " ideas, you will yield " +\
                    str(Number.clean_content) + " more " + str(Adj7.clean_content) + " ideas. Next time you need " + \
                    str(Adverb.clean_content) + " thought-up ideas for a " + str(Noun2.clean_content) + ", a way to " + \
                    str(Verb2.clean_content) + " sales for your business, or even " + str(Adj8.clean_content) + " ideas for activities for the company "\
                    + str(Event.clean_content) + ", put these suggestions to work and let the ideas " + str(Verb3.clean_content)\
                    + ". With so many " + str(Adj9.clean_content) + " ideas you'll have the boss declaring " + \
                    str(Excl.clean_content) + " in no time!"
        await ctx.send(mainStory)



def setup(bot):
    bot.add_cog(Errors(bot))