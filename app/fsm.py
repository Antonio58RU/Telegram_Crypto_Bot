from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keybords as kb
import database.requests as rq

from translations import _
import aiohttp

from translations import _

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
    lang = await rq.get_localization(callback.from_user.id)
    await callback.message.answer(_('Введите название криптовалюты.', lang), parse_mode='html')
    
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
    lang = await rq.get_localization(callback.from_user.id)
    await callback.message.answer(_('<b>Введите название криптовалюты и её количество\nчерез символ "-"</b>\nНапример - "BNB-3.54".', lang), parse_mode='html')
    
@router.message(CalculatorSt.name_and_amount)
async def get_nameCrypto_two(message: Message, state: FSMContext):
    await state.update_data(name_and_amount = message.text)
    data = await state.get_data()
    lang = await rq.get_localization(message.from_user.id)
    try:
        crypto_name, crypto_value = data['name_and_amount'].split('-')
        url = f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={crypto_name}&tsyms=USD'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                json_data = await response.json()
        price = json_data["RAW"][crypto_name]["USD"]["PRICE"]
        crypto_value = float(crypto_value)
    except:  
         await message.answer(text=_('Некорректные данные, повторите ввод!', lang)) 
    
        
    result = round(crypto_value * float(price), 5)
    await message.answer(_('⌨️ <b>Калькулятор</b>\n\nЦена {}: {} = {}$', lang).format(crypto_name, crypto_value, result), parse_mode='html', reply_markup=kb.calculatorIn(lang))
    await state.clear()

@router.callback_query(F.data == 'graphic')
async def graphic24(callback: CallbackQuery):
    await callback.answer('')
    lang = await rq.get_localization(callback.from_user.id)
    await callback.message.answer(_('<b>Выберите график.</b>', lang), reply_markup=kb.graphic(lang) ,parse_mode='html')


@router.callback_query(F.data == 'graphic24')
async def graphic24(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Graphic24St.nameCrypto)
    lang = await rq.get_localization(callback.from_user.id)
    await callback.message.answer(_('Введите название криптовалюты.', lang), parse_mode='html')
    
@router.message(Graphic24St.nameCrypto)
async def graphic24_two(message: Message, state: FSMContext):
    await state.update_data(nameCrypto = message.text)
    data = await state.get_data()
    crypto_name = data['nameCrypto']
    photo = FSInputFile(f'Images/Graphic_Image24/{crypto_name}.png')
    lang = await rq.get_localization(message.from_user.id)
    try:
        await message.answer_photo(photo=photo, caption=_('<b>График за 24 часа</b>', lang), reply_markup=kb.graphic24In(lang), parse_mode='html')
    except:
        await message.answer(text=_('Некорректные данные, повторите ввод!', lang)) 
        return
    await state.clear()
    
@router.callback_query(F.data == 'graphic7')
async def graphic7(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Graphic7St.nameCrypto)
    lang = await rq.get_localization(callback.from_user.id)
    await callback.message.answer(_('Введите название криптовалюты.', lang), parse_mode='html')
    
@router.message(Graphic7St.nameCrypto)
async def graphic7_two(message: Message, state: FSMContext):
    await state.update_data(nameCrypto = message.text)
    data = await state.get_data()
    crypto_name = data['nameCrypto']
    photo = FSInputFile(f'Images/Graphic_Image7/{crypto_name}.png')
    lang = await rq.get_localization(message.from_user.id)   
    try:
        await message.answer_photo(photo=photo, caption=_('<b>График за 7 дней</b>', lang), reply_markup=kb.graphic7In(lang), parse_mode='html')
    except:
        await message.answer(text=_('Некорректные данные, повторите ввод!', lang)) 
        return
    await state.clear()

async def get_messageStatsFull(crypto_name, message: Message):
    
    
    url = f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={crypto_name}&tsyms=USD'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_data = await response.json()
            
    lang = await rq.get_localization(message.from_user.id)
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
        toptiervolume24hourto = json_data["RAW"][crypto_name]["USD"]["TOPTIERVOLUME24HOURTO"]
    except:
        await message.answer(_('Некорректные данные, повторите ввод!', lang))

    messageStatsFull_text = _('<b>Изображение криптовалюты:</b>\n\n<b>Название: </b>{}\n<b>Маркет: </b>{}\n<b>Цена: </b>{}$\n<b>Обьём торгов за 24ч: </b>{}$\n<b>Изменение за 1ч: </b>{}%\n<b>Изменение за 24ч: </b>{}%\n<b>Максимальная цена за 24ч: </b>{}$\n<b>Минимальная цена за 24ч: </b>{}$', lang).format(fromsymbol, market, price, toptiervolume24hourto, changeday, change24h, highday, lowday)
    
    
    await message.answer_photo(photo=imageUrl, caption= messageStatsFull_text, reply_markup=kb.statsFullIn(lang), parse_mode='html')