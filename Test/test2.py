import ccxt
import pandas as pd
import matplotlib.pyplot as plt

exchange = ccxt.binance()
symbol = 'SOL/USDT'
timeframe = '1h'

# Получение данных OHLCV за последние 24 часа
ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=24)

# Создание DataFrame из полученных данных
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Форматирование временной метки для отображения только часа
df['timestamp'] = df['timestamp'].dt.strftime('%H')

# Построение графика цены закрытия
plt.plot(df['timestamp'], df['close'])

# Аннотация изменений цены
for i in range(1, len(df)):
    if df['close'][i] != df['close'][i-1]:
        plt.annotate(f'{df["close"][i]:.2f}', (df['timestamp'][i], df['close'][i]), xytext=(5, 5), textcoords='offset points')


plt.show()
