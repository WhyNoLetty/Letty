
# - Listagem de objetos cache "publicos".
__all__ = ('Cache')

# - Classe da Harumi para armazenar algumas informações em "cache".
class cache:
    # - Incluir atributos na instancia.
    __slots__ = ('guild_prefixes')
    def __init__(self):
    	# - Prefixo dos servidores
        self.guild_prefixes = {}

    # - Limpar o totalmente o cache.
    def clear(self) -> None:
    	# - Pegar um atributo da instancia e passa-lo por um for.
        for attr in [getattr(self, attr) for attr in self.__slots__]:
        	# - Verificar o atributo.
            if hasattr(attr, 'clear'):
            	# - Limpar a lista.
                attr.clear()
            else:
               # - Setar o atributo.
               setattr(self, attr.__name__, attr.__class__())