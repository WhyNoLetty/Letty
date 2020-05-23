#Import's necessários (List import).
import json, re, os
from collections import namedtuple

#Ler o arquivo .json e converter ele em objeto ou pega-lo puro.
def get(file, simple=False):
    try:
      with open(file, encoding='utf8') as data:
          if simple is False:
             return json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
          elif simple is True:
             return json.load(data)
    except Exception as e:
        print(e)

#Carregar dos como token, secret, prefix, etc.
env = get("./json/config.json")

#Carregar os emojis
emoji = get("./json/emoji.json")

#Carregar os emojis
download = get("./json/down.json")