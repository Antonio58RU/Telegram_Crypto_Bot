from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keybords as kb
import database.requests as rq

from translations import _

router = Router()
    
@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    lang = await rq.get_localization(message.from_user.id)   
    await message.answer(_('<b>🌟 Привет! Добро пожаловать в нашего бота! 🌟</b>\n\n📈 <b>CryptoStats:</b> Будьте в курсе цен, получайте статистику, графики и калькулятор крипты прямо в Telegram. 📉\n\nНе пропустите ни одной важной детали в мире криптовалют! 💰💻📊', lang), reply_markup=kb.mainRp(lang), parse_mode='html')

  
@router.message(Command('settings'))
async def cmd_start(message: Message):
     lang = await rq.get_localization(message.from_user.id) 
     await message.answer(text=_('⚙️ <b>Настройки</b>', lang), reply_markup=kb.settingsCmdIn(lang), parse_mode='html')
     
@router.message(Command('help'))
async def cmd_start(message: Message):
     lang = await rq.get_localization(message.from_user.id) 
     await message.answer(text=_('<b>🚀 Вы можете использовать следующие команды:</b>\n\n/start - Запуск бота\n/settings - Настройки\n/help - Помощь\n\nЕсли у вас возникли вопросы или нужна помощь, не стесняйтесь обращаться к нам! 😊\nhttps://t.me/AntonBog123\n\nУдачного использования! 💫', lang), parse_mode='html')
