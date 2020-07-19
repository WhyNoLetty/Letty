#Import's necessários (List import).
from discord.ext import commands
from database import Database

# - Class da harumi com seus eventos.
class Harumi(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
         - Funções:
          self.load : Evitar de recarregar os modulos caso haja alguma queda.
          self.env : Obter informações 'dict' da classe da parte 'env' como token, links, etc.
          self.db : Fornecer os dados para a conexão da database do bot como url, name, a variável do bot.
        """
        self.loaded = False
        self.env = kwargs['env']
        self.db = Database(url=self.env.config.database.url, name=self.env.config.database.name, harumi=self)

    # - Evento referente ao 'start'.
    async def on_ready(self):
       # - Executar o evento on_start caso loaded esteja 'false'.
       if not self.loaded:
          print(f"[Session] : O bot {self.user.name} está online.")  