from json import load
from collections import namedtuple
from dotenv import load_dotenv

__all__ = ("Cache", "Config")

def get(file, type="normal"):
    try:
      with open(file, encoding="utf8") as data:
          if type == "obj":
             return load(data, object_hook=lambda d: namedtuple("X", d.keys())(*d.values()))
          elif type == "normal":
             return load(data)
    except Exception as e:
        print(e)

class Config:
    def __init__(self):
      self.config = get("./json/config/config.json", type="obj")
      self.staff = get("./json/config/staff.json", type="obj")
      self.link = get("./json/config/link.json", type="obj")
      self.emoji = get("./json/config/emoji.json", type="obj")

class Cache:
    __slots__ = ("prefix")
    def __init__(self):
        self.prefix = {}

    def clear(self) -> None:
        for attr in [getattr(self, attr) for attr in self.__slots__]:
            if hasattr(attr, "clear"):
                attr.clear()
            else:
               setattr(self, attr.__name__, attr.__class__())

load_dotenv("./json/config/.env")