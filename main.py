#Import's necessários (List import).
from config import harumi, config, staff
from discord import Game
from utils import prefix
import asyncio, os

# - Setar as variaveis na classe da Harumi
bot = harumi(
             staff=staff,
             config=config,
             link=link,
             command_prefix=prefix,
             activity=Game(f'with mr.roxanne | h.help'),
             help_command=None,
             shard_ids=[int(x) for x in range(1)],
             shard_count=int(1)
             )

# - Iniciar o loop de evento das task.
loop = asyncio.get_event_loop()
# - Criação da task do bot.
bot = loop.create_task(bot.start(os.environ['BOT_TOKEN']))
# - Criação da task dashboard.
# web = loop.create_task(web.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)), loop=loop))
# - Aguardar as 2 task, e quando for criadas executa-las.
gathered = asyncio.gather(bot)
try:
  # - Executar as task após ser completadas.
  loop.run_until_complete(gathered)
except KeyboardInterrupt:
    # - Ignorar interrupção por teclado (CRLT + D)
    pass
finally:
    # - Desconectar o bot caso tenha algum erro na task.
    loop.run_until_complete(bot.logout())
    loop.close()

