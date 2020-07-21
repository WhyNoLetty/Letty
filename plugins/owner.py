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
        self.module = {"-r":"reload", "-u":"unload", "-l":"load"}
        
    # - Executar funções no bot.
    @commands.command(name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, code):
       #Tentar executar a função.
       try:
           # - Executar uma função async.
           if code.startswith('await '):
              result = await eval(code[6:])
           else:
             # - Executar uma função não async.
             result = eval(code)
           # - Enviar a mensagem no canal caso a função tenha exito.
           return await ctx.send(ctx.lang('cmd.eval.success', {"self":self.harumi, "out":result, "ctx":ctx}))
       # - Caso ouver algum erro na execução do comando.
       except Exception as e:
          # - Enviar a mensagem no canal caso a função tenha não tenha exito.
          await ctx.send(ctx.lang('cmd.eval.no_success', {"self":self.harumi, "out":e, "ctx":ctx}))

    @commands.command(name='module')
    @commands.is_owner()
    async def _module(self, ctx, event, *, module):
       try:
         # - Deixar o nome do evento em minusculo.
         event = event.lower()
         # - Checar se o evento é válido.
         if not event in ['-r', '-u', '-l']:
           # - Enviar a mensagem no canal se o evento foi inválido.
           return await ctx.send(ctx.lang('cmd.module.no_valid', {"self":self.harumi, "ctx":ctx}))
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
         await ctx.send(ctx.lang('cmd.module.success', {"self":self.harumi, "module":module, "event":ctx.lang(f'cmd.module.event.{self.module[event]}'), "ctx":ctx}))
       except Exception as e:
          # - Caso ouver algum erro na execução do comando.
          await ctx.send(ctx.lang('cmd.eval.no_success', {"self":self.harumi, "out":e, "ctx":ctx}))

#Adicionar o plugin na lista.
def setup(harumi):
    harumi.add_cog(Base(harumi))        