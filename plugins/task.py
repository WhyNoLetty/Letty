#Import's necessários (List import).
import discord, random, datetime
from discord.ext import commands, tasks

#Classe do plugin 'Task'
class Task(commands.Cog):
    def __init__(self, kinash):
        """
         - Funções:
          self.kinash : Puxar as informações do bot pela classe Kinash.
          self.bot : Obter informações 'dict' da classe da parte 'env' com informações do bot
          self.message : Obter informações 'dict' da classe da parte 'env' com informações da presence do bot e converter-las em uma 'dict'
          self.presence : Colocar toda as atividades (jogando, ouvindo, etc) de presence do bot em uma dict.
          self.status : Colocar todo os status (online, afk, não pertube) da presence do bot em uma dict.
          self.presence : Colocar toda as tasks (funções automatizas) em uma dict.
        """
        self.kinash = kinash
        self.bot = self.kinash.env.bot           
        self.message = {'listening':self.kinash.env.bot.presence.listening,'watching':self.kinash.env.bot.presence.watching,'streaming':self.kinash.env.bot.presence.streaming,'playing':self.kinash.env.bot.presence.playing}
        self.presence = [discord.ActivityType.listening,discord.ActivityType.watching,discord.ActivityType.streaming,discord.ActivityType.playing]
        self.status = [discord.Status.online,discord.Status.dnd,discord.Status.idle]
        #self.tasks = [('change_presence', self.change_presence.start()),('change_avatar', self.change_avatar.start()),]
    
    #Task para trocar o avatar e as cores do embed.
    @tasks.loop(minutes=10)
    async def change_avatar(self):
    	try: 
           avatar = open(f"./image/avatar/{random.randint(1, 2)}.png", 'rb').read()
           #Trocar o avatar do bot.
           await self.kinash.user.edit(avatar=avatar)
    	except Exception as e:
        #Caso ouver algum erro na execução da task.
    		print(e)
    
    #Task para trocar a presence do bot e a mensagem.
    @tasks.loop(minutes=10)
    async def change_presence(self):
      try:
        #Passar todos os shard do bot no 'for', e após passar usar o 'try' para executar a mudança do presence.
        for shard in self.kinash.shards:
            #Puxar uma atividade aleatoria da presence (jogando, ouvindo etc)
            activity = random.choice(self.presence)
            #Puxar uma messagem aleátoria  da presence.
            message = random.choice(self.message[activity.name]).format(website=self.bot.link.website, prefix=self.bot.prefix[0])
            #Definir o presence.
            await self.kinash.change_presence(activity=discord.Activity(type=activity, name=message + f' [{shard}]',url=self.bot.link.twitch), shard_id=shard, status=random.choice(self.status))
      except Exception as e:
        #Caso ouver algum erro na execução da task.
        print(e)


#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Task(kinash))        