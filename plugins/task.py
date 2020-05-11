#Import's necessários (List import).
import discord, random
from discord.ext import commands, tasks

#Classe do plugin 'Utilidade'
class Task(commands.Cog):
    def __init__(self, kinash):
        self.kinash = kinash
        self.bot = self.kinash.env.bot           
        self.message = {
                        'listening':self.kinash.env.bot.presence.listening,
                        'watching':self.kinash.env.bot.presence.watching,
                        'streaming':self.kinash.env.bot.presence.streaming,
                        'playing':self.kinash.env.bot.presence.playing
                       }
        self.presence = [ 
                           discord.ActivityType.listening,
                           discord.ActivityType.watching,
                           discord.ActivityType.streaming,
                           discord.ActivityType.playing
                          ]
        
        self.status = [
                       discord.Status.online,
                       discord.Status.dnd,
                       discord.Status.idle
                      ]
    

        self._tasks = [
                       ('change_presence', self.change_presence.start()),
                       ('change_avatar', self.change_avatar.start()),
                      ]
    
    @tasks.loop(minutes=10)
    async def change_avatar(self):
    	try:
           info = random.choice(self.kinash.env.bot.image)
           avatar = open(info.path, 'rb').read()
           rgb = info.rgb
           self.kinash.color = [discord.Colour.from_rgb(*rgb[0]), discord.Colour.from_rgb(*rgb[1])]
    	except Exception as e:
    		print(e)

    @tasks.loop(minutes=10)
    async def change_presence(self):
      try:
        for shard in self.kinash.shards:
            activity = random.choice(self.presence)
            message = random.choice(self.message[activity.name]).format(website=self.bot.link.website, prefix=self.bot.prefix[0])
            await self.kinash.change_presence(activity=discord.Activity(type=activity, name=message + f' [{shard}]',url=self.bot.link.twitch), shard_id=shard, status=random.choice(self.status))
      except Exception as e:
        print(e)

#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Task(kinash))        