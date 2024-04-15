from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keybords as kb

import requests 

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
  
    await message.answer("Меню", reply_markup=kb.mainRp)
    
    
@router.message(F.text == 'Статистика Binance')
async def get_stats(message: Message):
    
    r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD,EUR')
    json_data = r.json()

    price = json_data["RAW"]["BTC"]["USD"]["PRICE"]
    price2 = json_data["RAW"]["ETH"]["USD"]["PRICE"]
    
    await message.answer(f"🏦CryptoStats\n\nBTC:={price}\nETH:={price2}",reply_markup=kb.mainIn)
    
 


    