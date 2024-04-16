from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keybords as kb

import requests 

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("@cryptostats58_bot: Будьте в курсе цен, получайте статистику, прогнозы продаж и калькулятор крипты прямо в Telegram.", reply_markup=kb.mainRp)
    
    
@router.message(F.text == 'Статистика Binance')
async def get_stats(message: Message):
    
    r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,BNB,SOL&tsyms=USD')
    json_data = r.json()

    priceBTC = round(json_data["RAW"]["BTC"]["USD"]["PRICE"], 2)
    priceETH = round(json_data["RAW"]["ETH"]["USD"]["PRICE"], 2)
    priceUSDT = round(json_data["RAW"]["USDT"]["USD"]["PRICE"], 2)
    priceBNB = round(json_data["RAW"]["BNB"]["USD"]["PRICE"], 2)
    priceSOL = round(json_data["RAW"]["SOL"]["USD"]["PRICE"], 2)
    
    changePct24HourBTC = round(json_data["RAW"]["BTC"]["USD"]["CHANGEPCT24HOUR"], 2)
    changePct24HourETH = round(json_data["RAW"]["ETH"]["USD"]["CHANGEPCT24HOUR"], 2)
    changePct24HourUSDT = round(json_data["RAW"]["USDT"]["USD"]["CHANGEPCT24HOUR"], 2)
    changePct24HourBNB = round(json_data["RAW"]["BNB"]["USD"]["CHANGEPCT24HOUR"], 2)
    changePct24HourSOL = round(json_data["RAW"]["SOL"]["USD"]["CHANGEPCT24HOUR"], 2)

    
    await message.answer(f"🏦<b>CryptoStats</b>\n\n<b>BTC:=</b><i>{priceBTC}$</i>, <b>24h:</b> <i>{changePct24HourBTC}%</i>\n<b>ETH:=</b> <i>{priceETH}$</i>, <b>24h:</b> <i>{changePct24HourETH}%</i>\n<b>USDT:=</b> <i>{priceUSDT}$</i>, <b>24h:</b> <i>{changePct24HourUSDT}%</i>\n<b>BNB:=</b> <i>{priceBNB}$</i>, <b>24h:</b> <i>{changePct24HourBNB}%</i>\n<b>SOL:=</b> <i>{priceSOL}$</i>, <b>24h:</b> <i>{changePct24HourSOL}%</i>",reply_markup=kb.mainIn, parse_mode="html")
    
@router.callback_query(F.data == 'updateStats')
async def updateStats(callback: CallbackQuery):
    pass
    
    