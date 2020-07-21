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
        
    #Comando de ajuda para o usuário.
    @commands.command(name='help')
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def _help(self, ctx, *, args=None):
       # - Checar se a pessoa executou o comando e o dono.
       owner = await ctx.bot.is_owner(ctx.author)
       # - Caso não houver argumentos irá mostrar todos os comandos.
       if args:
          # - Puxar as informação do comando caso o mesmo existir.
          command = self.harumi.get_command(args)
          # - Checar se o comando existe, e caso existir verificar se ele não estar "escondido" se caso estiver verificar se o author e o dono para mostra-lo.
          if not command or command.hidden and owner is False:
             return await ctx.send(ctx.lang('cmd.help.none', {"self":self.harumi, "ctx": ctx, "args":args}))







#Adicionar o plugin na lista.
def setup(harumi):
    harumi.add_cog(Base(harumi))        