#import's necessários
from config import Shiro_bot, env
import asyncio

#Evento para puxar a classe da shiro e executar o token.    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(Shiro_bot.start(env.app.token))
    #loop.create_task(Shiro_site.run(host='127.0.0.1', port=5001, use_reloader=False, loop=loop))
    loop.run_forever()