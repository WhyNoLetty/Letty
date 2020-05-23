#Import's necessários (List import).
import discord, json
from discord.ext import commands
from config import get
import asyncio

#Classe do plugin 'Onwer' e deixa-la escondida através do hidden.
class Onwer(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, kinash):
        """
         - Funções:
          self.kinash : Puxar as informações do bot pela classe Kinash.
          self.module: Converter a função em uma palavra para puxar do sistema de lang pro comando.
        """
        self.kinash = kinash
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
           await ctx.send(ctx.lang('cmd.eval.success', {"self":self.kinash, "in":code, "out":result, "ctx":ctx}))
       except Exception as e:
          #Caso ouver algum erro na execução do comando.
          await ctx.send(ctx.lang('err.eval.error', {"self":self.kinash, "in":code, "out":e, "ctx":ctx}))

    #Recarregar, descarregar, carregar modulos do bot.
    @commands.command(name='module')
    @commands.is_owner()
    async def _module(self, ctx, type=None, *, module=None):
       try:
           #Verificar se a função para executar no modulo é valída.
           if not type.lower() in ['-r', '-u', '-l']:
              return await ctx.send(ctx.lang('err.module.type_no_valid', {"self":self.kinash, "ctx":ctx}))
           #Verificar se o modulo é valido.
           if module is None:
              return await ctx.send(ctx.lang('err.module.module_none', {"self":self.kinash, "type":ctx.lang(f'cms.{self.module[type]}'), "ctx":ctx}))
           if type.lower() == '-r':
              #Recarregar o modulo.
              self.kinash.reload_extension(f'plugins.{module}')
           elif type.lower() == '-u':
                #Descarregar o modulo.
                self.kinash.unload_extension(f'plugins.{module}')
           else:
             #Caregar o modulo.
             self.kinash.load_extension(f'plugins.{module}')
           await ctx.send(ctx.lang('cmd.module.success', {"self":self.kinash, "module":module, "type":ctx.lang(f'cms.{self.module[type]}ed'), "ctx":ctx}))
       except Exception as e:
           #Caso ouver algum erro na execução do comando.
           await ctx.send(ctx.lang('err.module.error', {"self":self.kinash, "e":e, "module":module, "type":ctx.lang(f'cms.{self.module[type]}'), "ctx":ctx}))

    #Criar emojis para o bot.
    #@commands.command(name='make_emoji')
    #@commands.is_owner()
    #async def _make_emoji(self, ctx):
    #   try:
    #       #Dict dos emojis
    #       emojis = {}
    #       #puxar os ids da guilds da env é fazer um for com elas.
    #       for guild in self.kinash.env.bot.emoji:          
    #         #Pegar o id do servidor é puxar todos os emojis do servidor.
    #         for emoji in self.kinash.get_guild(guild).emojis:
    #             #adiciona-los em uma lista
    #             emojis[emoji.name] = str(emoji)
    #       #Abrir/Criar um arquivo json.
    #       with open('./json/emoji.json', 'w+') as jsonf:
    #            #Inserir todo os emojis no json e salvar-los e depos indenta-los.
    #            json.dump(emojis, jsonf, indent=4, sort_keys=True)
    #       #Definir os novos emojis na classe na fct emoji.
    #       self.kinash.emoji = get("./json/emoji.json")
    #       await ctx.send(ctx.lang('cmd.make_emoji.create', {"self":self.kinash, "emojis":len(emojis), "ctx":ctx}))
    #   except Exception as e:
    #       #Caso ouver algum erro na execução do comando.
    #       await ctx.send(ctx.lang('err.make_emoji.error', {"self":self.kinash, "e":e, "ctx":ctx}))
    

#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Onwer(kinash))        