from discord import Colour
from discord.ext import commands
from .data import Config, Cache
from discord.ext.translation import Files
from database import Database
from os import listdir

class Letty(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loaded = False
        self.data = Config()
        self.cache = Cache()
        self.db = Database(letty=self)
        self.lang = Files(source='pt_BR')
        self.color = [Colour.from_rgb(*self.data.config.color.embed.normal), Colour.from_rgb(*self.data.config.color.embed.error)]

    async def on_start(self):
        plugins = [p[:-3] for p in listdir("plugins") if p.endswith(".py")]
        total_plugins = len(plugins)
        for i, plugin in enumerate(plugins, 1):
          try:
             self.load_extension(f"plugins.{plugin}")
          except Exception as e:
              print(f"[Plugin] : Erro ao carregar o plugin {plugin}.\n{e.__class__.__name__}: {e}")
          else:
            print(f"[Plugin] : O plugin {plugin} carregado com sucesso. ({i}/{total_plugins})")
        self.loaded = True

    async def on_ready(self):
       if not self.loaded:
          await self.on_start()
          await self.lang.load_languages()
          print(f'[Language] : {len(self.lang.strings)} linguagem(s) carregada(s).')
          print(f"[Session] : O bot {self.user.name} está online.")  

    async def on_message(self, message):
       if not self.loaded or message.guild is None:return   
       if message.author.bot or not message.channel.permissions_for(message.guild.me).send_messages:return
       ctx = await self.get_context(message)
       if not ctx.valid or ctx.command.cog_name in self.data.config.ignore.module and not ctx.author.id in self.data.staff:return
       ctx.db = await self.db.get_guild(ctx.guild.id)
       ctx.lang = await self.lang.get(ctx.db.data['config']['language'])
       try:
          await self.invoke(ctx)
       except Exception as e:
            self.dispatch('command_error', ctx, e)         