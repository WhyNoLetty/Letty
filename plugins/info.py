#Import's necessários (List import).
import discord
from discord.ext import commands

#Classe do plugin 'Utilidade'
class Utility(commands.Cog):
    def __init__(self, kinash):
        self.kinash = kinash
        self.link = self.kinash.env.bot.link           


    async def show_cmd(self, ctx, command):
       #Nome do evento.
       name = command.qualified_name
       #As alternativa do evento.
       aliase = command.aliases
       #Puxar o prefixo mais o nome do evento.
       invocation = f'{ctx.prefix}{name}'
       #Puxar o meta com as traduções do evento.
       meta = ctx.lang(f'cmd.{name}.meta') or {}
       #descrição do evento.
       description = meta.get('description', ctx.lang('cms.no_defined'))
       #Como usar o evento.
       usage = meta.get('usage')
       #Exemplos de como usar o evento.

      
       em = discord.Embed(color=self.kinash.color[0], title=ctx.lang('cmd.help.name', {"cmd": command.name.title()}))
       em.set_thumbnail(url=self.kinash.user.avatar_url)
       em.set_author(name=ctx.lang('cmd.help.helper'), icon_url=ctx.author.avatar_url)
       em.add_field(name=ctx.lang('cmd.help.aliase', {"emoji":"🎨", "total":len(aliase)}), value=' | '.join([f'`{a}`' for a in aliase]) or f"``{ctx.lang('cms.no_defined')}``")
       em.add_field(name=ctx.lang('cmd.help.usage', {"emoji":"🎨"}), value=f'`{invocation}{" " + usage if usage else ""}`')

       if hasattr(command, 'commands'):
          print('213')
       else:
         example = meta.get('example', [])
         invocation = ctx.prefix + (command.full_parent_name + ' ' if command.parent else '')
         if len(example) != 0:
            em.add_field(name=ctx.lang('cmd.help.example', {"emoji":"🎨", "total":len(example)}), value='\n'.join(f'`{invocation}{aliase[i] if -1 < i < len(aliase) else command.name} {e}`' for i, e in enumerate(example, -1)))
       
       em.add_field(name=ctx.lang('cmd.help.description', {"emoji":"🎨"}), value=f'`{description}`')
       em.add_field(name='\u200b', value=ctx.lang('cmd.help.suport', {"link":self.link.discord}), inline=False)
       em.set_footer(text=f"{ctx.me.name} © 2020", icon_url=ctx.me.avatar_url)

       return await ctx.send(embed=em)




    @commands.command(name='help')
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def _help(self, ctx, *, args=None):
        if args:
            command = self.kinash.get_command(args)
            if not command or command.hidden:
                return await ctx.send(ctx.lang('err.help.none', {"self":self.kinash, "ctx": ctx}))
            
            return await self.show_cmd(ctx, command)
        
        em = discord.Embed(color=self.kinash.color[0], title=ctx.lang('cmd.help.name', {"command": command.name.title()}))\
        .add_field(name=ctx.lang('cmd.help.usage', {"emoji":"🎨"}), value=f'`{cmd}{" " + usage if usage else ""}`')\
        .add_field(name=ctx.lang('cmd.help.aliase', {"emoji":"🎨", "total":(total_aliases := len(aliase))}), value=' | '.join([f'`{a}`' for a in aliases]) or ctx.lang('cms.no_defined'))\
        .add_field(name=ctx.lang('cmd.help.description', {"emoji":"🎨"}), value=f'`{description}`')\
        .add_field(name=ctx.lang('cmd.help.description', {"emoji":"🎨"}), value='\n'.join(f'`{invocation}{aliases[i] if -1 < i < total_aliases else command.name} {e}`' for i, e in enumerate(example, -1)))\
        .add_field(name='\u200b', value=ctx.lang('cmd.help.suport', {"link":ctx.lang('cms.suport')}), inline=False)
        await ctx.send(embed=em)

               
#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Utility(kinash))        