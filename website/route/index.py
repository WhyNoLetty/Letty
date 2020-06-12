from quart import Quart
from quart.blueprints import Blueprint
from quart import session, render_template


class Index(Quart):
    def __init__(self, bot):
        self.bot = bot
        self.route = Blueprint('index', __name__, url_prefix="/")
        self.route.add_url_rule("/", 'index', self.index)
        self.route.add_url_rule("index", 'index', self.index)
        self.route.add_url_rule("guilds", 'indexs', self.guilds)
        self.route.add_url_rule("cmds", 'indexz', self.cmds)

    async def index(self):
        guilds = [g for g in self.bot.guilds]
        data = [len(guilds), sum(g.member_count for g in guilds if not g.unavailable)]
        return await render_template('index.html', data=data)

    async def guilds(self):
        return await render_template('guilds.html')

    async def cmds(self):
        return await render_template('cmds.html')        