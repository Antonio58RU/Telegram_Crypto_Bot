from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keybords as kb
import database.requests as rq

from translations import _, get_lang

router = Router()
    
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await rq.set_user(message.from_user.id)
    await message.answer('CryptoStats: Будьте в курсе цен, получайте статистику, прогнозы продаж и калькулятор крипты прямо в Telegram.', reply_markup=kb.mainRp(await get_lang(message.from_user.id)))
    await state.clear()
  
@router.message(Command('settings'))
async def cmd_start(message: Message):
     await message.answer(text='⚙️ <b>Настройки</b>', reply_markup=kb.settingsCmdIn, parse_mode='html')
     
@router.message(Command('help'))
async def cmd_start(message: Message):
     await message.answer(text='/start - Запуск бота\n/setting - Настройки\n/help Помощь\n\nhttps://t.me/AntonBog123')