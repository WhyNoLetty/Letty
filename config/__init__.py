#import's necessários
from .base import Shiro
from .data import env, emoji, get
from .http import get_aio, post_aio


"""
- Observação:
 O Arquivo __init__.py vai ser meio que uma importação 'global'
 de todo os modulos e configuração da pasta CONFIG.
"""