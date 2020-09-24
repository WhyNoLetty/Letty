import discord, json, traceback, sys
from config import get
from discord.ext import commands
from contextlib import redirect_stdout
import traceback, io, textwrap

class Owner(commands.Cog):
    def __init__(self, letty):
        self.letty = letty
        self.last_result = None

    def cleanup_code(self, content):
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')
    
    @commands.command(name='make')
    @commands.is_owner()
    async def _make(self, ctx, event):
       if event == 'emoji':
        array = {}
        for guild in self.letty.data.config.id.guild.emoji:
          for emoji in self.letty.get_guild(guild).emojis:
            array[emoji.name] = str(emoji)
        with open('./json/config/emoji.json', 'w+') as jsonf:
            json.dump(array, jsonf)
        self.letty.data.emoji = get("./json/config/emoji.json", type='obj')
        await ctx.send(await ctx.lang('command|make|success', {"ctx":ctx, "emoji":len(array)}))


    @commands.command(name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, code):
        env = {'bot': self.letty,'ctx': ctx,'channel': ctx.channel,'author': ctx.author,'guild': ctx.guild,'message': ctx.message}
        body = self.cleanup_code(code)
        stdout = io.StringIO()
        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'
        try:
            exec(to_compile, env)
        except Exception as e:
            value = f"{traceback.format_exc()}"
            return await ctx.send(await ctx.lang('command|eval|error', {"ctx":ctx, "code":value}))
        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            value = f"{value}{traceback.format_exc()}"
            return await ctx.send(await ctx.lang('command|eval|error', {"ctx":ctx, "code":value}))
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass
            if ret is None:
              if value:
                await ctx.send(await ctx.lang('command|eval|success', {"ctx":ctx, "code":value}))
            else:
              self.last_result = ret
              value = f"{value}{ret}"
              await ctx.send(await ctx.lang('command|eval|success', {"ctx":ctx, "code":value}))

def setup(letty):
    letty.add_cog(Owner(letty))        