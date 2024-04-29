import pycoingecko
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from time import sleep

crypto_list = {'bitcoin': 'BTC', 'ethereum': 'ETH', 'solana': 'SOL', 'usd-coin': 'USDC', 'hedera-hashgraph': 'HBAR', 'first-digital-usd': 'FDUSD', 'pepe': 'PEPE', 'binancecoin': 'BNB', 'dogecoin': 'DOGE', 'ripple': 'XRP'}

# Initialize CoinGecko API client
coinGecko = pycoingecko.CoinGeckoAPI()

def gr24():
    while True:
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
            plt.title(symbol.capitalize())  # Set the title to the capitalized symbol

            # Save the image in the 'Graphic_Image24' folder with the symbol as the filename
            plt.savefig(f'Images/Graphic_Image24/{image_name}.png')
            plt.close()
            sleep(10)
        print('Графики 24 часа готовы')            
        sleep(30 * 60) 
        