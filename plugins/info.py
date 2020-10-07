from discord.ext import commands
import discord

class Info(commands.Cog):
    def __init__(self, letty):
        self.letty = letty

    async def help_embed(self, ctx, command):
       qualified_name = command.qualified_name
       invocation = f'{ctx.prefix}{qualified_name}'
       aliase = command.aliases
       data = await ctx.lang(f'help|{"|".join(qualified_name.split(" "))}') or {}
       usage = data.get('usage')
       description = data.get('description', await ctx.lang('value|not_defined|f'))
       permission = [f'{await ctx.lang("permission|text|"+a["text"])} [{await ctx.lang("permission|user|"+a["user"])}]' for a in data.get('permission')] or await ctx.lang('value|not_need|permission')
       embed = discord.Embed(colour=self.letty.color[0])
       embed.set_author(name=await ctx.lang('command|help|user'), icon_url=ctx.author.avatar_url)
       embed.add_field(name=await ctx.lang('command|help|name', {"self":self.letty}), value=f"• `{command.name}`")
       embed.add_field(name=await ctx.lang('command|help|usage', {"self":self.letty}), value=f"• `{invocation}{f' {usage}' if usage != None else ''}`", inline=False)
       embed.add_field(name=await ctx.lang('command|help|aliase', {"self":self.letty, "count":len(aliase)}), value='• '+' | '.join([f'`{a}`' for a in aliase]) or f"`{await ctx.lang('value|not_defined|f')}`", inline=False)
       embed.add_field(name=await ctx.lang('command|help|permission', {"self":self.letty, "count":len(permission)}), value="• "+" | ".join([f"`{a}`" for a in permission]), inline=False)
       embed.set_thumbnail(url=ctx.me.avatar_url)
       if hasattr(command, 'commands'):
          examples = []
          for sub_command in command.commands:
              example_ = await ctx.lang(f'help|{command}|{sub_command.name}')
              example = example_.get("example")
              examples.append(f'`{invocation} {sub_command.name} {example[0]}`')
          embed.add_field(name=await ctx.lang('command|help|example', {"self":self.letty, "count":len(examples)}), value='• '+' | '.join(examples), inline=False)
          embed.add_field(name=await ctx.lang('command|help|sub', {"self":self.letty, "count":len(command.commands)}), value='• '+' | '.join([f'`{c.name}`' for c in command.commands]), inline=False)
          embed.add_field(name=await ctx.lang('command|help|description', {"self":self.letty}), value=f'• `{description}`', inline=False)
          embed.add_field(name="\u200b", value=await ctx.lang('command|help|invoke_subcommand', {"ctx":ctx,"command":command, "help":ctx.invoked_with if ctx.command.name == 'help' else 'help'}), inline=False)
       else:
         example = data.get('example', [])
         invocation = f"{ctx.prefix}{command.full_parent_name + ' ' if command.parent else ''}"
         embed.add_field(name=await ctx.lang('command|help|example', {"self":self.letty, "count":len(example)}), value='• '+' | '.join(f'`{invocation}{aliase[i] if -1 < i < len(aliase) else command.name} {e}`'for i, e in enumerate(example, -1)) or f"{await ctx.lang('value|not_defined|m')}", inline=False)
         embed.add_field(name=await ctx.lang('command|help|description', {"self":self.letty}), value=f'• `{description}`', inline=False)
       embed.add_field(name="\u200b", value=await ctx.lang('command|help|suport', {"self":self.letty}), inline=False)
       embed.set_footer(text=f"{ctx.me.name} © 2020" , icon_url=ctx.me.avatar_url)
       return embed

    @commands.command(name='help', aliases=['ajuda', 'commands', 'cmds'])
    @commands.bot_has_permissions(embed_links=True)
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def _help(self, ctx, *, args=None):
       if args:
          command = self.letty.get_command(args)
          if not command or command.hidden and not ctx.author.id in [692492572878176348]:
             return await ctx.send(await ctx.lang('command|help|hidden_or_not', {"ctx":ctx, "args":args}))
          embed = await self.help_embed(ctx, command)
          return await ctx.send(embed=embed)
       prefix = ctx.db.data['config']['prefix']
       embed = discord.Embed(colour=self.letty.color[0], description=await ctx.lang('command|help|description_full', {"self":self.letty, "prefix":prefix}))
       embed.set_author(name=await ctx.lang('command|help|list'), icon_url=ctx.author.avatar_url)
       embed.set_thumbnail(url=ctx.me.avatar_url)
       for name, cog in sorted(self.letty.cogs.items(), key=lambda c: c[0] == 'Music', reverse=True):
           cmds = [c for c in cog.get_commands() if not c.hidden]
           value = ' | '.join(f'`{c}`' for c in cmds)
           if value:
              embed.add_field(name=await ctx.lang(f'value|help|{name.lower()}', {"self":self.letty, "count":len(cmds)}), value=value, inline=True)
       
       embed.set_footer(text=f"{ctx.me.name} © 2020" , icon_url=ctx.me.avatar_url)
       return await ctx.send(embed=embed)

def setup(letty):
    letty.add_cog(Info(letty))        