#Import's necessários (List import).
import discord, json, traceback, sys
from config import get
from discord.ext import commands

#Classe do plugin 'Owner'
class Owner(commands.Cog):
    def __init__(self, harumi):
        """
         - Funções:
          self.harumi : Puxar as informações do bot pela classe harumi.
        """
        self.harumi = harumi
        self.module = {"-r":"reload", "-u":"unload", "-l":"load"}
    
    # - Executar funções no bot.
    @commands.command(name='make')
    @commands.is_owner()
    async def _make(self, ctx, event):
       if event == 'emoji':
        # - Array para armazenar os emojis temporariamente.
        array = {}
        # - Puxar todos os 'ids' das guilds.
        for guild in self.harumi.data.config.id.guild.emoji:
          # - Puxar  todos os emojis da guild.
          for emoji in self.harumi.get_guild(guilds).emojis:
            # - Adicionar o nome do emoji mais o emoji no Array.
            array[emoji.name] = str(emoji)
        # - Abrir o arquivo emoji.json e ler-lo.
        with open('./json/config/emoji.json', 'w+') as jsonf:
            # - Inserir os emojis do Array no json e salva-lo.
            json.dump(array, jsonf)
        # - Atualizar os emojis da Harumi na class Kwarg.
        self.harumi.data.emoji = get("./json/config/emoji.json", type='obj')
        # - Enviar a mensagem no canal caso a evento tenha exito.
        await ctx.send(ctx.lang('command.make.emoji.success', {"ctx":ctx, "emoji":len(array)}))

    # - Executar funções no bot.
    @commands.command(name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, code):
       #Tentar executar a função.
       try:
           # - Executar uma função async.
           if code.startswith('await '):
              aa = await eval(code[6:])
           else:
             # - Executar uma função não async.
             aa = eval(code)
           # - Enviar a mensagem no canal caso a função tenha exito.
           return await ctx.send(ctx.lang('command.eval.success', {"ctx":ctx, "e":aa}))
       # - Caso ouver algum erro na execução do comando.
       except Exception as e:
          # - Enviar a mensagem no canal caso a função tenha não tenha exito.
          await ctx.send(ctx.lang('command.eval.error', {"ctx":ctx, "e":e}))

    @commands.command(name='module')
    @commands.is_owner()
    async def _module(self, ctx, event, *, module):
       try:
         # - Deixar o nome do evento em minusculo.
         event = event.lower()
         # - Checar se o evento é válido.
         if not event in ['-r', '-u', '-l']:
           # - Enviar a mensagem no canal se o evento foi inválido.
           return await ctx.send(ctx.lang('exception.module.valid', {"self":self.harumi, "ctx":ctx}))
         # - Recarregar o modulo.
         if event == '-r':
            self.harumi.reload_extension(f'plugins.{module}')
         # - Descarregar o modulo.
         elif event == '-u':
              self.harumi.unload_extension(f'plugins.{module}')
         # - Carregar o modulo.
         elif event == '-l':
              self.harumi.load_extension(f'plugins.{module}')
         # - Enviar a mensagem no canal se o evento foi executado com sucesso.
         await ctx.send(ctx.lang('command.module.executed', {"self":self.harumi, "module":module, "event":ctx.lang(f'convert.module.{self.module[event]}'), "ctx":ctx}))
       except Exception as e:
          # - Caso ouver algum erro na execução do comando.
          await ctx.send(ctx.lang('exception.module.error', {"self":self.harumi, "module":module, "event":ctx.lang(f'convert.module.{self.module[event]}ed'), "out":e, "ctx":ctx}))

#Adicionar o plugin na lista.
def setup(harumi):
    harumi.add_cog(Owner(harumi))        