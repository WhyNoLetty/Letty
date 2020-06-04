#Import's necessários (List import).
import discord
from discord.ext import commands
from discord.ext.commands.errors import *


#Classe do plugin 'Event'
class Event(commands.Cog):
    def __init__(self, shiro):
        """
         - Funções:
          self.shiro : Puxar as informações do bot pela classe shiro.
        """
        self.shiro = shiro

#    @commands.Cog.listener()
 #   async def on_command_error(self, ctx, e):
  #      original = e.__cause__
   #     
    #    if isinstance(original, (discord.NotFound, discord.Forbidden)):
     #       pass
#
 #       if isinstance(e, (UserInputError)):
  #          usage = (ctx.lang(f'cmd.{".".join(ctx.command.qualified_name.split())}.meta') or {}).get('usage')
   #         usage = ctx.prefix + (ctx.command.parent.name + ' ' if ctx.command.parent else '') + ctx.invoked_with + (' ' + usage if usage else '')
    #        await ctx.send(ctx.lang('err.error.input', {"ctx":ctx,"self":self.shiro, "usage": usage}))

#Adicionar o plugin na lista.
def setup(shiro):
    shiro.add_cog(Event(shiro))        