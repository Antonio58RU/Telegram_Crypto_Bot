from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keybords as kb
import database.requests as rq

from translations import _
import requests 

router = Router()

class StatsFullSt(StatesGroup):
    nameCrypto = State()

class Graphic24St(StatesGroup):
    nameCrypto = State()
    
class CalculatorSt(StatesGroup):
    name_and_amount = State()
        
@router.callback_query(F.data == 'getStatsFull')
async def get_statsFull(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(StatsFullSt.nameCrypto)
    await callback.message.answer('Введите название криптовалюты.', parse_mode='html')
    
@router.message(StatsFullSt.nameCrypto)
async def StatsFull_stats(message: Message, state: FSMContext):
    await state.update_data(nameCrypto = message.text)
    data = await state.get_data()
    crypto_name = data['nameCrypto']
    await get_messageStatsFull(crypto_name, message)
    
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
    
    try:
        crypto_name, crypto_value = data['name_and_amount'].split('-')
        r = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={crypto_name}&tsyms=USD')
        json_data = r.json()
        price = json_data["RAW"][crypto_name]["USD"]["PRICE"]
        crypto_value = float(crypto_value)
    except:  
         await message.answer(text='Некорректные данные, повторите ввод!') 
    
        
    
    await message.answer(f'⌨️ <b>Калькулятор</b>\n\nЦена {crypto_name}: {crypto_value} = {round(crypto_value * float(price),5)}$', parse_mode='html', reply_markup=kb.calculatorIn)
    await state.clear()

@router.callback_query(F.data == 'graphic24')
async def graphic24(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Graphic24St.nameCrypto)
    await callback.message.answer('Введите название криптовалюты.', parse_mode='html')
    
@router.message(Graphic24St.nameCrypto)
async def graphic24_two(message: Message, state: FSMContext):
    await state.update_data(nameCrypto = message.text)
    data = await state.get_data()
    crypto_name = data['nameCrypto']
    try:
        photo = FSInputFile(f'Images/Graphic_Image24/{crypto_name}.png')
    except:
        pass
    
    await message.answer_photo(photo=photo, caption='<b>График за 24 часа</b>', reply_markup=kb.graphic24In, parse_mode='html')
    await state.clear()

async def get_messageStatsFull(crypto_name, message: Message):
    
    
    r = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={crypto_name}&tsyms=USD')
    json_data = r.json()

    try:
        imageUrl = json_data["RAW"][crypto_name]["USD"]["IMAGEURL"]
        imageUrl = f'https://www.cryptocompare.com/{imageUrl}'
        fromsymbol = json_data["RAW"][crypto_name]["USD"]["FROMSYMBOL"]
        market = json_data["RAW"][crypto_name]["USD"]["MARKET"]
        price = json_data["RAW"][crypto_name]["USD"]["PRICE"]
        change24h = json_data["RAW"][crypto_name]["USD"]["CHANGEPCT24HOUR"]
        highday = json_data["RAW"][crypto_name]["USD"]["HIGHDAY"]
        lowday = json_data["RAW"][crypto_name]["USD"]["LOWDAY"]
        changeday = json_data["RAW"][crypto_name]["USD"]["CHANGEPCTDAY"]
    except:
        await message.answer('Некорректные данные, повторите ввод!')

    messageStatsFull_text = f'<b>Изображение криптовалюты:</b>\n\n<b>Название: </b>{fromsymbol}\n<b>Маркет: </b>{market}\n<b>Цена: </b>{price}$\n<b>Изменение за 1ч: </b>{changeday}%\n<b>Изменение за 24ч: </b>{change24h}%\n<b>Максимальная цена за 24ч: </b>{highday}$\n<b>Минимальная цена за 24ч: </b>{lowday}$'
    
    
    await message.answer_photo(photo=imageUrl, caption= messageStatsFull_text, reply_markup=kb.statsFullIn, parse_mode='html')