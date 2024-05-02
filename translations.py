from database import requests as rq

translations = {
    '<b>CryptoStats:</b> Будьте в курсе цен, получайте статистику, графики и калькулятор крипты прямо в Telegram.': '<b>CryptoStats:</b> Stay up to date with prices, get statistics, charts and crypto calculator directly in Telegram.',
    '/start - Запуск бота\n/settings - Настройки\n/help Помощь\n\nhttps://t.me/AntonBog123': '/start - Start the bot\n/settings - Settings\n/help Help\n\nhttps://t.me/AntonBog123',
    '⚙️ <b>Настройки</b>': '⚙️ <b>Settings</b>',
    '🏦 Статистика': '🏦 Statistics',
    '👑 Премиум функционал': '👑 Premium Functionality',
    '📕 О сервисе': '📕 About the Service',
    '💼 Профиль': '💼 Profile',
    'Выберите пункт меню': 'Select menu item',
    
    '<b>Логин:</b> {}\n<b>Статус:</b> {}\n<b>Зарегистрирован:</b> {}': '<b>Login:</b> {}\n<b>Status:</b> {}\n<b>Registered:</b> {}',
    
    'Стандарт': 'Standard',
    'Премиум': 'Premium',   
    
    
    
    '⏳ Обновить': '⏳ Refresh',
    '📈 Полная информация': '📈 Full information',
    '⌨️ Калькулятор криптовалюты': '⌨️ Cryptocurrency calculator',
    '₿ Список криптовалют': '₿ List of cryptocurrencies',
    
    'Введите название криптовалюты.': 'Enter the name of the cryptocurrency.',
    '<b>Введите название криптовалюты и её количество\nчерез символ "-"</b>\nНапример - "BNB-3.54".': '<b>Enter the name of the cryptocurrency and its quantity\nseparated by the "-" symbol</b>\nFor example - "BNB-3.54".',
    '<b>График за 24 часа</b>': '<b>24 hour chart</b>',
    '<b>График за 7 дней</b>': '<b>Chart for 7 days</b>',
    '<b>Выберите график.</b>': '<b>Select schedule.</b>',
    '📈 График(24)': '📈 Chart(24)',
    '📉 График(7)': '📉 Graph(7)',
    'Некорректные данные, повторите ввод!': 'Invalid data, please re-enter!',
    '<b>Изображение криптовалюты:</b>\n\n<b>Название: </b>{}\n<b>Маркет: </b>{}\n<b>Цена: </b>{}$\n<b>Обьём торгов за 24ч: </b>{}$\n<b>Изменение за 1ч: </b>{}%\n<b>Изменение за 24ч: </b>{}%\n<b>Максимальная цена за 24ч: </b>{}$\n<b>Минимальная цена за 24ч: </b>{}$': '<b>Cryptocurrency image:</b>\n\n<b>Name: </b>{}\n<b>Market: </b>{}\n<b>Price: </b> {}$\n<b>Trading volume for 24 hours: </b>{}$\n<b>Change for 1 hour: </b>{}%\n<b>Change for 24 hours: </b>{}%\n<b>Maximum price for 24 hours: </b>{}$\n<b>Minimum price for 24 hours: </b>{}$',
    '⌨️ <b>Калькулятор</b>\n\nЦена {}: {} = {}$': '⌨️ <b>Calculator</b>\n\nPrice {}: {} = {}$',
    
    '✏️ Повторить': '✏️ Repeat',
    '👈 Назад': '👈 Back',
    
    '👑 <b>Премиум функционал</b>': '👑 <b>Premium functionality</b>',
    'Приобретите премиум доступ чтобы пользоваться данными функционалом': 'Purchase premium access to use this functionality',
    
    'Вы уже приобрели премиум статус.': 'You have already purchased premium status.',
    'Премиум куплен!': 'Premium purchased!',
    
    '📉 Графики': '📉 Charts',
    '📰 Новости': '📰 News',
    '📘 Обучающие материалы': '📘 Educational materials',
    
    
    '👑 Приобрести премиум': '👑 Purchase premium',
    '⚙️ Настройки': '⚙️ Settings',
    '📌 Помощь': '📌 Help',
    
    '<b>Выберите язык</b>': '<b>Select language</b>',
    '<b>Русский язык установлен.</b>': '<b>English language is set.</b>',
    '😛 Язык': '😛 Language',
    
    "<b>Наш сервис дает вам возможность быть в курсе актуальных цен на криптовалюты, получать подробную информацию о рынке и использовать удобный калькулятор для расчета криптовалют - все это доступно прямо в Telegram. \n\nЗдесь вы найдете следующие функции:\n \n- Просмотр статистики цен на криптовалюты.\n- Получение полной статистики по криптовалютам.\n- Использование калькулятора для расчета криптовалют.\n- Просмотр списка доступных криптовалют.\n\nПремиум-статус предоставляет доступ к дополнительным функциям:\n\n- Графики цен на криптовалюты за 7 дней и за последние 24 часа, позволяющие более детально анализировать динамику цен.\n- Приватный канал с новостями, где вы можете получать эксклюзивные новости и аналитику.\n- Приватный канал с обучающими материалами.</b>": "<b>Our service gives you the opportunity to be aware of current prices for cryptocurrencies, receive detailed information about the market and use a convenient calculator for calculating cryptocurrencies - all this is available directly in Telegram. \n\nHere you will find the following functions:\n \n - View cryptocurrency price statistics.\n- Get complete statistics on cryptocurrencies.\n- Use a calculator to calculate cryptocurrencies.\n- View a list of available cryptocurrencies.\n\nPremium status provides access to additional features:\n\n- Cryptocurrency price charts for 7 days and the last 24 hours, allowing you to analyze price dynamics in more detail.\n- Private news channel where you can receive exclusive news and analytics.\n- Private channel with educational materials.</b> ",
}

def _(text, lang='ru'):
    if lang == 'ru':
        return text
    else:
        return translations[text]

