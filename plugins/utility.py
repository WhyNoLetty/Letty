#Import's necessários (List import).
import discord
from discord.ext import commands

#Classe do plugin 'Utilidade'
class Utility(commands.Cog):
    def __init__(self, nixest):
        self.nixest = nixest

    #O primeiro comando 'say'
    @commands.command(aliases=['dizer'])
    async def say(self, ctx, *, word=None):
        if word is None:
           return await ctx.send(f'{ctx.prefix}{ctx.command} + algo')

        await ctx.send(word)


#Adicionar o plugin na lista.
def setup(nixest):
    nixest.add_cog(Utility(nixest))        