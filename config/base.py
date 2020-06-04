#Import's necessários (List import).
from discord.ext.commands import AutoShardedBot
from discord.ext.translation import files
from discord.ext.mylistanime import client
from database import on_connect_db
import os, discord


#Classe da bot (Autoshared class).
class Shiro(AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
         - Funções:
          self.load : Evitar de recarregar os modulos caso haja alguma queda.
          self.env : Obter informações 'dict' da classe da parte 'env' como token, links, etc.
          self.emoji : Obter os emojis do bot.
          self.db : Fornecer os dados para a conexão da database do bot como url, name, a variável do bot.
          self.lang : Puxar as tradução do bot como primária sendo português a primeira tradução
          self.mal : Puxar a classe da api do myanimelist, e puxar as informações do anime.
          self.color : Definir a cor dos embed.
        """
        self.loaded = False
        self.env = kwargs['env']
        self.emoji = kwargs['emoji']
        self.db = on_connect_db(name=self.env.database.name, uri=self.env.database.url, bot=self)
        self.lang = files(source='pt_BR')
        self.mal = client()
        self.color = [discord.Colour.from_rgb(*self.env.bot.color[0]), self.env.bot.color[1]]

    #Evento para carregar o(s) plugin(s).
    async def on_start(self):
        #Puxar todo os plugins de um directorio.
        plugins = [p[:-3] for p in os.listdir("plugins") if p.endswith(".py")]
        #Contar quantos plugins existem.
        total_plugins = len(plugins)
        #Enumerar todo os plugins e passar eles por um 'for', e após passar usar o 'try' para executar uma leitura do mesmo.
        for i, plugin in enumerate(plugins, 1):
          try:
             #Carregar o plugin.
             self.load_extension(f"plugins.{plugin}")
          except Exception as e:
              #Caso houver um erro ao carregar o plugin.
              print(f"[Plugin] : Erro ao carregar o plugin {plugin}.\n{e.__class__.__name__}: {e}")
          else:
            #Quando o plugin carrega com sucesso.
            print(f"[Plugin] : O plugin {plugin} carregado com sucesso. ({i}/{total_plugins})")
        #Após carregar o(s) plugin(s) deixar a condição do loaded 'true'.
        self.loaded = True
    
    #Evento referente ao 'start'.
    async def on_ready(self):
       #Executar o evento on_start caso loaded esteja 'false'.
       if not self.loaded:
          #carregar todo os modulos/plugins.
          await self.on_start()
          #carregar toda os json com as linguagem do bot no local './json/lang/'
          self.lang.load_languages()
          print(f'[Language] : {len(self.lang.strings)} linguagem(s) carregada(s).')
          print(f"[Session] : O bot {self.user.name} está online.")    
    
    #Evento referente a bloqueios de usuários, canais, checks entre outros.
    async def on_message(self, message):
       #Checar se a mensagem não originou de um 'dm' ou se o modulo estar carregado.
       if not self.loaded or message.guild is None:return   
       #Checar se a mensagem não se originou de um bot ou checar se pode enviar comandos no canal.
       if message.author.bot or not message.channel.permissions_for(message.guild.me).send_messages:return
       #Puxar as informações da mensagem como comandos, valores, canais, servidor etc.
       ctx = await self.get_context(message)
       #Checar se o comando é valído, se o comando não estar em uma classe proibida, se o author é um admin.
       if not ctx.valid or ctx.command.cog_name in [] and not ctx.author.id in self.env.bot.admin:return
       #Importar as informações do database pro context.
       ctx.db = await self.db.get_guild(ctx.guild.id)
       ctx.lang = self.lang.get(ctx.db.data['config']['language'])
       try:
          #Invocar comandos pelo contexto e poder manipular alguns eventos.
          await self.invoke(ctx)
       except Exception as e:
            #Invocar o evento command_error caso ouver algum erro na execução do comando.
            self.dispatch('command_error', ctx, e)
