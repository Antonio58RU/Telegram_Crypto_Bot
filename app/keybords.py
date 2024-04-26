from translations import _

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

def mainRp(lang):
    mainRp = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_('🏦 Статистика', lang)), KeyboardButton(text=_('👑 Премиум функционал', lang))],
        [KeyboardButton(text=_('📕 О сервисе', lang)),KeyboardButton(text=_('💼 Профиль', lang))]], resize_keyboard=True, input_field_placeholder=_('Выберите пункт меню', lang))
    return mainRp

def mainIn(lang):
    mainIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('⏳ Обновить', lang), callback_data='updateStats'),
                                                InlineKeyboardButton(text=_('📈 Полная информация', lang), callback_data='getStatsFull')],
                                                [InlineKeyboardButton(text=_('⌨️ Калькулятор криптовалюты', lang), callback_data='calculator'),
                                                InlineKeyboardButton(text=_('₿ Список криптовалют', lang), callback_data='listcrypto')]])
    return mainIn

def profileIn(lang):
    profileIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('👑 Приобрести премиум', lang), callback_data='buyPremium')],
                                                [InlineKeyboardButton(text=_('⚙️ Настройки', lang), callback_data='settings')],
                                                [InlineKeyboardButton(text=_('📌 Помощь', lang), callback_data='help')]])
    return profileIn

statsFullIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✏️ Повторить', callback_data='getStatsFull')],
                                                    [InlineKeyboardButton(text='👈 Назад', callback_data='backStatsFull')]])

languagesIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🇷🇺 Русский', callback_data='lang_ru')],
                                                [InlineKeyboardButton(text='🇺🇸 English', callback_data='lang_eu')]])

settingsIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='😛 Язык', callback_data='setLang')],
                                                [InlineKeyboardButton(text='👈 Назад', callback_data='backProfil')]])

backProfilIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='👈 Назад', callback_data='backProfil')]])

backStatsIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='👈 Назад', callback_data='backStatsFull')]])

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