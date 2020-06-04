#Import's necessários (List import).
import discord, json
from discord.ext import commands
from config import get
import asyncio

#Classe do plugin 'Onwer' e deixa-la escondida através do hidden.
class Onwer(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, shiro):
        """
         - Funções:
          self.shiro : Puxar as informações do bot pela classe shiro.
          self.module: Converter a função em uma palavra para puxar do sistema de lang pro comando.
        """
        self.shiro = shiro
        self.module = {'-r':"reload", "-u":"unload", "-l":"load"}

    #Executar funções no bot.
    @commands.command(name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, code=None):
       try:
           #Executar asyncronizado quando começar com await
           if code.startswith('await '):
              result = await eval(code[6:])
           else:
             #Executar a função não asyncronizado.
             result = eval(code)
           await ctx.send(ctx.lang('command.eval.success', {"self":self.shiro, "out":result, "ctx":ctx}))
       except Exception as e:
          #Caso ouver algum erro na execução do comando.
          await ctx.send(ctx.lang('error.eval.error', {"self":self.shiro, "out":e, "ctx":ctx}))

    #Recarregar, descarregar, carregar modulos do bot.
    @commands.command(name='module', aliases=['oi', 'test', 'gg'])
    @commands.is_owner()
    async def _module(self, ctx, type, *, module):
       try:
           #Verificar se a função para executar no modulo é valída.
           if not type.lower() in ['-r', '-u', '-l']:
              return await ctx.send(ctx.lang('error.module.no_valid', {"self":self.shiro, "ctx":ctx}))
           if type.lower() == '-r':
              #Recarregar o modulo.
              self.shiro.reload_extension(f'plugins.{".".join(module)}')
           elif type.lower() == '-u':
                #Descarregar o modulo.
                self.shiro.unload_extension(f'plugins.{".".join(module)}')
           else:
             #Caregar o modulo.
             self.shiro.load_extension(f'plugins.{".".join(module)}')
           await ctx.send(ctx.lang('command.module.success', {"self":self.shiro, "module":module, "type":ctx.lang(f'common.module.{self.module[type]}'), "ctx":ctx}))
       except Exception as e:
           #Caso ouver algum erro na execução do comando.
           await ctx.send(ctx.lang('error.module.error', {"self":self.shiro, "e":e, "module":module, "type":ctx.lang(f'common.module.{self.module[type]}'), "ctx":ctx}))

#Adicionar o plugin na lista.
def setup(shiro):
    shiro.add_cog(Onwer(shiro))        