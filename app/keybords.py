from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Маркет'),KeyboardButton(text='Профиль')],
    [KeyboardButton(text='О сервисе'),KeyboardButton(text='Vip возможности')]
])

