import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from time import sleep

crypto_list = ['BTC', 'ETH', 'SOL', 'USDC', 'HBAR', 'FDUSD', 'PEPE', 'BNB', 'DOGE', 'XRP']

def get_historical_data(symbol):
    url = 'https://min-api.cryptocompare.com/data/v2/histoday'

    params = {
        'fsym': symbol,
        'tsym': 'USD',
        'limit': 7,  # Запрашиваем данные за последние 7 дней
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'Success':
            prices = {}
            for item in data['Data']['Data']:
                # Преобразуем временную метку в удобный формат времени
                timestamp = item['time']
                time_str = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
                prices[time_str] = item['close']  # Добавляем цену в словарь с ключом времени
            return prices
        else:
            print("Ошибка:", data['Message'])
    else:
        print("Ошибка при запросе:", response.status_code)

def gr7():
    while True:
        for symbol in crypto_list:
            # Получаем исторические данные за последние 7 дней
            prices = get_historical_data(symbol)
            if prices:
                dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in prices.keys()]
                prices = list(prices.values())

                # Plot the data
                fig, ax = plt.subplots()
                ax.plot(dates, prices)
                ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Set the interval to 1 day
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))  # Format the date to show month and day
                plt.xlabel('Date')
                plt.ylabel('Price (USD)')
                plt.xticks(rotation=45)
                plt.title(symbol)  # Set the title

                # Save the image in the 'Images/Graphic_Image7' folder with the symbol as the filename
                plt.savefig(f'Images/Graphic_Image7/{symbol}.png')
                plt.close()
            sleep(1)
        print('Графики 7 дней готовы')
        sleep((6 * 60) * 60)

