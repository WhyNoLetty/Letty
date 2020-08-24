#Import's necessários (List import).
import discord, traceback
from discord.ext import commands
from discord.ext.commands.errors import *

#Classe do plugin 'Event'
class Event(commands.Cog):
    def __init__(self, harumi):
        """
        Id : Funções:
          self.harumi : Puxar as informações do bot pela classe harumi.
        """
        self.harumi = harumi
        self.harumi.loop.create_task(self._fetch_logs_channels())
    
    async def _fetch_logs_channels(self):
        self.error_logs = await self.harumi.fetch_channel(747289985421541467)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, e):
        original = e.__cause__
        if isinstance(original, (discord.NotFound, discord.Forbidden)):
            pass
        else:
          traceback_ = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
          em = discord.Embed(colour=self.harumi.color[0], timestamp=ctx.message.created_at, description=f'```py\n{traceback_[:2038]}```')
          em.set_image(url=ctx.guild.icon_url)
          for x in ['server', 'user', 'channel', 'message']:
              em.add_field(name=ctx.lang(f'error.on_command.{x}.name'), value=f"``{ctx.lang(f'error.on_command.{x}.string', {'ctx':ctx})}``", inline=True)
          await self.error_logs.send(embed=em)

#Adicionar o plugin na lista.
def setup(harumi):
    harumi.add_cog(Event(harumi))        
