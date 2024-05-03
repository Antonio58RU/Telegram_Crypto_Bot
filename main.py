import os
import asyncio
#import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from dotenv import load_dotenv
from database.models import async_main
from app import handlers, handlers_cmd, fsm
from bot_cmds_list import commands
import multiprocessing
from graphic24 import gr24
from graphic7 import gr7

async def main():
    print('Бот запущен!')
    load_dotenv()
    await async_main()
    bot = Bot(token = os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(handlers.router)
    dp.include_router(fsm.router)
    dp.include_router(handlers_cmd.router)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)

    
def start_main():
    try:
        asyncio.run(main())
    except:
        print('Exit1')

def start_gr24():
    gr24()
  
def start_gr7():
    gr7()

        
if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO)
    process_main = multiprocessing.Process(target=start_main)
    process_gr24 = multiprocessing.Process(target=start_gr24)
    process_gr7 = multiprocessing.Process(target=start_gr7)

    process_main.start()
    process_gr24.start()
    process_gr7.start()


    process_main.join()
    #process_gr24.join()
    #process_gr7.join()
    
