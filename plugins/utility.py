#Import's necessários (List import).
import discord
from discord.ext import commands

#Classe do plugin 'Utilidade'
class Utility(commands.Cog):
    def __init__(self, kinash):
        self.kinash = kinash

    #O primeiro comando 'say'
    @commands.command(aliases=['dizer'])
    async def say(self, ctx, *, word=None):
        if word is None:
           return await ctx.send(ctx.lang("cmd.say.none",{'ctx':ctx, 'emoji':'⁉️'}))

        await ctx.send(word)

               
#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Utility(kinash))        