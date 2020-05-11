#import's necessários
from config import Kinash, env
import discord

#Definir algumas coisas na classe da kinash como prefix, shards, game etc.
nix = Kinash(
             command_prefix=env.bot.prefix, 
             env=env,
             activity=discord.Game(f'www.kinash.xyz'),
             help_command=None,
             shard_ids=[int(x) for x in range(1)],
             shard_count=int(1)
             )
#Evento para puxar a classe da kinash e executar o token.
if __name__ == "__main__":
    nix.run(env.app.token)
