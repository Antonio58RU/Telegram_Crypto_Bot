import pycoingecko
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

crypto_list = ['bitcoin', 'ethereum', 'solana', 'usd-coin', 'hedera-hashgraph', 'first-digital-usd', 'pepe', 'binancecoin', 'xrp']

# Initialize CoinGecko API client
coinGecko = pycoingecko.CoinGeckoAPI()

# Get historical price data for Bitcoin for the last 24 hours
btc_data = coinGecko.get_coin_market_chart_by_id('hedera-hashgraph', 'usd', '1d')

# Extract the dates and prices from the data
dates = [data[0] for data in btc_data['prices']]

# Convert unix timestamp to datetime
dates = [
    datetime.datetime.fromtimestamp(date/1000)
    for date in dates
]

prices = [data[1] for data in btc_data['prices']]

# Plot the data
fig, ax = plt.subplots()
ax.plot(dates, prices)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)

plt.savefig(f'Graphic_Image24/{symbol}.png')
plt.clf()
