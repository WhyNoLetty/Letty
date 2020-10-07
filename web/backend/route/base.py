from quart import Blueprint, render_template


class Basic:
    def __init__(self, *, app, letty):
        self.app = app
        self.letty = letty
        self.blueprint = Blueprint("user", __name__)
        
        @self.blueprint.route("/")
        @self.blueprint.route("/index")
        async def index():
             lang = await self.letty.lang.get('pt_BR')
             return await render_template("index.html", lang=lang)
        
        self.app.register_blueprint(self.blueprint, url_prefix="/")
