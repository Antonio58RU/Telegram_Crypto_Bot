from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keybords as kb

import requests 

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR')
    json_data = r.json()

    price = json_data["RAW"]["BTC"]["USD"]["PRICE"]
    
    await message.answer(f"Цена BTC в USD: {price}", reply_markup=kb.main)
    
@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')
    
 
@router.callback_query(F.data == 'catalog')     
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог', show_alert=True)
    await callback.message.edit_text('Колбек', reply_markup= await kb.inline_cars())
    

    