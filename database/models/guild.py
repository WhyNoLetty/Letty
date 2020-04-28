#import's necessários
from motor.core import Collection

#Classe principal responsavél por converter os dados em um objeto.
class Guild:
    def __init__(self, data, collection: Collection):
        """
         - Funções:
          self.db : Puxa informações da 'collection'.
          self.data : São os dados do servidor a ser manipulado.
          self.id : é o ID do servidor em questão a ser manipulado.

        """
        self.db = collection
        self.data = data
        self.id = data['_id']
    
    #Função $set : substitui o valor x pelo valor y.
    async def set(self, data):
        await self.db.update_one({"_id": self.id}, {"$set": data})
    
    #Função $inc : editar um valor x somando/subtraindo/etc com o valor y.
    async def inc(self, data):
        await self.db.update_one({"_id": self.id}, {"$inc": data})
    
    #Função $push : adicionar um valor x em um array.
    async def push(self, data):
        await self.db.update_one({"_id": self.id}, {"$push": data})
    
    #Função $pull : remover um valor x em um array.
    async def pull(self, data):
        await self.db.update_one({"_id": self.id}, {"$pull": data})
    
    #Função delete : deletar o servidor do banco de dados.
    async def delete(self):
        await self.db.delete_one({"_id": self.id})