from quart import Blueprint, render_template, redirect, request, session, jsonify
from functools import wraps
from web.oauth import Api
from web.utils import Filter, require_auth

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
             return await render_template("index.html", bot=self.letty, lang=lang, guilds=len(guilds), members=members, user=None, route='index')
        
        
        @self.blueprint.route("/url/<value>")
        async def url(value):
           return redirect(await self.oauth.url(value=value, data=request.args))

        @self.blueprint.route("/commands")
        async def cmds():
           lang = await self.letty.lang.get('pt_BR')
           return await render_template("cmds.html", lang=lang, bot=self.letty, route='cmds', user=None)

        @self.blueprint.route("/callback")
        async def callback():
           callback = await self.oauth.callback(data=request.args)
           if callback is None:
              return redirect("/")
           
           session['token'] = callback['access_token']
           return redirect("/user")
        
        @self.blueprint.route("/user")
        @require_auth
        async def user():
           callback = await self.oauth.get_user(data=session)
           return jsonify(callback)
        
        @self.blueprint.route("/guild")
        @require_auth
        async def guild():
           callback = await self.oauth.get_user(data=session, endpoint='@me/guilds')
           return jsonify(callback)        
        

        self.app.register_blueprint(self.blueprint, url_prefix="/")
        
