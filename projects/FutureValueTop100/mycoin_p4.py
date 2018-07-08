import json
import requests
import math

global_url = 'https://api.coinmarketcap.com/v2/global/'
ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array/&limit=2'


request = requests.get(global_url)
results = request.json()

# print(json.dumps(results,sort_keys=True,indent=4))

data = results['data']

total_market_cap = float(data['quotes']['USD']['total_market_cap'])

request = requests.get(ticker_url)
results = request.json()

#print(json.dumps(results,sort_keys=True,indent=4))

data = results['data']

for currency in data:
	name = currency['name']
	ticker = currency['symbol']
	percent_market_cap = round(float(currency['quotes']['USD']['market_cap'])/total_market_cap,2)
	print(round(percent_market_cap*100,2))


print()