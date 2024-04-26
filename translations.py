from database import requests as rq

translations = {
    '<b>Логин:</b> {}\n<b>Статус:</b> {}\n<b>Зарегистрирован:</b> {}': '<b>Login:</b> {}\n<b>Status:</b> {}\n<b>Registered:</b> {}',
    
    '🏦 Статистика': '🏦 Statistics',
    '👑 Премиум функционал': '👑 Premium Functionality',
    '📕 О сервисе': '📕 About the Service',
    '💼 Профиль': '💼 Profile',
    'Выберите пункт меню': 'Select menu item',
    
    '⏳ Обновить': '⏳ Refresh',
    '📈 Полная информация': '📈 Full information',
    '⌨️ Калькулятор криптовалюты': '⌨️ Cryptocurrency calculator',
    '₿ Список криптовалют': '₿ List of cryptocurrencies',
    
    '👑 Приобрести премиум': '👑 Purchase premium',
    '⚙️ Настройки': '⚙️ Settings',
    '📌 Помощь': '📌 Help'
}

def _(text, lang='ru'):
    if lang == 'ru':
        return text
    else:
        return translations[text]

async def get_lang(tg_id):
    return await rq.get_localization(tg_id)       