import requests
from datetime import datetime

# Функция для получения исторических данных с интервалом в 10 минут
def get_historical_data():
    url = 'https://min-api.cryptocompare.com/data/v2/histominute'
    fsym = 'BTC'
    tsym = 'USD'
    limit = 144  # За последние 24 часа (24 часа * 6 10-минутных интервалов в часе)

    params = {
        'fsym': fsym,
        'tsym': tsym,
        'limit': limit,
        'aggregate': 10  # Используем параметр aggregate для получения данных с интервалом в 10 минут
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'Success':
            prices = {}
            for item in data['Data']['Data']:
                # Преобразуем временную метку в удобный формат времени
                timestamp = item['time']
                time_str = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                prices[time_str] = item['close']  # Добавляем цену в словарь с ключом времени
            return prices
        else:
            print("Ошибка:", data['Message'])
    else:
        print("Ошибка при запросе:", response.status_code)

# Получаем и выводим словарь цен
prices = get_historical_data()
if prices:
    print("Цены с интервалом в 10 минут за последние 24 часа:")
    for time, price in prices.items():
        print(f"{time}: {price}")
