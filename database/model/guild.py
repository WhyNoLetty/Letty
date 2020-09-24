from motor.core import Collection

class Guild:
    def __init__(self, data, collection: Collection):
        self.db = collection
        self.data = data
        self.id = data['_id']

    async def set(self, data):
        await self.db.update_one({"_id": self.id}, {"$set": data})

    async def inc(self, data):
        await self.db.update_one({"_id": self.id}, {"$inc": data})

    async def push(self, data):
        await self.db.update_one({"_id": self.id}, {"$push": data})

    async def pull(self, data):
        await self.db.update_one({"_id": self.id}, {"$pull": data})

    async def delete(self):
        await self.db.delete_one({"_id": self.id}) 