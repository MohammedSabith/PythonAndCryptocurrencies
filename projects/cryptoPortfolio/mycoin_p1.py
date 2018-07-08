import os
import json
import requests
from prettytable import PrettyTable
from colorama import Fore,Back,Style

convert = 'USD'

listing_url = 'https://api.coinmarketcap.com/v2/listings/?convert=' + convert

request = requests.get(listing_url)
results = request.json()

#print(json.dumps(results,sort_keys=True,indent=4))

data = results['data']

listing_url_pair = {}

for currency in data:
	id = currency['id']
	symbol = currency['symbol']
	listing_url_pair[symbol] = id

#print(listing_url_pair)

total_value = 0.00

print()

table = PrettyTable(['Name','Amount','Value','Price','24h'])

with open('portfolio.txt') as inp:
	for line in inp:
		symbol, amount = line.split()
		symbol = symbol.upper()
		ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(listing_url_pair[symbol]) +'/?structure=array'
		request = requests.get(ticker_url)
		results = request.json()
		data = results['data'][0]

		name = data['name']
		price = data['quotes'][convert]['price']
		day_change = data['quotes'][convert]['percent_change_24h']
		value = float(amount) * float(price) 
		value = round(value,2)
		total_value += value
		if day_change > 0:
			day_change = Back.GREEN + str(day_change) +'%' + Style.RESET_ALL
		else:
	    	 day_change = Back.RED + str(day_change) +'%' + Style.RESET_ALL
		table.add_row([name+'('+symbol+')',
			amount,
			value,
			price,
			day_change])

print(total_value)
print(table)
