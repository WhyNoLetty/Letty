#Import's necessários (List import).
import discord
from discord.ext import commands, tasks

from quart.serving import Server
from quart.logging import create_serving_logger
from cogs.api import app
from discord.ext import commands

#Classe do plugin 'Task'
class Task(commands.Cog):
    def __init__(self, shiro):
        """
         - Funções:
          self.shiro : Puxar as informações do bot pela classe shiro.
          self.bot : Obter informações 'dict' da classe da parte 'env' com informações do bot
          self.message : Obter informações 'dict' da classe da parte 'env' com informações da presence do bot e converter-las em uma 'dict'
          self.presence : Colocar toda as atividades (jogando, ouvindo, etc) de presence do bot em uma dict.
          self.status : Colocar todo os status (online, afk, não pertube) da presence do bot em uma dict.
          self.presence : Colocar toda as tasks (funções automatizas) em uma dict.
        """
        self.shiro = shiro

#Adicionar o plugin na lista.
def setup(shiro):
    shiro.add_cog(Task(shiro))        