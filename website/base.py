from quart import Quart
from .route import Index

class Server(Quart):
  def __init__(self, env, db, bot):
    super().__init__(__name__, static_folder="static", template_folder="templates")
   
    self.config['SECRET_KEY'] = '123'
    self.register_blueprint(Index(bot).route)


  def run(self):
      super().run(host='0.0.0.0', port=5000)