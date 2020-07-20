#Import's necessários (List import).
import discord
from discord.ext import commands

#Classe do plugin 'Base'
class Base(commands.Cog):
    def __init__(self, harumi):
        """
         - Funções:
          self.harumi : Puxar as informações do bot pela classe harumi.
        """
        self.harumi = harumi
        
    @commands.command(name='say')
    #@commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def _say(self, ctx):
        
        await ctx.send('Olá')

               
#Adicionar o plugin na lista.
def setup(harumi):
    harumi.add_cog(Base(harumi))        