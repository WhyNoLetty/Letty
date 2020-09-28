from discord.ext.commands import when_mentioned_or

async def prefix(letty, message):
    guild_id = message.guild.id
    try:
        prefix = letty.cache.prefix[guild_id]
    except KeyError:
        guild = await letty.db.get_guild(guild_id)
        letty.cache.prefix[guild_id] = prefix = guild.data['config']['prefix']
    result = letty.data.config.prefix if prefix is None else prefix
    return when_mentioned_or(result)(letty, message)       