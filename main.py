from config import Letty
from discord import Game
from utils import prefix
import asyncio, os

bot = Letty(
            command_prefix=prefix,
            activity=Game(f'Starting... :3'),
            help_command=None,
            shard_ids=[int(x) for x in range(1)],
            shard_count=int(1)
            )

loop = asyncio.get_event_loop()
task_bot = loop.create_task(bot.start(os.environ['BOT_TOKEN']))
#task_web = loop.create_task(web.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)), loop=loop))
gathered = asyncio.gather(task_bot)
try:
  loop.run_until_complete(gathered)
except KeyboardInterrupt:
    pass
finally:
    loop.run_until_complete(bot.logout())
    loop.close()

