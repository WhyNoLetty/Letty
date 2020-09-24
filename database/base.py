from motor import motor_asyncio
from .model import Guild
import os

class Database:
    def __init__(self, *, letty):
        self.letty = letty
        self.connection = motor_asyncio.AsyncIOMotorClient(os.environ['DB_URL'])
        self.db = db = self.connection[os.environ['DB_NAME']]
        self.guild = db.guilds

    async def get_guild(self, guild_id):
        data = await self.guild.find_one({"_id": guild_id})
        if data != None:
           return Guild(data, self.guild)
        else:
          return await self.register_guild(guild_id)

    async def register_guild(self, guild_id):
        data = {
                "_id": guild_id,
                "config":{"prefix":"lt.","language":"pt_BR"},
                "disable":{"command":[],"channel":[],"role":[],"member":[]}
                }
        await self.guild.insert_one(data)
        return Guild(data, self.guild)  