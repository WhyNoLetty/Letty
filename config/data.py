#Import's necessários (List import).
from json import load
from collections import namedtuple

# - Ler o arquivo e converter ele em objeto ou pega-lo puro.
def get(file, type='normal'):
    try:
      with open(file, encoding='utf8') as data:
          if type == 'obj':
             return load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
          elif type == 'normal':
             return load(data)
    except Exception as e:
        print(e)

# - Obter as informações do bot, como token, secret, ids, entre outros.
env = get("./json/config/env.json", type='obj')
