import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from dotenv import load_dotenv

from database.models import async_main

from app.handlers import router

from bot_cmds_list import commands


async def main():
    load_dotenv()
    await async_main()
    bot = Bot(token = os.getenv('TOKEN'))
    await bot(DeleteWebhook(drop_pending_updates=True))
    dp = Dispatcher()
    dp.include_router(router)
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
    