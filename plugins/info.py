#Import's necessários (List import).
import discord
from discord.ext import commands

#Classe do plugin 'Utilidade'
class Utility(commands.Cog):
    def __init__(self, kinash):
        """
         - Funções:
          self.kinash : Puxar as informações do bot pela classe Kinash.
        """
        self.kinash = kinash
        
    #Função pra gerar o embed do comando.
    async def show_cmd(self, ctx, command):
       #Nome do comando.
       name = command.qualified_name
       #As alternativa do comando.
       aliase = command.aliases
       #Puxar o prefixo mais o nome do comando.
       invocation = f'{ctx.prefix}{name}'
       #Puxar o meta com as traduções do comando.
       meta = ctx.lang(f'help.{name}') or {}
       #descrição do comando.
       description = meta.get('description', ctx.lang('cms.help.no_defined'))
       #Como usar o c[omando].
       usage = meta.get('usage')
       #Permissões do comando.
       perm = [f'{ctx.lang(f"perm.text."+a["text"])} [{ctx.lang(f"perm.user."+a["user"])}]' for a in meta.get('perm')]
       #Embed de ajuda ao usuário.
       em = discord.Embed(color=self.kinash.color[0], title=ctx.lang('cmd.help.name', {"name": name}))
       em.set_thumbnail(url=self.kinash.user.avatar_url)
       em.set_author(name=ctx.lang('cmd.help.helper'), icon_url=ctx.author.avatar_url)
       em.add_field(name=ctx.lang('cmd.help.aliase', {"self":self.kinash, "total":len(aliase)}), value='• '+' | '.join([f'`{a}`' for a in aliase]) or f"``{ctx.lang('cms.help.no_defined')}``", inline=False)
       em.add_field(name=ctx.lang('cmd.help.usage', {"self":self.kinash}), value=f'• `{invocation}{" " + usage if usage else ""}`', inline=False)
       em.add_field(name=ctx.lang('cmd.help.perm', {"self":self.kinash, "total":len(perm)}), value="• "+" | ".join([f"`{a}`" for a in perm]) or f"``{ctx.lang('cms.help.no_rank')}``", inline=False)
       #Quando houver sub-comandos.
       if hasattr(command, 'commands'):
          print('213')
       else:
         example = meta.get('example', [])
         invocation = ctx.prefix + (command.full_parent_name + ' ' if command.parent else '')
         if len(example) != 0:
            em.add_field(name=ctx.lang('cmd.help.example', {"self":self.kinash, "total":len(example)}), value='\n'.join(f'• `{invocation}{aliase[i] if -1 < i < len(aliase) else command.name}` `{e}`' for i, e in enumerate(example, -1)), inline=False)
       em.add_field(name=ctx.lang('cmd.help.description', {"self":self.kinash}), value=f'• `{description}`', inline=False)
       em.add_field(name='\u200b', value=ctx.lang('cmd.help.suport', {"self":self.kinash}), inline=False)
       em.set_footer(text=f"{ctx.me.name} © 2020", icon_url=ctx.me.avatar_url)
       return await ctx.send(embed=em)

    @commands.command(name='help')
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def _help(self, ctx, *, args=None):
        #Checar se a pessoa executou o comando e o dono.
        owner = await ctx.bot.is_owner(ctx.author)
        #Caso não houver argumentos irá mostrar todos os comandos.
        if args:
            #Puxar as informação do comando
            command = self.kinash.get_command(args)
            #Checar se o comando existe, e caso existir verificar se ele não estar "escondido" se caso estiver verificar se o author e o dono para mostra-lo.
            if not command or command.hidden and owner is False:
                return await ctx.send(ctx.lang('err.help.none', {"self":self.kinash, "ctx": ctx, "args":args}))
            #Puxar a informação do comando.
            return await self.show_cmd(ctx, command)
        #Embed com todo os comandos.
        em = discord.Embed(color=self.kinash.color[0], description=ctx.lang('cmd.help.link', {"self":self.kinash}))
        em.set_author(name=ctx.lang('cmd.help.helper'), icon_url=ctx.author.avatar_url)
        #Puxar todo os cogs do bot e enumerar-los.
        for name, cog in sorted(self.kinash.cogs.items(), reverse=True):
           #Ignorar comandos no cogs ['onwer', 'utility'] se o author for o dono enviar os comandos.
           if name.lower() in ['onwer', 'utility'] and owner is False:return
           #Listar todo os comandos do cog.
           cmds = [c for c in cog.get_commands()]
           value = ' | '.join(f'`{c}`' for c in cmds)
           #Se não houver comandos no cog.
           if value:
              em.add_field(name=ctx.lang(f'cmd.help.category.{name.lower()}', {"self":self.kinash, "total": len(cmds)}), value=value, inline=True)
        em.set_footer(text=f"{ctx.me.name} © 2020", icon_url=ctx.me.avatar_url)
        await ctx.send(embed=em)

               
#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Utility(kinash))        