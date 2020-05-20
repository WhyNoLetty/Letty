#Import's necessários (List import).
import discord, json
from discord.ext import commands
from config import get
#Classe do plugin 'Onwer'
class Onwer(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, kinash):
        self.kinash = kinash

    @commands.command(name='gg')
    @commands.is_owner()
    async def make_emoji(self, ctx):
        emojis = {}
        for guild in self.kinash.env.bot.emoji:          
            for emoji in self.kinash.get_guild(guild).emojis:
                emojis[emoji.name] = str(emoji)
        with open('./json/emoji.json', 'w+') as jsonf:
            json.dump(emojis, jsonf, indent=4, sort_keys=True)
        
        self.kinash.color = get("./json/emoji.json")
        await ctx.send('Done!')


#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Onwer(kinash))        