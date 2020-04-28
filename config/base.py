#Import's necessários (List import).
from discord.ext.commands import AutoShardedBot
from database import on_connect_db

#Classe da Nixest (Autoshared class).
class Nixest(AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
         - Funções:
          self.load : Evitar de recarregar os modulos caso haja alguma queda.
          self.env : Obter informações 'dict' da classe da parte 'env'como token, links, etc.
          self.db : Fornecer os dados para a conexão da database do bot como url, name, a variável do bot.
        """
        self.loaded = True
        self.env = kwargs['env']
        self.db = on_connect_db(name=self.env.database.name, uri=self.env.database.url, bot=self)

    #Evento do Nixest referente ao 'start'.
    async def on_ready(self):
       print(f"[Session] : O bot {self.user.name} está online.")

    #Evento do Nixest referente a bloqueios de usuários, canais, checks entre outros.
    async def on_message(self, message):
       print(f'{message.guild.name} {message.author.name} {message.content}')
       #Checar se a mensagem não originou de um 'dm' ou se o modulo estar carregado.
       if not self.loaded or message.guild is None:return   
       #Checar se a mensagem não se originou de um bot ou checar se o Nixest pode enviar comandos no canal.
       if message.author.bot or not message.channel.permissions_for(message.guild.me).send_messages:return
       #Puxar as informações da mensagem como comandos, valores, canais, servidor etc.
       ctx = await self.get_context(message)
       #Checar se o comando é valído, se o comando não estar em uma classe proibida, se o author é um admin.
       if not ctx.valid or ctx.command.cog_name in [] and not ctx.author.id in self.env.bot.admin:return
       ctx.gdb = await self.db.get_guild(ctx.guild.id)

       try:
          #Invocar comandos pelo contexto e poder manipular alguns eventos.
          await self.invoke(ctx)
       except Exception as e:
            #Invocar o evento command_error caso ouver algum erro na execução do comando.
            self.dispatch('command_error', ctx, e)