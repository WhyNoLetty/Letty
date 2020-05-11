#Import's necessários (List import).
import discord
from discord.ext import commands

#Classe do plugin 'Utilidade'
class Utility(commands.Cog):
    def __init__(self, kinash):
        self.kinash = kinash
    
    async def command_help(self, ctx, command):
        qualified_name = command.qualified_name
        cmd = f'{ctx.prefix}{qualified_name}'
        print(cmd)
        aliases = command.aliases
        metadata = ctx.lang(f'cmd.{qualified_name}.meta') or {}
        description = metadata.get('description', ctx.lang('cms.no_supplied'))
        usage = metadata.get('usage')
        
        example = metadata.get('example', [])
        invocation = ctx.prefix + (command.full_parent_name + ' ' if command.parent else '')

        em = discord.Embed(color=self.kinash.color[0], title=ctx.lang('cmd.help.name', {"command": command.name.title()}))\
        .add_field(name=ctx.lang('cmd.help.usage', {"emoji":"🎨"}), value=f'`{cmd}{" " + usage if usage else ""}`')\
        .add_field(name=ctx.lang('cmd.help.aliase', {"emoji":"🎨", "total":(total_aliases := len(aliases))}), value=' | '.join([f'`{a}`' for a in aliases]) or ctx.lang('cms.no_defined'))\
        .add_field(name=ctx.lang('cmd.help.description', {"emoji":"🎨"}), value=f'`{description}`')\
        .add_field(name=ctx.lang('cmd.help.description', {"emoji":"🎨"}), value='\n'.join(f'`{invocation}{aliases[i] if -1 < i < total_aliases else command.name} {e}`' for i, e in enumerate(example, -1)))\
        .add_field(name='\u200b', value=ctx.lang('cmd.help.suport', {"link":ctx.lang('cms.suport')}), inline=False)
        await ctx.send(embed=em)



    @commands.command(name='help', aliases=['ajuda', 'commands', 'cmds'])
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def _help(self, ctx, *, args=None):
        if args:
            cmd = self.kinash.get_command(args)
            if not cmd or cmd.hidden:
                return await ctx.send(ctx.lang('cmd.help.none.cmd', {"author": ctx.author.name, "emoji": "?"}))

            await self.command_help(ctx, cmd)
            return
        
        em = discord.Embed(color=self.kinash.color[0], title=ctx.lang('cmd.help.name', {"command": command.name.title()}))\
        .add_field(name=ctx.lang('cmd.help.usage', {"emoji":"🎨"}), value=f'`{cmd}{" " + usage if usage else ""}`')\
        .add_field(name=ctx.lang('cmd.help.aliase', {"emoji":"🎨", "total":(total_aliases := len(aliases))}), value=' | '.join([f'`{a}`' for a in aliases]) or ctx.lang('cms.no_defined'))\
        .add_field(name=ctx.lang('cmd.help.description', {"emoji":"🎨"}), value=f'`{description}`')\
        .add_field(name=ctx.lang('cmd.help.description', {"emoji":"🎨"}), value='\n'.join(f'`{invocation}{aliases[i] if -1 < i < total_aliases else command.name} {e}`' for i, e in enumerate(example, -1)))\
        .add_field(name='\u200b', value=ctx.lang('cmd.help.suport', {"link":ctx.lang('cms.suport')}), inline=False)
        await ctx.send(embed=em)

               
#Adicionar o plugin na lista.
def setup(kinash):
    kinash.add_cog(Utility(kinash))        