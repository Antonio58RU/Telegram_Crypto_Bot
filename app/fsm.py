from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keybords as kb
import database.requests as rq

from translations import _
import requests 

from translations import _, get_lang

router = Router()

class StatsFullSt(StatesGroup):
    nameCrypto = State()

class Graphic24St(StatesGroup):
    nameCrypto = State()

class Graphic7St(StatesGroup):
    nameCrypto = State()
        
class CalculatorSt(StatesGroup):
    name_and_amount = State()
        
@router.callback_query(F.data == 'getStatsFull')
async def get_statsFull(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(StatsFullSt.nameCrypto)
    await callback.message.answer(_('Введите название криптовалюты.', await get_lang(callback.from_user.id)), parse_mode='html')
    
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
    await callback.message.answer(_('<b>Введите название криптовалюты и её количество\nчерез символ "-"</b>\nНапример - "BNB-3.54".', await get_lang(callback.from_user.id)), parse_mode='html')
    
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
         await message.answer(text=_('Некорректные данные, повторите ввод!', await get_lang(message.from_user.id))) 
    
        
    result = round(crypto_value * float(price), 5)
    await message.answer(_('⌨️ <b>Калькулятор</b>\n\nЦена {}: {} = {}$', await get_lang(message.from_user.id)).format(crypto_name, crypto_value, result), parse_mode='html', reply_markup=kb.calculatorIn(await get_lang(message.from_user.id)))
    await state.clear()

@router.callback_query(F.data == 'graphic')
async def graphic24(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Graphic24St.nameCrypto)
    await callback.message.answer(_('<b>Выберите график.</b>', await get_lang(callback.from_user.id)), reply_markup=kb.graphic(await get_lang(callback.from_user.id)) ,parse_mode='html')


@router.callback_query(F.data == 'graphic24')
async def graphic24(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Graphic24St.nameCrypto)
    await callback.message.answer(_('Введите название криптовалюты.', await get_lang(callback.from_user.id)), parse_mode='html')
    
@router.message(Graphic24St.nameCrypto)
async def graphic24_two(message: Message, state: FSMContext):
    await state.update_data(nameCrypto = message.text)
    data = await state.get_data()
    crypto_name = data['nameCrypto']
    photo = FSInputFile(f'Images/Graphic_Image24/{crypto_name}.png')
  
    try:
        await message.answer_photo(photo=photo, caption=_('<b>График за 24 часа</b>', await get_lang(message.from_user.id)), reply_markup=kb.graphic24In(await get_lang(message.from_user.id)), parse_mode='html')
    except:
        await message.answer(text=_('Некорректные данные, повторите ввод!', await get_lang(message.from_user.id))) 
        return
    await state.clear()
    
@router.callback_query(F.data == 'graphic7')
async def graphic7(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Graphic7St.nameCrypto)
    await callback.message.answer(_('Введите название криптовалюты.', await get_lang(callback.from_user.id)), parse_mode='html')
    
@router.message(Graphic7St.nameCrypto)
async def graphic7_two(message: Message, state: FSMContext):
    await state.update_data(nameCrypto = message.text)
    data = await state.get_data()
    crypto_name = data['nameCrypto']
    photo = FSInputFile(f'Images/Graphic_Image7/{crypto_name}.png')
       
    try:
        await message.answer_photo(photo=photo, caption=_('<b>График за 7 дней</b>', await get_lang(message.from_user.id)), reply_markup=kb.graphic7In(await get_lang(message.from_user.id)), parse_mode='html')
    except:
        await message.answer(text=_('Некорректные данные, повторите ввод!', await get_lang(message.from_user.id))) 
        return
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
        await message.answer(_('Некорректные данные, повторите ввод!', await get_lang(message.from_user.id)))

    messageStatsFull_text = _('<b>Изображение криптовалюты:</b>\n\n<b>Название: </b>{}\n<b>Маркет: </b>{}\n<b>Цена: </b>{}$\n<b>Изменение за 1ч: </b>{}%\n<b>Изменение за 24ч: </b>{}%\n<b>Максимальная цена за 24ч: </b>{}$\n<b>Минимальная цена за 24ч: </b>{}$', await get_lang(message.from_user.id)).format(fromsymbol, market, price, changeday, change24h, highday, lowday)
    
    
    await message.answer_photo(photo=imageUrl, caption= messageStatsFull_text, reply_markup=kb.statsFullIn(await get_lang(message.from_user.id)), parse_mode='html')