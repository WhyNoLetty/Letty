#Import's necessários (List import).
from discord.ext.commands import when_mentioned_or
import os

# -  Obter o prefix da Harumi
async def prefix(harumi, message):
	# - Id da guild
    guild_id = message.guild.id
    try:
        prefix = harumi.cache.prefix[guild_id]
    except KeyError:
        guild = await harumi.db.get_guild(guild_id)
        harumi.cache.prefix[guild_id] = prefix = guild.data['config']['prefix']
    
    result = os.environ['BOT_PREFIX'] if prefix is None else prefix
    return when_mentioned_or(result)(harumi, message)       