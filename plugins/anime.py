#Import's necessários (List import).
import discord
from discord.ext import commands
from asyncio import TimeoutError as TimeoutException

#Classe do plugin 'Anime'
class Anime(commands.Cog):
    def __init__(self, shiro):
        self.shiro = shiro

    #O comando 'anime' pra puxar as info de animes.
    @commands.command()
    async def anime(self, ctx, type='Nonse', *,query=None):
        print(type, query)
        
        if not type.lower() in ['anime', 'manga']: return await ctx.send(ctx.lang("cmd.anime.string.type",{'emoji':'⁉️'}))
        if query is None: return await ctx.send(ctx.lang("cmd.anime.string.query",{'emoji':'⁉️'}))
        
        anime = await self.shiro.mal.search(type, query, limit=8)
        if len(anime) == 0:
           return await ctx.send('sem anime')

        lista = [f'`»` `{i}` [{x.title}]({x.url})' for i, x in enumerate(anime, 1)]
        cancel = ctx.lang("cmd.anime.string.exit")

        em = discord.Embed(color=0x363651,description=ctx.lang("cmd.anime.choose", {'lista':'\n'.join(lista)}))\
        .set_author(name=ctx.lang('cmd.anime.results'),icon_url=ctx.author.avatar_url)\
        .set_thumbnail(url=self.shiro.user.avatar_url)\
        .set_footer(text=ctx.lang('cmd.anime.cancel', {'value':cancel}))
        q = await ctx.send(content=ctx.author.mention, embed=em)

        def check(m):
            return m.channel.id == q.channel.id and m.author.id == ctx.author.id and (m.content.isdecimal() and 0 < int(m.content) <= len(anime) or m.content.lower() == cancel)

        try:
            a = await self.shiro.wait_for('message', timeout=120, check=check)
        except TimeoutException:
            a = None

        if a is None or a.content.lower() == cancel:
            return await q.delete()
        
        unknown = ctx.lang("cmd.anime.string.unknown")
        anime = anime[int(a.content) - 1]
        
        full_synopsis = ctx.lang('cmd.anime.read', {"url": anime.url}),
        if len(anime.synopsis) > 2048:
            anime.synopsis = anime.synopsis[:2048 - len(full_synopsis)] + full_synopsis

        em = discord.Embed(color=0x363651, title=f"**{anime.title}**", description=anime.synopsis or ctx.lang('commands.anime.string.no_synopsis'))\
        .set_author(name=ctx.lang('cmd.anime.info', {"type": type.title()}),icon_url=ctx.author.avatar_url)\
        .set_thumbnail(url=anime.image_url)\
        .set_footer(text=str(ctx.author))
        await q.edit(content=None, embed=em)

#Adicionar o plugin na lista.
def setup(shiro):
    shiro.add_cog(Anime(shiro))        