#import's necessários
from config import Nixest, env

#Definir algumas coisas na classe da nixest como prefix, shards, game etc.
nix = Nixest(
             command_prefix=env.bot.prefix, 
             env=env
             )

#Evento para puxar a classe do Nixest e executar o token.
if __name__ == "__main__":
    nix.run(env.app.token)
