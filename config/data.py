#Import's necessários (List import).
import json, re, os
from collections import namedtuple

#Ler o arquivo .json e converter ele em objeto.
def get(file):
    try:
      with open(file, encoding='utf8') as data:
          return json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    except Exception as e:
        print(e)

#Carregar dos como token, secret, prefix, etc.
env = get("./json/config.json")

#Carregar os emojis
emoji = get("./json/emoji.json")