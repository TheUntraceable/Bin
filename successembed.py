import discord
import datetime

class SuccessEmbed:
  def success(title : str = "Success!", desc : str =  "Command executed successfully!"):
    embed = discord.Embed(
      title = title,
      description = desc,
      color = discord.Color.green(),
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_author(name = "Success")
    return embed