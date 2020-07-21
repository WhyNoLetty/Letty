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
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def _say(self, ctx, *, args=None):
        if args is None:
          return await ctx.send(ctx.lang("cmd.say.none", {"emoji":"❔", "ctx":ctx}))
        await ctx.send(args)
               
#Adicionar o plugin na lista.
def setup(harumi):
    harumi.add_cog(Base(harumi))        