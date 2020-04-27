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
        self.load = False
        self.env = kwargs['env']
        self.db = on_connect_db(name=self.env.database.name, uri=self.env.database.url, bot=self)

    #Evento do Nixest referente ao 'start'.
    async def on_ready(self):
       print(f"[Session] : O bot {self.user.name} está online.")