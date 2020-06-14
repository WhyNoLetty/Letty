from quart import Quart
from quart.blueprints import Blueprint
from quart import session, render_template, request
import quart.flask_patch
from flask import Markup

class Filter():
    def __init__(self, name):
        self.name = name

    def aliases(self, cmd):
        html = []
        for aliase in cmd.aliases:
            html.append(aliase)
        return html        
        #return Markup(html)
    
    def examples(self, cmd, example):
        aliase = cmd.aliases
        if hasattr(cmd, 'commands'):
           return []
        else:
         invocation = 's.' + (cmd.full_parent_name + ' ' if cmd.parent else '')
         if len(example) != 0:
            gg =  (f'{invocation}{aliase[i] if -1 < i < len(aliase) else cmd.name} {e}' for i, e in enumerate(example, -1))
            print(gg)
            return gg
         return []
    
    def permission(self, perm, list):
        html = []
        for txt in perm:
            text = f'{list["text"][txt["text"]]} [{list["user"][txt["user"]]}]'
            html.append(text)
        return html      
        #return Markup(html)      

class Index(Quart):
    def __init__(self, bot):
        self.bot = bot
        self.route = Blueprint('index', __name__, url_prefix="/")
        self.filter = Filter('index')
        
        self.route.add_url_rule("/", 'index', self.index)
        self.route.add_url_rule("index", 'index', self.index)
        self.route.add_url_rule("guilds", 'indexs', self.guilds)
        self.route.add_url_rule("cmds", 'indexz', self.cmds)
        
        self.route.add_app_template_filter(self.filter.aliases)
        self.route.add_app_template_filter(self.filter.examples)
        self.route.add_app_template_filter(self.filter.permission)


    async def index(self):
        guilds = [g for g in self.bot.guilds]
        data = [len(guilds), sum(g.member_count for g in guilds if not g.unavailable)]
        lang  = request.args.get("lang", 'pt_BR')
        if not lang in ['pt_BR', 'en_US']:
           lang = 'pt_BR'
        translate = self.bot.lang.get(lang)        
        return await render_template('index.html', data=data, translate=translate)

    async def guilds(self):
        return await render_template('guilds.html')

    async def cmds(self):
        check = request.args.get("admin", False)
        lang  = request.args.get("lang", 'pt_BR')
        if not lang in ['pt_BR', 'en_US']:
           lang = 'pt_BR'
        translate = self.bot.lang.get(lang)
        modules = ['onwer', 'event'] if check == False else []
        return await render_template('cmds.html', bot=self.bot, modules=modules, lang=lang, translate=translate)        