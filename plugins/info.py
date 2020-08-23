#Import's necessários (List import).
import discord
from discord.ext import commands
import os
from json import load

#Classe do plugin 'Base'
class Base(commands.Cog):
    def __init__(self, harumi):
        """
         - Funções:
          self.harumi : Puxar as informações do bot pela classe harumi.
        """
        self.harumi = harumi
    
    async def command_help(self, ctx, command):
       # - O nome completo do comando.
       name_full = command.qualified_name
       # - Prefixo atual mais o nome comando.        
       invocation = f'{ctx.prefix}{name_full}'
       # - As alternativas de nome do comando.
       aliases = command.aliases
       # - Informações do comando.
       data = ctx.lang(f'help.{".".join(name_full.split(" "))}') or {}
       # - Como usar o comando.
       usage = data.get('usage')
       # - Descrição do comando.
       description = data.get('description', ctx.lang("exception.help.description"))
       # - Lista de permissões necessária para executar o comando.
       permission = [f'{ctx.lang(f"permission.text."+a["text"])} [{ctx.lang(f"permission.user."+a["user"])}]' for a in data.get('permission')]
       # - Criação do embed com as informações.
       em = discord.Embed(colour=self.harumi.color[0], title=ctx.lang('command.help.name', {"command": command.name.title()}))
       em.set_author(name=ctx.lang('command.help.helper'), icon_url=ctx.author.avatar_url)
       em.add_field(name=ctx.lang('command.help.aliase'), value=' | '.join([f'• `{a}`' for a in aliases]) or f'• ``{ctx.lang("exception.help.aliase")}``', inline=False)
       em.add_field(name=ctx.lang('command.help.usage'), value=f'• ``{invocation}{" " + usage if usage else ""}``', inline=False)
       em.add_field(name=ctx.lang('command.help.permission'), value=' | '.join([f'• `{a}`' for a in permission]) or f'``• {ctx.lang("exception.help.permission")}``', inline=False)
       em.set_thumbnail(url=self.harumi.user.avatar_url)
       # - Checar se o comando tem sub-comandos.
       if hasattr(command, 'commands'):
          pass
       else:
         # - Exemplos de usos do comando.
         example = data.get('example', [])
         # - O nome completo do comando.
         invocation = ctx.prefix + (command.full_parent_name + ' ' if command.parent else '')
         em.add_field(name=ctx.lang('command.help.example'), value='\n'.join(f'• ``{invocation}{aliases[i] if -1 < i < len(aliases) else command.name} {e}``' for i, e in enumerate(example, -1)), inline=False)
       em.add_field(name=ctx.lang('command.help.description'), value=f'• ``{description}``', inline=False)
       em.add_field(name="\u200b", value=ctx.lang('command.help.suport', {"self":self.harumi}), inline=False)
       em.set_footer(text=f"{ctx.me.name} © 2020", icon_url=ctx.me.avatar_url)
       return await ctx.send(embed=em)

    #Comando de ajuda para o usuário.
    @commands.command(name='help', aliases=['oi'])
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def _help(self, ctx, *, args=None):
       # - Checar se a pessoa executou o comando e o dono.
       owner = await ctx.bot.is_owner(ctx.author)
       # - Caso não houver argumentos irá mostrar todos os comandos.
       if args:
          # - Puxar as informação do comando caso o mesmo existir.
          command = self.harumi.get_command(args)
          # - Checar se o comando existe, e caso existir verificar se ele não estar "escondido" se caso estiver verificar se o author e o dono para mostra-lo.
          if not command or command.hidden and owner is False:
             return await ctx.send(ctx.lang('exception.help.found', {"self":self.harumi, "ctx": ctx, "command":args}))
          # - Executar a função pra puxar o embed com as informações com o comando.
          return await self.command_help(ctx, command)
       # - Criação do embed com as informações dos comandos.
       em = discord.Embed(colour=self.harumi.color[0], title=ctx.lang('command.help.update'), description=ctx.lang('command.help.help', {'prefix':self.harumi.cache.prefix[ctx.guild.id]}), url=self.harumi.data.link.suport)
       em.set_author(name=ctx.lang('command.help.list'), icon_url=ctx.me.avatar_url, url=self.harumi.data.link.website)
       # - Passar todo os modulos da Harumi em um for e sortea-los.
       for name, cog in sorted(self.harumi.cogs.items(), key=lambda c: c[0] == 'Music', reverse=True):
          # - Pegar apenas os comandos visível do modulo.
          cmds = [c for c in cog.get_commands() if not c.hidden]
          # - Dar um join com todo os comandos.
          value = ' '.join(f'`{c}`' for c in cmds)
          # - Caso houver comandos no modulo adicionar no embed.
          if value:
             em.add_field(name=ctx.lang('command.help.category', {"total": len(cmds), "category": ctx.lang(f'convert.help.{name.lower()}')}), value=value, inline=True)
       em.set_footer(text=f"{ctx.me.name} © 2020", icon_url=ctx.me.avatar_url)
       return await ctx.send(embed=em)

#Adicionar o plugin na lista.
def setup(harumi):
    harumi.add_cog(Base(harumi))        