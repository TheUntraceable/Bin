import discord
import datetime

class ErrorEmbed:
  def error(title, reason):
    embed = discord.Embed(
      title = title,
      description = reason,
      color = discord.Color.red(),
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_author(name = "Error")
    return embed