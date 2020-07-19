#Import's necessários (List import).
from motor import motor_asyncio

#Classe principal da Database.
class Database():
    def __init__(self, *, name, url, harumi):
        """
         - Funções:
          self.connection : Fazer a conexão com o banco de dados mongoDB através do Motor asyncio.
          self.db : Puxa informações da 'collection'.
        """
        self.harumi = harumi
        self.connection = motor_asyncio.AsyncIOMotorClient(url)
        self.db = db = self.connection[name]
