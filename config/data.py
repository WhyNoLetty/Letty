#Import's necessários (List import).
from json import load
from collections import namedtuple
from dotenv import load_dotenv

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

# - Classe com dados, configurações entre outros da Harumi.
class kwarg:
    def __init__(self):
      # - Obter as informações da Harumi, cor de embed, lista de ignoração, ids, entre outros.
      self.config = get("./json/config/config.json", type='obj')
      # - Obter a listagem de staff da Harumi.
      self.staff = get("./json/config/staff.json", type='obj')
      # - Obter a listagem de links uteís da Harumi.
      self.link = get("./json/config/link.json", type='obj')
      # - Obter a listagem de emojis da Harumi.
      self.emoji = get("./json/config/emoji.json", type='obj')

# - Carregar os valores do .env.
load_dotenv("./json/config/.env")

