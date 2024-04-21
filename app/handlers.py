from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import asyncio

import app.keybords as kb
import database.requests as rq


import requests 


router = Router()

class StatsFullSt(StatesGroup):
    nameCrypto = State()
    
class CalculatorSt(StatesGroup):
    name_and_amount = State()
 

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await rq.set_user(message.from_user.id)
    await message.answer('@cryptostats58_bot: Будьте в курсе цен, получайте статистику, прогнозы продаж и калькулятор крипты прямо в Telegram.', reply_markup=kb.mainRp)
    await state.clear()
     
@router.message(F.text == '🏦 Статистика Binance')
async def get_stats(message: Message):
    await message.answer(get_messageStats(), reply_markup=kb.mainIn, parse_mode='html')
    
@router.callback_query(F.data == 'updateStats')
async def update_stats(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(get_messageStats(), reply_markup=kb.mainIn, parse_mode='html')
    
@router.callback_query(F.data == 'getStatsFull')
async def get_statsFull(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(StatsFullSt.nameCrypto)
    await callback.message.answer('Введите название криптовалюты для получения её полной информации.', parse_mode='html')
    
@router.message(StatsFullSt.nameCrypto)
async def StatsFull_stats(message: Message, state: FSMContext):
    await state.update_data(nameCrypto = message.text)
    data = await state.get_data()
    await message.answer_photo(photo=f'https://images.cryptocompare.com/sparkchart/{data['nameCrypto']}/USD/latest.png?ts=1713464400', caption=get_messageStatsFull(data), reply_markup=kb.statsFullIn, parse_mode='html')
    await state.clear()
 
@router.callback_query(F.data == 'calculator')
async def get_nameCrypto(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(CalculatorSt.name_and_amount)
    await callback.message.answer('<b>Введите название криптовалюты и её количество\nчерез символ "-"</b>\nНапример - "BNB-3.54".', parse_mode='html')
    
@router.message(CalculatorSt.name_and_amount)
async def get_nameCrypto_two(message: Message, state: FSMContext):
    await state.update_data(name_and_amount = message.text)
    data = await state.get_data()
    crypto_name, crypto_value = data['name_and_amount'].split('-')
    
    r = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={crypto_name}&tsyms=USD')
    json_data = r.json()
    try:
        price = json_data["RAW"][crypto_name]["USD"]["PRICE"]
    except KeyError:  
        await message.answer(text='Некорректные данные1') 
        #asyncio.run(get_nameCrypto)
    
    try:
        crypto_value = float(crypto_value)
    except ValueError:  
        await message.answer(text='Некорректные данные2') 
        
    
    await message.answer(f'⌨️ <b>Калькулятор</b>\n\nЦена {crypto_name}: {crypto_value} = {round(crypto_value * float(price),5)}$', parse_mode='html', reply_markup=kb.calculatorIn)
    await state.clear()
        
@router.callback_query(F.data == 'backStatsFull')
async def back_statsFull(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(get_messageStats(), reply_markup=kb.mainIn, parse_mode='html')







@router.message(F.text == '💼 Профиль')
async def get_statsProfil(message: Message):
    user = await rq.get_user(message.from_user.id)
    await message.answer(f'<b>Логин:</b> {message.from_user.full_name}\n<b>Статус:</b> {premiumStatus(user.premium)}\n<b>Зарегистрирован:</b> {user.registr_date}', reply_markup=kb.profileIn, parse_mode='html')

@router.callback_query(F.data == 'settings')
async def settings(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='⚙️ <b>Настройки</b>', reply_markup=kb.settingsIn, parse_mode='html')
    
@router.callback_query(F.data == 'setLang')
async def settings(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='<b>Выберите язык</b>', reply_markup=kb.languagesIn, parse_mode='html')
 
@router.callback_query(F.data == 'backProfil')
async def back_Profil(callback: CallbackQuery):
    await callback.answer('')
    user1 = await rq.get_user(callback.from_user.id)
    await callback.message.edit_text(f'<b>Логин:</b> {callback.from_user.full_name}\n<b>Статус:</b> {premiumStatus(user1.premium)}\n<b>Зарегистрирован:</b> {user1.registr_date}', reply_markup=kb.profileIn, parse_mode='html')

     
     
     
@router.callback_query(F.data == 'help')
async def support(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='/start - Запуск бота\n/setting - Настройки\n/help Помощь\n\nhttps://t.me/AntonBog123', reply_markup=kb.backProfilIn)
  
  
  
  
       
@router.message(F.text == '📕 О сервисе')
async def get_info(message: Message):
    photo = FSInputFile('Images/photoInfo.jpeg')
    await message.answer_photo(photo=photo, caption='<b>Данный сервис позволяет быть в курсе актуальных цен на криптовалюты, получать подробную статистику о рынке, получать прогнозы продаж и использовать удобный калькулятор для расчета криптовалюты - все это доступно прямо в Telegram. Благодаря этому сервису вы сможете быть в курсе последних изменений на рынке и принимать осознанные решения в области криптовалютных инвестиций.</b>', parse_mode='html')
    
    
    
    
    
    
@router.message(F.text == '👑 Получить Vip')
async def get_vip(message: Message):
    await rq.update_user_premium_status(message.from_user.id)
    await message.answer('Ты премиум!')
       
    
 
    
    
    
    
def get_messageStats():
    
    cryptocurrencies = ["BTC", "ETH", "USDT", "BNB", "SOL", "USDC", "STETH", "XRP", "DOGE", "TON"]
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

def premiumStatus(premium: bool):
    if(premium == False):    
        return 'Стандарт'
    return 'Premium'
