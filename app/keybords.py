from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

mainRp = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Статистика Binance'),KeyboardButton(text='Профиль')],
    [KeyboardButton(text='О сервисе'),KeyboardButton(text='Получить Vip')]
], resize_keyboard=True)

mainIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Обновить', callback_data='updateStats'),
                                               InlineKeyboardButton(text='Калькулятор крипты', callback_data='calculator')],
                                                [InlineKeyboardButton(text='График(24)', callback_data='graphic'),
                                                InlineKeyboardButton(text='Продажа', callback_data='sell')]])