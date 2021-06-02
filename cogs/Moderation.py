import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import has_permissions, CheckFailure, bot_has_permissions
from errorembed import ErrorEmbed
import datetime

class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

# Events
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
         embed = discord.Embed(title="❌ Member not found!", name="Enter a valid member", colour=discord.Colour.red())
         await ctx.send(embed=embed)
        if isinstance(error, commands.BotMissingPermissions):
          embed = discord.Embed(title=f'❌ I do not have permission to do this! {error}', colour=discord.Colour.red())
          await ctx.send(embed=embed)
        if isinstance(error, commands.CommandOnCooldown):
          msg = 'This command on cooldown please try again in {:.2f}s!'.format(
            error.retry_after)
          await ctx.send(msg)

# Commands
    @commands.command(aliases = ['boot', 'yeet'])
    @bot_has_permissions(kick_members=True)
    @commands.cooldown(per=5, rate=1)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
     if ctx.author.top_role.position <= member.top_role.position:
       return await ctx.send("You can't kick someone higher or equal to you in the roles hierarchy. ")
     if ctx.author.top_role.position > member.top_role.position: 
      embed=discord.Embed(title='Kick:', description=f"👞You were kicked in {ctx.guild.name}!",colour=discord.Colour.red())
      embed.add_field(name="Reason:",value=reason,inline=False)
      embed.add_field(name="Responsible Moderator:",value=f"{ctx.author.name}",inline=False)
      await member.send(embed=embed)
      await member.kick(reason=reason)
      embed = discord.Embed(title="Kick:", description=f"✅Successfully kicked {member.name}!", colour=discord.Colour.blue())
      embed.add_field(name="Reason:", value=reason, inline=False)
      embed.add_field(name="Responsible Moderator:",value=f"{ctx.author.mention}",inline=False)
      await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def hackban(self, ctx, user_id: int, *, reason=None):
       await ctx.guild.ban(discord.Object(id=user_id), reason=reason)
       await ctx.send(f'*{self.bot.get_user(user_id)}* just got hackbanned!')


    @bot_has_permissions(manage_nicknames=True)
    @commands.cooldown(per=5, rate=1)
    @commands.command(aliases = ['nick', 'n', 'nickset'])
    async def nickname(self, ctx, member: discord.Member, *, nick = None):
        if not ctx.author.guild_permissions.manage_nicknames:
            await ctx.send("You do not have the permissions to use this command.")
            return
        if nick and len(nick) < 2:
            await ctx.send("That nickname is too short. It must be 2 characters or more.")
            return
        if nick and len(nick) > 32:
            await ctx.send("That nickname is too long. It must be 32 characters or less.")
            return
        previous_name = member.display_name
        try:
            await member.edit(nick = nick)
        except Exception:
            print(Exception)
            await ctx.send("I cannot nickname this member.")
            return
        if not nick:
            await ctx.send(f"{previous_name}'s nickname was reset.")
        else:
            await ctx.send(f"{previous_name} was nicknamed {nick}.")
    
    @nickname.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed=discord.Embed(title='❌Error, missing required arguments:', description='f!nickname [Member] [Nick]', colour=discord.Colour.red())
          embed.add_field(name='Example:',value='```f!nickname <user> <nick>```')
          await ctx.send(embed=embed)

    @commands.command(aliases=['bon, hammer'])
    @bot_has_permissions(ban_members=True)
    @commands.cooldown(per=5, rate=1)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
      if ctx.author.top_role.position <= member.top_role.position:
        return await ctx.send("You can't ban someone higher or equal to you in the roles hierarchy. ")
      elif ctx.author.top_role.position > member.top_role.position:
        embed = discord.Embed(title="Ban:", description=f"🔨You were banned in {ctx.guild.name}!", colour=discord.Colour.red())
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.add_field(name="Responsible Moderator:", value=f'{ctx.author.name}', inline=False)
        await member.send(embed=embed)
        await member.ban(reason = reason, delete_message_days = 0)
        embed = discord.Embed(title="Ban:", description=f"✅Successfully banned {member.name}!", colour=discord.Colour.blue())
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.add_field(name="Responsible Moderator:", value=f'{ctx.author.mention}', inline=False)
        await ctx.send(embed=embed)


    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=["purge"])
    async def clear(self, ctx, number: int):
        msg = "message"
        if number != 1:
            msg+='s'
        amt = await ctx.channel.purge(limit = (int(number) + 1))
        await asyncio.sleep(1)
        clearConfirmation = await ctx.send(f"**Cleared `{len(amt) - 1}` {msg} from this channel**", delete_after=4.0)
        await clearConfirmation.add_reaction("<:tickYes:315009125694177281>")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!purge [number of messages]', colour=discord.Colour.red())
          embed.add_field(name='Example:',value='```f!purge 5```')
          await ctx.send(embed=embed)
      

    @clear.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @bot_has_permissions(manage_messages=True)
    @commands.cooldown(per=5, rate=1)
    async def unmute(self ,ctx, member: discord.Member):
     mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
     if ctx.author.top_role.position <= member.top_role.position:
       return await ctx.send("You can't unmute someone higher or equal to you in the roles hierarchy. ")
     if ctx.author.top_role.position > member.top_role.position:
       await member.remove_roles(mutedRole)
       embed = discord.Embed(title=f"Unmute:", description=f"Successfully unmuted {member.mention}!",colour=discord.Colour.blue())
       await ctx.send(embed=embed) 
       embed = discord.Embed(title = "Unmute:", description=f"You were unmuted in {ctx.guild.name}!", colour=discord.Colour.blue())
       await member.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!unmute [Member]', colour=discord.Colour.red())
          embed.add_field(name='Example:',value='```f!unmute <user>```')
          await ctx.send(embed=embed)
    

    @commands.command(aliases=['sm', 'slowm'])
    @commands.cooldown(per=5, rate=1)
    @commands.has_permissions(manage_channels=True)
    @bot_has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
     if seconds == 0:
        await ctx.channel.edit(slowmode_delay=0)
        await ctx.send('Slowmode has turned `off`.')
     else:
      await ctx.channel.edit(slowmode_delay=seconds)
      await ctx.send(f"Successfully set the slowmode to `{seconds}` seconds.")

    @commands.command()
    @bot_has_permissions(ban_members=True)
    @commands.cooldown(per=5, rate=1)
    @has_permissions(ban_members=True)
    async def softban(self, ctx, member : discord.Member, *, reason = None):
     if ctx.author.top_role.position <= member.top_role.position:
       return await ctx.send("You can't softban someone higher or equal to you in the roles hierarchy. ")
     if ctx.author.top_role.position > member.top_role.position:
       embed = discord.Embed(title="Ban:", description=f"🔨You were banned in {ctx.guild.name}!", colour=discord.Colour.red())
       embed.add_field(name="Reason:", value=reason, inline=False)
       embed.add_field(name="Responsible Moderator:", value=f'{ctx.author.name}', inline=False)
       await member.send(embed=embed)
       await member.ban(reason = reason, delete_message_days = 7)
       embed = discord.Embed(title="Ban:", description=f"✅Successfully banned {member.name}!", colour=discord.Colour.blue())
       embed.add_field(name="Reason:", value=reason, inline=False)
       embed.add_field(name="Responsible Moderator:", value=f'{ctx.author.mention}', inline=False)
       await ctx.send(embed=embed)

    @kick.error
    async def softban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!softban [Member] [Reason]', colour=discord.Colour.red())
          embed.add_field(name='Example:',value='```f!softban <user> <reason>```')
          await ctx.send(embed=embed)
      

    @commands.command(aliases=['forgive', 'unbon', 'unyeet'])
    @commands.cooldown(per=5, rate=1)
    @has_permissions(ban_members=True)
    async def unban(self, ctx, id: int, *,reason=None):
         user = await self.client.fetch_user(id)
         await ctx.guild.unban(user)
         embed = discord.Embed(title="Unban:", description=f"✅Successfully unbanned {user.name}!", colour=discord.Colour.blue())
         embed.add_field(name="Reason:", value=reason, inline=False)
         embed.add_field(name="Responsible Moderator:", value=f'{ctx.author.mention}', inline=False)
         await ctx.send(embed=embed)

    @commands.command(aliases = ['l'])
    @commands.has_permissions(manage_channels = True)
    @bot_has_permissions(administrator=True)
    async def lock(self, ctx):
     await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
     await ctx.send( ctx.channel.mention + " has been successfully locked! :white_check_mark:")
   
    @commands.command(aliases = ['ul'])
    @commands.has_permissions(manage_channels=True)
    @bot_has_permissions(administrator=True)
    async def unlock(self, ctx):
     await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
     await ctx.send(ctx.channel.mention + " has been successfully unlocked! :white_check_mark:")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx, channel: discord.TextChannel=None):
        if channel == None:
            channel = ctx.channel

        em=discord.Embed(title="THIS CHANNEL HAS BEEN NUKED", color=discord.Color.red())
        em.set_image(url="https://images-ext-2.discordapp.net/external/JNt33sq5EYYGo-xdL75c7PROOZ3KAMyaB9LAAMXigY8/https/i.pinimg.com/originals/47/12/89/471289cde2490c80f60d5e85bcdfb6da.gif")
        pos = channel.position
        await channel.delete()
        channels = await channel.clone()
        await channels.edit(position=pos)
        await channels.send(embed=em)
        await ctx.send("Successfuly nuked the channel")

    #@commands.command(aliases = ["hush", "shut"])
    #@commands.has_permissions(manage_messages=True)
    #@commands.cooldown(per=5, rate=1)
    #@bot_has_permissions(manage_roles=True)
    #async def mute(self, ctx, member: discord.Member, *, reason=None):
    #   if ctx.author.top_role.position <= member.top_role.position:
    #    return await ctx.send("You can't mute someone higher or equal to you in the roles hierarchy. ")
    #   if ctx.author.top_role.position > member.top_role.position: 
    #    guild = ctx.guild
    #    mutedRole = discord.utils.get(guild.roles, name="Muted")
#
    #    if not mutedRole:
    #        mutedRole = await guild.create_role(name="Muted")
    #        
    #        for channel in guild.channels:
    #            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, #read_messages=True)
    #    embed = discord.Embed(title="Mute", description=f"✅Successfully muted {member.mention} for {reason}!", #colour=discord.Colour.blue())
    #    embed.add_field(name="reason:", value=reason, inline=False)
    #    await ctx.send(embed=embed)
    #    await member.add_roles(mutedRole, reason=reason)
    #    embed=discord.Embed(title='Mute', description=f"You has been muted in {guild.name}.")
    #    embed.add_field(name="Reason:", value=f"{reason}")
    #    await member.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!kick [Member] [Reason]', colour=discord.Colour.red())
          embed.add_field(name='Example:',value='```f!kick <user> <reason>```')
          await ctx.send(embed=embed)
      
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!ban [Member] [Reason]', colour=discord.Colour.red())
          embed.add_field(name="Syntax:", value="```f!ban <user>```")
          await ctx.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!unban [Member] [Reason]', colour=discord.Colour.red())
          embed.add_field(name="Syntax:", value="```f!unban <user>```")
          await ctx.send(embed=embed)

    @softban.error
    async def softban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
         embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!softban [Member] [Reason]', colour=discord.Colour.red())
        embed.add_field(name="Syntax:", value="```f!softban <user> <reason>```")
        await ctx.send(embed=embed)
    
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
         embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!unmute [Member]', colour=discord.Colour.red())
        embed.add_field(name="Syntax:", value="```f!unmute <user>```")
        await ctx.send(embed=embed)

    @slowmode.error
    async def slowmode_error(self, ctx, error):
       if isinstance(error, commands.MissingRequiredArgument):
         embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!slowmode [Seconds]', colour=discord.Colour.red())
         embed.add_field(name='Syntax:',value='```f!slowmode <time>```')
         await ctx.send(embed=embed)

    @slowmode.error
    async def createrole_error(self, ctx, error):
       if isinstance(error, commands.MissingRequiredArgument):
         embed=discord.Embed(title='❌Error, missing required arguments:', description=f'f!createchannel [Name]', colour=discord.Colour.red())
         embed.add_field(name='Syntax:',value='```f!createchannel <channel name>```')
         await ctx.send(embed=embed)

    @commands.command(aliases = ["makerole", "cr", "creater"])
    @bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def createrole(self, ctx, *, name = "UnknownRole"):
        role=  await ctx.guild.create_role(name = name)
        em = discord.Embed(title = "<a:greentick:843851431512768543> Role Created", color = ctx.author.color, description = f"{role.mention} was successfully created!")
        em.add_field(name = "Role:", value = f"{role.mention}")
        em.add_field(name ="Moderator:", value = f"{ctx.author.mention}")
        em.set_footer(text = "f!vote 😏")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

    @createrole.error
    async def createrole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<a:NO:800658193033592882> Role Creation Failed")
            em.add_field(name = "Reason:", value = "`Manage Roles perms missing!`")
            em.set_footer(text = "Imagine thinking you have the perms!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<a:NO:800658193033592882> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||a dummy!||")
            em.add_field(name = 'Insufficient Perms', value = 'Give __ALL__ the permissions asked for when adding me')
            em.set_footer(text = "f!bot for more info!", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.guild_only()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    @commands.command(aliases = ["addrole", "grole", "gr"])
    async def giverole(self, ctx, user : discord.Member, *, role : discord.Role):
        if ctx.author.top_role > user.top_role or ctx.author == ctx.guild.owner:
            await user.add_roles(role)
            msg = await ctx.send(f"**The `{role}` role was added to {user.mention}**")
            await msg.add_reaction("a:tick:")



    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases = ['deletechannel', 'delete-channel'])
    @bot_has_permissions(manage_channels=True)
    @commands.has_permissions(manage_channels = True)
    async def delete_channel(self, ctx, channel: discord.TextChannel = None):

        if channel == None:
            channel = ctx.channel

        msg = await ctx.send(f"Deleting `{channel}`... <a:3859_Loading:754710375446085754>")
        await channel.delete()
        await msg.edit(content = f"Deleted `{channel}` <a:greentick:843851431512768543>")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(administrator = True)
    @bot_has_permissions(manage_channels=True)
    async def massrole(self, ctx, *, role):
            members = ctx.guild.members
            for member in members:
                try:
                    await member.add_role(role=role)
                except:
                    await ctx.send(f"Couldn't add the role to {member.name} ")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(administrator = True)
    @bot_has_permissions(manage_guild=True)
    async def massnick(ctx, *, nick):
            members = ctx.guild.members
            for member in members:
                try:
                    await member.edit(nick=nick)
                except:
                    await ctx.send(f"Couldn't edit {member.name}'s' nickname ")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases = ['createchannel', 'create-channel'])
    @commands.has_permissions(manage_channels = True)
    async def create_channel(self, ctx, channelName = None):

        if channelName == None:
            await ctx.message.reply(f"You didn't mention what name you want the channel to have, please try again.")
            return

        msg = await ctx.send(f"Creating `{channelName}`... <a:3859_Loading:754710375446085754> ")
        await ctx.guild.create_text_channel(name = channelName)
        await msg.edit(content = f"Created `{channelName}` <:tickYes:454716382886494208>")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def botkick(self, ctx, member : discord.Member, *, reason=None):

        if int(ctx.author.top_role.position) < int(member.top_role.position):
            await ctx.send(f"The bot you are trying to kick has a higher role than you, so you can't kick them.")
            return

        if int(ctx.author.top_role.position) == int(member.top_role.position):
            await ctx.send(f"The bot you are trying to kick has the same role as you, so you can't kick them.")
            return

        await member.kick(reason=reason)

        embed = discord.Embed(
            title = "👢 Bot Kicked!",
            description = f"I have kicked **{member.name}#{member.discriminator}** from this server!",
            color = 0x00FFFF
        )

        # await ctx.send(f':crossed_swords: {member.mention} was kicked.\nReason: {reason}')
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def botban(self, ctx, member : discord.Member, *, reason=None):

        if int(ctx.author.top_role.position) < int(member.top_role.position):
            await ctx.send(f"The bot you are trying to ban has a higher role than you, so you can't ban them.")
            return

        if int(ctx.author.top_role.position) == int(member.top_role.position):
            await ctx.send(f"The bot you are trying to ban has the same role as you, so you can't ban them.")
            return

        await member.ban(reason=reason)

        embed = discord.Embed(
            title = "🔨 Bot banned!",
            description = f"I have banned **{member.name}#{member.discriminator}** from this server!",
            color = 0x00FFFF
        )

        # await ctx.send(f':crossed_swords: {member.mention} was kicked.\nReason: {reason}')
        await ctx.send(embed=embed)

    @commands.command(aliases = ["hush", "shut"])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(per=5, rate=1)
    @bot_has_permissions(manage_roles=True)
    @commands.has_permissions(kick_members=True, manage_roles=True)
    async def mute(self, ctx, member: discord.Member, mute_time:str=None,*,reason: str=None):
        if member.top_role > ctx.author.top_role:
            em = discord.Embed(title="Error",description="The member has higher role than you.",color=discord.Color.red())
            await ctx.send(embed=em)
            return

        if member == ctx.author:
            em = discord.Embed(title="Error",description="You cannot mute yourself. Please mention another member to mute",color=discord.Color.red())
            await ctx.send(embed=em)
            return

        message = await ctx.send(f"Muting {member}. Please wait...\nIt will take a few seconds")

        role = discord.utils.get(ctx.guild.roles, name="Muted")

        for chan in ctx.guild.channels:
            await chan.set_permissions(role,speak=False,send_messages=False,read_message_history=True,read_messages=True)

        if not role:
            await ctx.guild.create_role(name='Muted')

            for channel in ctx.guild.channels:
                await channel.set_permissions(role,speak=False,send_messages=False,read_message_history=True,read_messages=True)

        if mute_time == None:
            if member.bot == True:
              await message.delete()
              await ctx.send(f"Muted {member} indefinitely.")
              await member.add_roles(role)
            else:
              await message.delete()
              await ctx.send(f"Muted {member} indefinitely.")
              await member.add_roles(role)
        else:
            time_unit = None
            parsed_time = None

            if 's' in mute_time:
                time_unit = 'seconds'
                parsed_time = mute_time[0:(len(mute_time) - 1)]
            elif 'm' in mute_time:
                time_unit = 'minutes'
                parsed_time = mute_time[0:(len(mute_time) - 1)]
            elif 'h' in mute_time:
                time_unit = 'hours'
                parsed_time = mute_time[0:(len(mute_time) - 1)]
            elif 'd' in mute_time:
                time_unit = 'days'
                parsed_time = mute_time[0:(len(mute_time) - 1)]

            if member.bot == True:
                await message.delete()
                await member.add_roles(role)
                await ctx.send(f"Muted {member} for {parsed_time} {time_unit}.\nReason: {reason}")

                if time_unit == 'seconds':
                    await asyncio.sleep(int(parsed_time))
                elif time_unit == 'minutes':
                    await asyncio.sleep(int(parsed_time) * 60)
                elif time_unit == 'hours':
                    await asyncio.sleep(int(parsed_time) * 3600)
                elif time_unit == 'days':
                    await asyncio.sleep(int(parsed_time) * 86400)

                await member.remove_roles(role)
                await ctx.send(f"{member} was unmuted because time's up")
            else:
                await message.delete()
                await member.add_roles(role)
                await ctx.send(f"Muted {member} for {parsed_time} {time_unit}.\nReason: {reason}")
                await member.send(f"You were muted in {ctx.guild.name} for {parsed_time} {time_unit}.\nReason: {reason}")

                if time_unit == 'seconds':
                    await asyncio.sleep(int(parsed_time))
                elif time_unit == 'minutes':
                    await asyncio.sleep(int(parsed_time) * 60)
                elif time_unit == 'hours':
                    await asyncio.sleep(int(parsed_time) * 3600)
                elif time_unit == 'days':
                    await asyncio.sleep(int(parsed_time) * 86400)

                await member.remove_roles(role)
                await ctx.send(f"Unmuted {member} because time's up")
                await member.send(f"You were unmuted in {ctx.guild.name} because time's up")

    @commands.command(aliases = ["create_vc", "create-vc"])
    @commands.has_permissions(manage_channels=True)
    async def createvc(self,ctx,channelName):
            guild = ctx.guild

            em = discord.Embed(title='Success!', description=f'{channelName} Has Been Created',color=discord.Colour.green())
            await guild.create_voice_channel(name=channelName)
            await ctx.send(embed=em)

    @commands.command(aliases = ["delete-vc", "delete_vc"])
    @commands.has_permissions(manage_channels=True)
    async def deletevc(self,ctx,vc: discord.VoiceChannel):
            em = discord.Embed(title='Success!', description=f'{vc} has been deleted' , color=discord.Colour.red())
            await ctx.send(embed=em)
            await vc.delete()

    @commands.command(aliases=['delcategory'])
    @commands.has_permissions(manage_channels=True)
    async def deletecategory(self, ctx, *, channel : commands.CategoryChannelConverter = None):
      """Delete a category."""
      if ctx.author.guild_permissions.manage_channels:
        if channel == None:
          embed = ErrorEmbed.error("Missing Command Arguments", "You need to specify a category to delete.")
          await ctx.send(embed=embed)
        else:
          embed = discord.Embed(
            title = "Category deleted",
            description = channel.name,
            color = 0x5f10a3,
            timestamp = datetime.datetime.utcnow()
          )
          await ctx.send(embed=embed)
          await channel.delete()
      else:
        embed = ErrorEmbed.error("Missing Permissions", "You need the permission of **Manage Channels** to run this   command.")
        await ctx.send(embed=embed)

    @deletecategory.error
    async def delecaterror(self, ctx, error):
      if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await ctx.send("Make sure I have **Manage Channels** perms to run that command!")

    @commands.command(aliases=['addcategory', 'makecategory'])
    @commands.has_permissions(manage_channels=True)
    async def createcategory(self, ctx, *, channelName = None):
      """Create a category."""
      if ctx.author.guild_permissions.manage_channels:
        if channelName == None:
          embed = ErrorEmbed.error("Missing Command Arguments", "You need to specify a category to create.")
          await ctx.send(embed=embed)
        else:
          embed = discord.Embed(
            title = "Category created",
            description = channelName,
            color = 0x5f10a3,
            timestamp = datetime.datetime.utcnow()
          )
          await ctx.send(embed=embed)
          await ctx.guild.create_category(name=channelName)
      else:
        embed = ErrorEmbed.error("Missing Permissions", "You need the permission of **Manage Channels** to run this   command.")
        await ctx.send(embed=embed)

    @createcategory.error
    async def ccategoryerror(self, ctx, error):
      if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await ctx.send("Make sure I have **Manage Channels** perms to run that command!")

    @commands.command(name="masskick")
    @commands.has_permissions(kick_members=True)
    async def masskick(self, ctx):
        def check(m):
            return m.author == ctx.author

        await ctx.send("How many members do you want to kick?")
        msg = await self.bot.wait_for("message", check=check)

        for i in range(int(msg.content)):
            await ctx.send("Whom do you want to kick?")
            msg2 = await self.bot.wait_for("message", check=check)
            user = msg2.mentions[0]
            if ctx.author.top_role.position <= user.top_role.position and ctx.guild.owner.id != ctx.author.id:
                await ctx.send("You cannot kick this user because their role is higher than or equal to yours.")
            else:
                await user.kick()
                await ctx.send(f"User **{user}** has been kicked.")
                await user.send(f"You have been **kicked** from **{ctx.guild}** server")


def setup(client):
    client.add_cog(Errors(client))