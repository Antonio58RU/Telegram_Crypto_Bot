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
    await message.answer(_('<b>CryptoStats:</b> Будьте в курсе цен, получайте статистику, графики и калькулятор крипты прямо в Telegram.', await get_lang(message.from_user.id)), reply_markup=kb.mainRp(await get_lang(message.from_user.id)), parse_mode='html')
    await state.clear()
  
@router.message(Command('settings'))
async def cmd_start(message: Message):
     await message.answer(text=_('⚙️ <b>Настройки</b>', await get_lang(message.from_user.id)), reply_markup=kb.settingsCmdIn, parse_mode='html')
     
@router.message(Command('help'))
async def cmd_start(message: Message):
     await message.answer(text=_('/start - Запуск бота\n/settings - Настройки\n/help Помощь\n\nhttps://t.me/AntonBog123', await get_lang(message.from_user.id)))