#Import's necessários (List import).
from discord.ext.commands import AutoShardedBot

#Classe da Nixest (Autoshared class).
class Nixest(AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
         - Funções:
          self.load : Evitar de recarregar os modulos caso haja alguma queda.
          self.config : Obter informações 'dict' da classe da parte 'config'.
        """
        self.load = False
        self.confg = kwargs['config']
    
    #Evento do Nixest referente ao 'start'.
    async def on_ready(self):
       print(f"[Session] : O bot {self.user.name} está online.")