from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keybords as kb
import database.requests as rq

from translations import _, get_lang
import requests 


router = Router()
     
@router.message((F.text == '🏦 Статистика') | (F.text == '🏦 Statistics'))
async def get_stats(message: Message):
    await message.answer(get_messageStats(), reply_markup=kb.mainIn(await get_lang(message.from_user.id)), parse_mode='html')
    
@router.callback_query(F.data == 'updateStats')
async def update_stats(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(get_messageStats(), reply_markup=kb.mainIn(await get_lang(callback.from_user.id)), parse_mode='html')
    
@router.callback_query(F.data == 'listcrypto')
async def get_cryptoList(callback: CallbackQuery):
    await callback.answer('')
    cryptocurrencies = {
    "Bitcoin": "BTC",
    "Ethereum": "ETH",
    "Solona": "SOL",
    "First Digital USD": "FDUSD",
    "USD Coin": "USDC",
    "Pepe": "PEPE",
    "Binance Coin": "BNB",
    "XRP": "XRP",
    "Dogecoin": "DOGE",
    "Tether": "USDT"
}

    result = ""
    for currency, symbol in cryptocurrencies.items():
        result += f"<b>{currency}</b>({symbol})\n"
    await callback.message.answer(result,reply_markup=kb.backStatsIn , parse_mode='html')

        
@router.callback_query(F.data == 'backStatsFull')
async def back_statsFull(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(get_messageStats(), reply_markup=kb.mainIn(lang(callback.from_user.id)), parse_mode='html')



@router.message((F.text == '💼 Профиль') | (F.text == '💼 Profile'))
async def get_statsProfil(message: Message):
    user = await rq.get_user(message.from_user.id)
    await message.answer(_(get_profilStats(), user.language).format(message.from_user.full_name, premiumStatus(user.premium), user.registr_date), reply_markup=kb.profileIn(await get_lang(message.from_user.id)), parse_mode='html')

@router.callback_query(F.data == 'settings')
async def settings(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='⚙️ <b>Настройки</b>', reply_markup=kb.settingsIn, parse_mode='html')
    
@router.callback_query(F.data == 'setLang')
async def settings(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='<b>Выберите язык</b>', reply_markup=kb.languagesIn, parse_mode='html')
    
@router.callback_query(F.data.startswith('lang_'))
async def set_language(callback: CallbackQuery):
    await callback.answer('')
    lang = callback.data[5:]
    await rq.set_lang(callback.from_user.id, lang)
    if lang == 'ru':
        message_text = '<b>Русский язык установлен.</b>'
    else:
        message_text = '<b>English language is set.</b>'
    
    await callback.message.answer(text=message_text, reply_markup=kb.mainRp(lang), parse_mode='html') 
    
@router.callback_query(F.data == 'backProfil')
async def back_Profil(callback: CallbackQuery):
    await callback.answer('')
    user = await rq.get_user(callback.from_user.id)
    await callback.message.answer(_(get_profilStats(), user.language).format(callback.message.from_user.full_name, premiumStatus(user.premium), user.registr_date), reply_markup=kb.profileIn(await get_lang(callback.message.from_user.id)), parse_mode='html')

  
@router.callback_query(F.data == 'help')
async def support(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='/start - Запуск бота\n/setting - Настройки\n/help Помощь\n\nhttps://t.me/AntonBog123', reply_markup=kb.backProfilIn)
  
  
  
  
       
@router.message((F.text == '📕 О сервисе') | (F.text == '📕 About the Service'))
async def get_info(message: Message):
    photo = FSInputFile('Images/photoInfo.jpeg')
    await message.answer_photo(photo=photo, caption='<b>Данный сервис позволяет быть в курсе актуальных цен на криптовалюты, получать подробную статистику о рынке, получать прогнозы продаж и использовать удобный калькулятор для расчета криптовалюты - все это доступно прямо в Telegram. Благодаря этому сервису вы сможете быть в курсе последних изменений на рынке и принимать осознанные решения в области криптовалютных инвестиций.</b>', parse_mode='html')
    
    
    
    
    
    
@router.message((F.text == '👑 Премиум функционал') | (F.text == '👑 Premium Functionality'))
async def premium_func(message: Message):
    user = await rq.get_user(message.from_user.id)
    if(user.premium == True):
        await message.answer('👑 <b>Премиум функционал</b>', reply_markup=kb.premiumIn, parse_mode='html')
    else:
        await message.answer('Приобретите премиум доступ чтобы пользоваться данными функционалом', reply_markup=kb.premiumBuyIn)
       
@router.callback_query(F.data == 'buyPremium')
async def buy_premium(callback: CallbackQuery):
    await callback.answer('')
    user = await rq.get_user(callback.from_user.id)
    if(user.premium == True):
        await callback.message.answer(text='Вы уже приобрели премиум статус.')
    else:
        await rq.update_user_premium_status(callback.from_user.id)
        await callback.message.answer(text='Премиум куплен!')
    


            
@router.callback_query(F.data == 'backPremium')
async def backPremium(callback: CallbackQuery):
    await callback.answer('')
    user = await rq.get_user(callback.from_user.id)
    if(user.premium == True):
        await callback.message.answer('👑 <b>Премиум функционал</b>', reply_markup=kb.premiumIn, parse_mode='html')
    else:
        await callback.message.answer('Приобретите премиум доступ чтобы пользоваться данными функционалом', reply_markup=kb.premiumBuyIn)
    
    
def get_profilStats():
    return '<b>Логин:</b> {}\n<b>Статус:</b> {}\n<b>Зарегистрирован:</b> {}'

    
def get_messageStats():
    
    cryptocurrencies = ["BTC", "ETH", "USDT", "BNB", "SOL"]
    fsyms = ','.join(cryptocurrencies)

    url = f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={fsyms}&tsyms=USD'
    r = requests.get(url)
    json_data = r.json()

    messageStats_text = "🏦<b>CryptoStats</b>\n\n"

    for currency in cryptocurrencies:
        price = round(json_data["RAW"][currency]["USD"]["PRICE"],5)
        change24h =  round(json_data["RAW"][currency]["USD"]["CHANGEPCT24HOUR"],5)
        
        messageStats_text += f"<b>{currency}:=</b><i>{price}$</i>, <b>24h:</b> <i>{change24h}%</i>\n"
    return messageStats_text

def premiumStatus(premium: bool):
    if(premium == False):    
        return 'Стандарт'
    return 'Премиум'









