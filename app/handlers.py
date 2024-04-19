from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keybords as kb

import requests 

cryptocurrencies = ["BTC", "ETH", "USDT", "BNB", "SOL"]
prices = {}
changes24h = {}

router = Router()

class StatsFull(StatesGroup):
    nameCrypto = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('@cryptostats58_bot: Будьте в курсе цен, получайте статистику, прогнозы продаж и калькулятор крипты прямо в Telegram.', reply_markup=kb.mainRp)
      
@router.message(F.text == '🏦 Статистика Binance')
async def get_stats(message: Message):
    await message.answer(get_messageStats(), reply_markup=kb.mainIn, parse_mode='html')
    
@router.callback_query(F.data == 'updateStats')
async def update_stats(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(get_messageStats(), reply_markup=await kb.mainIn, parse_mode='html')
    
@router.callback_query(F.data == 'getStatsFull')
async def get_statsFull(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(StatsFull.nameCrypto)
    await callback.message.answer('Введите название криптовалюты для получения её полной информации.', parse_mode='html')
    
@router.message(StatsFull.nameCrypto)
async def StatsFull_stats(message: Message, state: FSMContext):
    await state.update_data(nameCrypto = message.text)
    data = await state.get_data()
    await message.answer_photo(photo=f'https://images.cryptocompare.com/sparkchart/{data['nameCrypto']}/USD/latest.png?ts=1713464400', caption=get_messageStatsFull(data), reply_markup=await kb.statsFullIn, parse_mode='html')
    await state.clear()
    
@router.callback_query(F.data == 'backStatsFull')
async def back_statsFull(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(get_messageStats(), reply_markup=await kb.mainIn, parse_mode='html')

@router.message(F.text == '💼 Профиль')
async def get_statsProfil(message: Message):
    await message.answer(f'<b>Логин:</b> {message.from_user.full_name}\n<b>Статус:</b> Vip\n<b>Зарегистрирован:</b> 01-01-1888', reply_markup=await kb.profileIn, parse_mode='html')

@router.callback_query(F.data == 'settings')
async def settings(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='<b>Выберите язык</b>', reply_markup=await kb.langIn, parse_mode='html')
     
@router.callback_query(F.data == 'support')
async def support(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='https://t.me/AntonBog123')
       
@router.message(F.text == '📕 О сервисе')
async def get_info(message: Message):
    photo = FSInputFile('Images/photoInfo.jpeg')
    await message.answer_photo(photo=photo, caption='<b>Данный сервис позволяет быть в курсе актуальных цен на криптовалюты, получать подробную статистику о рынке, получать прогнозы продаж и использовать удобный калькулятор для расчета криптовалюты - все это доступно прямо в Telegram. Благодаря этому сервису вы сможете быть в курсе последних изменений на рынке и принимать осознанные решения в области криптовалютных инвестиций.</b>', parse_mode='html')
    
@router.message(F.text == '👑 Получить Vip')
async def get_vip(message: Message):
    await message.answer('ТЫ ВИП!')
       
    
 
    
def get_messageStats():
    r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,BNB,SOL&tsyms=USD')
    json_data = r.json()

    for currency in cryptocurrencies:
        price = json_data["RAW"][currency]["USD"]["PRICE"]
        prices[currency] = round(price, 2)
        
    for currency in cryptocurrencies:
        change24h = json_data["RAW"][currency]["USD"]["CHANGEPCT24HOUR"]
        changes24h[currency] = round(change24h, 2)
        
    messageStats_text = f"🏦<b>CryptoStats</b>\n\n<b>BTC:=</b><i>{prices['BTC']}$</i>, <b>24h:</b> <i>{changes24h['BTC']}%</i>\n<b>ETH:=</b><i>{prices['ETH']}$</i>, <b>24h:</b> <i>{changes24h['ETH']}%</i>\n<b>USDT:=</b><i>{prices['USDT']}$</i>, <b>24h:</b> <i>{changes24h['USDT']}%</i>\n<b>BNB:=</b><i>{prices['BNB']}$</i>, <b>24h:</b> <i>{changes24h['BNB']}%</i>\n<b>SOL:=</b><i>{prices['SOL']}$</i>, <b>24h:</b> <i>{changes24h['SOL']}%</i>"
    return messageStats_text

def get_messageStatsFull(data):
    nameCrypto = data['nameCrypto']
    
    r = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={nameCrypto}&tsyms=USD')
    json_data = r.json()

    fromsymbol = json_data["RAW"][nameCrypto]["USD"]["FROMSYMBOL"]
    market = json_data["RAW"][nameCrypto]["USD"]["MARKET"]
    price = json_data["RAW"][nameCrypto]["USD"]["PRICE"]
    change24h = json_data["RAW"][nameCrypto]["USD"]["CHANGEPCT24HOUR"]
    
    messageStatsFull_text = f'<b>График за 7 дней</b>\n\n<b>Название: </b>{fromsymbol}\n<b>Маркет: </b>{market}\n<b>Цена: </b>{round(price, 2)}$\n<b>24ч: </b>{change24h}'
    return messageStatsFull_text