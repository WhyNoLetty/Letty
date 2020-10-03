from quart import Quart
from .backend.route import Basic

class Dashboard:
    def __init__(self, *, letty):
        self.letty = letty
        self.app = Quart(__name__, static_folder="frontend/static", template_folder="frontend/templates")
        self.base = Basic(app=self.app, letty=self.letty)
       
