import json
import requests

ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'

start=str(1)
limit=str(10)
currency='USD'
sort='rank'

currency = input('Enter your currency: ')
sort = input('Sort based on?: ')


ticker_url += '&sort='+sort+'&start='+start+'&limit='+limit+'&sort='+sort+'&convert='+currency

request = requests.get(ticker_url)
results = request.json()

print(json.dumps(results,sort_keys=True,indent=4))

