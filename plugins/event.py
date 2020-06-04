#Import's necessários (List import).
import discord
from discord.ext import commands
from discord.ext.commands.errors import *


#Classe do plugin 'Event'
class Event(commands.Cog):
    def __init__(self, kinash):
        """
         - Funções:
          self.kinash : Puxar as informações do bot pela classe Kinash.
        """
        self.kinash = kinash

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
    #        await ctx.send(ctx.lang('err.error.input', {"ctx":ctx,"self":self.kinash, "usage": usage}))

#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Event(kinash))        