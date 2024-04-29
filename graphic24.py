import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from time import sleep

crypto_list = ['BTC', 'ETH', 'SOL', 'USDC', 'HBAR', 'FDUSD', 'PEPE', 'BNB', 'DOGE', 'XRP']

def get_historical_data(symbol):
    url = 'https://min-api.cryptocompare.com/data/v2/histominute'
    limit = 144  # За последние 24 часа (24 часа * 6 10-минутных интервалов в часе)

    params = {
        'fsym': symbol,
        'tsym': 'USD',
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
                time_str = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                prices[time_str] = item['close']  # Добавляем цену в словарь с ключом времени
            return prices
        else:
            print("Ошибка:", data['Message'])
    else:
        print("Ошибка при запросе:", response.status_code)

def gr24():
    while True:
        for symbol in crypto_list:
            # Получаем исторические данные с интервалом в 10 минут
            prices = get_historical_data(symbol)
            if prices:
                dates = [datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in prices.keys()]
                prices = list(prices.values())

                # Plot the data
                fig, ax = plt.subplots()
                ax.plot(dates, prices)
                ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
                plt.xlabel('Date')
                plt.ylabel('Price (USD)')
                plt.xticks(rotation=45)
                plt.title(symbol)  # Установим название графика сокращенным именем криптовалюты

                # Сохраняем график
                plt.savefig(f'Images/Graphic_Image24/{symbol}.png')
                plt.close()
            sleep(1)
        print('Графики 24 часа готовы')            
        sleep(30 * 60) 
