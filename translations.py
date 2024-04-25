

translations = {
    '<b>Логин:</b> {}\n<b>Статус:</b> {}\n<b>Зарегистрирован:</b> {}': '<b>Login:</b> {}\n<b>Status:</b> {}\n<b>Registered:</b> {}',
    '🏦 Статистика Binance': '🏦 Statistics Binance'

}

def _(text, lang='ru'):
    if lang == 'ru':
        return text
    else:
        return translations[text]
       