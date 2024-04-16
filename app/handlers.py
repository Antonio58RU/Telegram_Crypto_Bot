from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keybords as kb

import requests 

cryptocurrencies = ["BTC", "ETH", "USDT", "BNB", "SOL"]
prices = {}
changes24h = {}

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("@cryptostats58_bot: Будьте в курсе цен, получайте статистику, прогнозы продаж и калькулятор крипты прямо в Telegram.", reply_markup=kb.mainRp)
    
    
@router.message(F.text == 'Статистика Binance')
async def get_stats(message: Message):
    await message.answer(get_messageStats(), reply_markup=kb.mainIn, parse_mode="html")
    
@router.callback_query(F.data == 'updateStats')
async def update_stats(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(get_messageStats(), reply_markup=kb.mainIn, parse_mode="html")
    
def get_messageStats():
    r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,BNB,SOL&tsyms=USD')
    json_data = r.json()

    for currency in cryptocurrencies:
        price = json_data["RAW"][currency]["USD"]["PRICE"]
        prices[currency] = round(price, 2)
        
    for currency in cryptocurrencies:
        change24h = json_data["RAW"][currency]["USD"]["CHANGEPCT24HOUR"]
        changes24h[currency] = round(change24h, 2)
        
    messageStats_text = f"🏦<b>CryptoStats</b>\n\n<b>BTC:=</b><i>{prices['BTC']}$</i>, <b>24h:</b> <i>{changes24h['BTC']}%</i>\n<b>ETH:=</b> <i>{prices['ETH']}$</i>, <b>24h:</b> <i>{changes24h['ETH']}%</i>\n<b>USDT:=</b> <i>{prices['USDT']}$</i>, <b>24h:</b> <i>{changes24h['USDT']}%</i>\n<b>BNB:=</b> <i>{prices['BNB']}$</i>, <b>24h:</b> <i>{changes24h['BNB']}%</i>\n<b>SOL:=</b> <i>{prices['SOL']}$</i>, <b>24h:</b> <i>{changes24h['SOL']}%</i>"
    return messageStats_text