from quart import Blueprint, render_template, redirect, request, session, url_for
from functools import wraps
from web.oauth import Api
from web.utils import Filter

class Basic:
    def __init__(self, *, app, letty):
        self.app = app
        self.letty = letty
        self.blueprint = Blueprint("basic", __name__)
        self.oauth = Api(letty=self.letty)
        self.filter = Filter(app=self.app)

        
        @self.blueprint.route("/")
        @self.blueprint.route("/index")
        async def index():
             lang = await self.letty.lang.get('pt_BR')
             guilds = [g for g in self.letty.guilds]
             members = sum(g.member_count for g in guilds if not g.unavailable)
             return await render_template("index.html", lang=lang, guilds=len(guilds), members=members, user=None, route='index')
        
        
        @self.blueprint.route("/url/<value>")
        async def url(value):
           return redirect(await self.oauth.url(value=value, data=request.args))

        @self.blueprint.route("/commands")
        async def cmds():
           lang = await self.letty.lang.get('pt_BR')
           return await render_template("cmds.html", lang=lang, bot=self.letty, route='cmds', user=None)


        self.app.register_blueprint(self.blueprint, url_prefix="/")
        
