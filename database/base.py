#Import's necessários (List import).
from motor import motor_asyncio
from .model import Guild

# - Classe principal da Database.
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
        self.guild = db.guilds


    # - Puxar as informações de um servidor e passar as informações pela classe Guild
    async def get_guild(self, guild_id):
    	# - Verificar se o servidor estar registrado no database.
        data = await self.guild.find_one({"_id": guild_id})
        # - Se o servidor estar registrado retornar os dados do mesmo.
        if data != None:
           # - Retornar os dados do servidor como objeto.
           return Guild(data, self.guild)
        else:
          # - Executar a função register_guild
          return await self.register_guild(guild_id)

    # - Registrar um servidor caso o mesmo não esteja registrado no banco de dados MongoDB
    async def register_guild(self, guild_id):
        data = {
                "_id": guild_id,
                "config":{"prefix":"h.","language":"pt_BR"},
                "disable":{"command":[],"channel":[],"role":[],"member":[]}
                }
        # - Registrar o servidor no bando de dados.
        await self.guild.insert_one(data)
        # - Retornar os dados do servidor como objeto.
        return Guild(data, self.guild)  