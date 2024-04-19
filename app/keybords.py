from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

mainRp = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🏦 Статистика Binance'),KeyboardButton(text='💼 Профиль')],
    [KeyboardButton(text='📕 О сервисе'),KeyboardButton(text='👑 Получить Vip')]
], resize_keyboard=True)

mainIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⏳ Обновить', callback_data='updateStats'),
                                               InlineKeyboardButton(text='📈 Полная информация', callback_data='getStatsFull')],
                                                [InlineKeyboardButton(text='⌨️ Калькулятор крипты', callback_data='calculator'),
                                                InlineKeyboardButton(text='📦 Продажа', callback_data='sell')]])

profileIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings')],
                                                [InlineKeyboardButton(text='📌 Помощь', callback_data='support')]])

statsFullIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🔙 Назад', callback_data='backStatsFull')]])

langIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🇷🇺 Русский', callback_data='setRussia')],
                                                [InlineKeyboardButton(text='🇺🇸 English', callback_data='setEnglish')]])
