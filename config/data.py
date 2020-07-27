#Import's necessários (List import).
from json import load
from collections import namedtuple

# - Ler o arquivo e converter ele em objeto ou pega-lo puro.
def get(file, type='normal'):
	# - Tentar executar o evento.
    try:
      # - Abrir o arquivo com formatação uft8.	
      with open(file, encoding='utf8') as data:
      	  # - Checar se o typo de sair é 'obj'
          if type == 'obj':
          	 # - Retornar as informações em objeto.
             return load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
          # - Checar se o typo de sair é 'normal'
          elif type == 'normal':
          	 # - Retornar as informações em 'dict'
             return load(data)
    except Exception as e:
    	# - Caso houver um erro printa-lo.
        print(e)

# - Obter as informações do bot, como token, secret, ids, entre outros.
env = get("./json/config/env.json", type='obj')
