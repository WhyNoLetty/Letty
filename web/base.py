from quart import Quart
from .backend.route import Basic
import os

class Dashboard:
    def __init__(self, *, letty):
        self.letty = letty
        self.app = Quart(__name__, static_folder="frontend/static", template_folder="frontend/templates")
        self.app.config['SECRET_KEY'] = os.environ['DASH_SECRET_KEY']
        self.base = Basic(app=self.app, letty=self.letty)
       
