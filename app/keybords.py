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

def statsFullIn(lang):
    statsFullIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('✏️ Повторить', lang), callback_data='getStatsFull')],
                                                        [InlineKeyboardButton(text=_('👈 Назад', lang), callback_data='backStatsFull')]])
    return statsFullIn


languagesIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🇷🇺 Русский', callback_data='lang_ru')],
                                                [InlineKeyboardButton(text='🇺🇸 English', callback_data='lang_eu')]])

def settingsIn(lang):
    settingsIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('😛 Язык', lang), callback_data='setLang')],
                                                [InlineKeyboardButton(text=_('👈 Назад', lang), callback_data='backProfil')]])
    return settingsIn

def backProfilIn(lang):
    backProfilIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('👈 Назад', lang), callback_data='backProfil')]])
    return backProfilIn

def backStatsIn(lang):
    backStatsIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('👈 Назад', lang), callback_data='backStatsFull')]])
    return backStatsIn

def calculatorIn(lang):
    calculatorIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('✏️ Повторить', lang), callback_data='calculator')],
                                                        [InlineKeyboardButton(text=_('👈 Назад', lang), callback_data='backStatsFull')]])
    return calculatorIn

def premiumIn(lang):
    premiumIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('📉 Графики', lang), callback_data='graphic'),
                                                InlineKeyboardButton(text=_('📰 Новости', lang), url= 'https://t.me/topslivs')],
                                                [InlineKeyboardButton(text=_('📘 Обучающие материалы', lang),url='https://t.me/FAQcrypta')]])
    return premiumIn                             
   
def premiumBuyIn(lang):                                       
    premiumBuyIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('👑 Приобрести премиум', lang), callback_data='buyPremium')]])
    return premiumBuyIn

def graphic(lang):
    graphic = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('📈 График(24)', lang), callback_data='graphic24')],
                                                    [InlineKeyboardButton(text=_('📉 График(7)', lang), callback_data='graphic7')],
                                                    [InlineKeyboardButton(text=_('👈 Назад', lang), callback_data='backPremium')]])
    return graphic

def graphic7In(lang):
    graphic7In = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('✏️ Повторить', lang), callback_data='graphic7')],
                                                    [InlineKeyboardButton(text=_('👈 Назад', lang), callback_data='graphic')]])
    return graphic7In

def graphic24In(lang):
    graphic24In = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('✏️ Повторить', lang), callback_data='graphic24')],
                                                    [InlineKeyboardButton(text=_('👈 Назад', lang), callback_data='graphic')]])
    return graphic24In


cryptoRp = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='BTC'),KeyboardButton(text='ETH')],
    [KeyboardButton(text='USDT'),KeyboardButton(text='BNB')]
], resize_keyboard=True, input_field_placeholder='Выберите криптовалюту')

def settingsCmdIn(lang):
    settingsCmdIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('😛 Язык', lang), callback_data='setLang')]])
    return settingsCmdIn


def payIn(PRICE, payment_url, payment_id, lang):
    payIn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_('Оплатить {}р'.format(PRICE), lang), url=payment_url),
                                                           InlineKeyboardButton(text=_('Проверить оплату', lang),callback_data=f'check_{payment_id}')],
                                                          [InlineKeyboardButton(text=_('Назад', lang),callback_data='backProfil')]])
    
    return payIn