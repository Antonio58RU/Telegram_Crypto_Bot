import pycoingecko
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from time import sleep

crypto_list = {'bitcoin': 'BTC', 'ethereum': 'ETH', 'solana': 'SOL', 'usd-coin': 'USDC', 'hedera-hashgraph': 'HBAR', 'first-digital-usd': 'FDUSD', 'pepe': 'PEPE', 'binancecoin': 'BNB', 'dogecoin': 'DOGE', 'ripple': 'XRP'}

# Initialize CoinGecko API client
coinGecko = pycoingecko.CoinGeckoAPI()

# Loop over each cryptocurrency in the list
for symbol, image_name in crypto_list.items():
    # Get historical price data for the cryptocurrency for the last 24 hours
    crypto_data = coinGecko.get_coin_market_chart_by_id(symbol, 'usd', '1d')

    # Extract the dates and prices from the data
    dates = [data[0] for data in crypto_data['prices']]

    # Convert unix timestamp to datetime
    dates = [
        datetime.datetime.fromtimestamp(date/1000)
        for date in dates
    ]

    prices = [data[1] for data in crypto_data['prices']]

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(dates, prices)
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)

    # Save the image in the 'Graphic_Image24' folder with the symbol as the filename
    plt.savefig(f'Graphic_Image24/{image_name}.png')
    plt.clf()
    sleep(5)
