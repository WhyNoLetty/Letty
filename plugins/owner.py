#Import's necessários (List import).
import discord, json
from discord.ext import commands
from config import get

#Classe do plugin 'Onwer'
class Onwer(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, kinash):
        self.kinash = kinash

    @commands.command(name='make_emoji')
    @commands.is_owner()
    async def _make_emoji(self, ctx):
       try:
           emojis = {}
           for guild in self.kinash.env.bot.emoji:          
             for emoji in self.kinash.get_guild(guild).emojiss:
                 emojis[emoji.name] = str(emoji)
           with open('./json/emoji.json', 'w+') as jsonf:
                json.dump(emojis, jsonf, indent=4, sort_keys=True)
            
           self.kinash.emoji = get("./json/emoji.json")
           await ctx.send(ctx.lang('cmd.make_emoji.create', {"self":self.kinash, "emojis":len(emojis), "ctx":ctx}))
       except Exception as e:
           await ctx.send(ctx.lang('err.make_emoji.create', {"self":self.kinash, "e":e, "ctx":ctx}))


#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Onwer(kinash))        