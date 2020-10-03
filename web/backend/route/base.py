from quart import Blueprint, render_template


class Basic:
    def __init__(self, *, app, letty):
        self.app = app
        self.letty = letty
        self.blueprint = Blueprint("user", __name__)
        
        @self.blueprint.route("/")
        @self.blueprint.route("/index")
        async def index():
             db = await self.letty.db.get_guild(757616076166004846)
             return await render_template("index.html")
        

        self.app.register_blueprint(self.blueprint, url_prefix="/")
