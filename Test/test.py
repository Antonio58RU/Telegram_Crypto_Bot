import requests

r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR')
print(1)
json_data = r.json()

price = json_data["RAW"]["BTC"]["USD"]["PRICE"]
print("Цена BTC в USD:", price)