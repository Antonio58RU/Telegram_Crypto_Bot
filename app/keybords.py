from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

mainRp = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🏦 Статистика Binance'),KeyboardButton(text='👑 Premium функции')],
    [KeyboardButton(text='📕 О сервисе'),KeyboardButton(text='💼 Профиль')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')

mainIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⏳ Обновить', callback_data='updateStats'),
                                               InlineKeyboardButton(text='📈 Полная информация', callback_data='getStatsFull')],
                                                [InlineKeyboardButton(text='⌨️ Калькулятор крипты', callback_data='calculator'),
                                                InlineKeyboardButton(text='📦 Продажа', callback_data='ghdfh')]])

profileIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings')],
                                                [InlineKeyboardButton(text='📌 Помощь', callback_data='help')]])

statsFullIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='👈 Назад', callback_data='backStatsFull')]])

languagesIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🇷🇺 Русский', callback_data='setRussia')],
                                                [InlineKeyboardButton(text='🇺🇸 English', callback_data='setEnglish')]])

settingsIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='😛 Язык', callback_data='setLang')],
                                                [InlineKeyboardButton(text='👈 Назад', callback_data='backProfil')]])

backProfilIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='👈 Назад', callback_data='backProfil')]])

calculatorIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✏️ Повторить', callback_data='calculator')],
                                                     [InlineKeyboardButton(text='👈 Назад', callback_data='backStatsFull')]])