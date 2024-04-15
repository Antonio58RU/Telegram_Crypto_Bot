import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config import TOKEN
from app.handlers import router

from bot_cmds_list import commands

bot = Bot(token = TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
    