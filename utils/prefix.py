#Import's necessários (List import).
from discord.ext.commands import when_mentioned_or

# -  Obter o prefixo da letty
async def prefix(letty, message):
    # - Id da guild
    guild_id = message.guild.id
    # - Tentar executar a função.
    try:
    	# - Tentar obter o prefixo no cache.
        prefix = letty.cache.prefix[guild_id]
    except KeyError:
    	# - Caso houver erro referente ao 'KeyError', puxar do database o prefixo
        guild = await letty.db.get_guild(guild_id)
        # - Adicionar o prefixo no cache.
        letty.cache.prefix[guild_id] = prefix = guild.data['config']['prefix']
    # - Checar se o prefixo é valído caso o mesmo não for, o prefixo será o prefixo padrão.
    result = letty.data.config.prefix if prefix is None else prefix
    # - Usar o prefixo do cache ou a menção.
    return when_mentioned_or(result)(letty, message)       