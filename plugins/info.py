from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, letty):
        self.letty = letty



def setup(letty):
    letty.add_cog(Info(letty))        