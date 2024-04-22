from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

mainRp = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🏦 Статистика Binance'),KeyboardButton(text='👑 Премиум функционал')],
    [KeyboardButton(text='📕 О сервисе'),KeyboardButton(text='💼 Профиль')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')

mainIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⏳ Обновить', callback_data='updateStats')],
                                               [InlineKeyboardButton(text='📈 Полная информация', callback_data='getStatsFull'),
                                                InlineKeyboardButton(text='⌨️ Калькулятор крипты', callback_data='calculator')]])

profileIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='👑 Приобрести премиум', callback_data='buyPremium')],
                                                [InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings')],
                                                [InlineKeyboardButton(text='📌 Помощь', callback_data='help')]])

statsFullIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✏️ Повторить', callback_data='getStatsFull')],
                                                    [InlineKeyboardButton(text='👈 Назад', callback_data='backStatsFull')]])

languagesIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🇷🇺 Русский', callback_data='setRussia')],
                                                [InlineKeyboardButton(text='🇺🇸 English', callback_data='setEnglish')]])

settingsIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='😛 Язык', callback_data='setLang')],
                                                [InlineKeyboardButton(text='👈 Назад', callback_data='backProfil')]])

backProfilIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='👈 Назад', callback_data='backProfil')]])

calculatorIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✏️ Повторить', callback_data='calculator')],
                                                     [InlineKeyboardButton(text='👈 Назад', callback_data='backStatsFull')]])

premiumIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='📉 График(24)', callback_data='graphic24'),
                                                InlineKeyboardButton(text='📰 Новости', url= 'https://t.me/topslivs')],
                                                [InlineKeyboardButton(text='📘 Обучающие материалы',url='https://t.me/FAQcrypta')]])
                                         
premiumBuyIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='👑 Приобрести премиум', callback_data='buyPremium')]])

graphic24In = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✏️ Повторить', callback_data='graphic24')],
                                                    [InlineKeyboardButton(text='👈 Назад', callback_data='backPremium')]])

cryptoRp = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='BTC'),KeyboardButton(text='ETH')],
    [KeyboardButton(text='USDT'),KeyboardButton(text='BNB')]
], resize_keyboard=True, input_field_placeholder='Выберите криптовалюту')


settingsCmdIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='😛 Язык', callback_data='setLang')]])