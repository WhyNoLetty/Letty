#Import's necessários (List import).
from discord.ext.commands import when_mentioned_or


async def prefix(harumi, message):
    guild_id = message.guild.id

