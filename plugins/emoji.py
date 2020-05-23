#Import's necessários (List import).
import discord, json
from discord.ext import commands
from config import get_aio, get
from io import BytesIO
import asyncio

#Classe do plugin 'Onwer' e deixa-la escondida através do hidden.
class Onwer(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, kinash):
        """
         - Funções:
          self.kinash : Puxar as informações do bot pela classe Kinash.
          self.module: Converter a função em uma palavra para puxar do sistema de lang pro comando.
        """
        self.kinash = kinash
        self.module = {'-r':"reload", "-u":"unload", "-l":"load"}

    async def icon_data(self, data, color):
      data = await get_aio(f"https://img.icons8.com/{data['type']}/{data['size']}/{color}/{data['real']}.png", res_method="read")
      return data
    
    async def event_coro(self, coro):
       try:
           coro = await asyncio.wait_for(coro, timeout=10.0)
       except asyncio.TimeoutError:
           return None
       except (discord.NotFound, discord.HTTPException) as e:
           return False
       else:
         return coro    

    async def create_emoji(self, guild, name, bio):
       return await self.event_coro(guild.create_custom_emoji(name=name, image=bio, reason=None)) 

    #Criar emojis para o bot.
    @commands.command(name='icons')
    @commands.is_owner()
    async def _make_emojsi(self, ctx):
       try:
          lista = [702629146475364465]
          for guild in lista:
             guild = await self.kinash.fetch_guild(guild)
             for emoji in await guild.fetch_emojis():
                 emoji_status = await self.delete_emoji(ctx, emoji.id)
                 if emoji_status is True:
                    bio = await get_aio(f"https://img.icons8.com/metro/500/000000/add-link.png", res_method="read")
                    emoji_created = await self.create_emoji(ctx, emoji.name, bio)
                    await ctx.send(emoji_created)
                 else:
                   await ctx.send(emoji.name)


       except Exception as e:
           #Caso ouver algum erro na execução do comando.
           await ctx.send(ctx.lang('err.make_emoji.error', {"self":self.kinash, "e":e, "ctx":ctx}))

    #Criar emojis para o bot.
    @commands.command(name='gg')
    @commands.is_owner()
    async def gg(self, ctx, *, id=None):
       try:
           emoji_data = get("./json/down.json", simple=True)
           for guild in self.kinash.env.bot.emoji:    
              guild = await self.kinash.fetch_guild(guild) 
              for emoji in await guild.fetch_emojis():
                 await emoji.delete()
                 emoji = await self.create_emoji(guild, emoji.name,(await self.icon_data(emoji_data[emoji.name], 'FF00FF')))
                 emoji_data[emoji.name].update(code=f'{emoji}')
           
           with open('./json/down.json', 'w+') as jsonf:
                #Inserir todo os emojis no json e salvar-los e depos indenta-los.
                json.dump(emoji_data, jsonf, indent=4, sort_keys=True)
           
           await ctx.send('123')




       except Exception as e:
           #Caso ouver algum erro na execução do comando.
           await ctx.send(ctx.lang('err.make_emoji.error', {"self":self.kinash, "e":e, "ctx":ctx}))

#                  bio = f"https://img.icons8.com/{url['type']}/{emoji['size']}/000000/{emoji['real']}.png"



               #bio = await get_aio(f"https://img.icons8.com/{emoji.type}/{emoji.size}/{color}/{emoji.real}.png", res_method="read")

#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Onwer(kinash))        