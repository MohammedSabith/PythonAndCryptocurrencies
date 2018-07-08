import os
import json
import requests
import time

convert = 'USD'

listing_url = 'https://api.coinmarketcap.com/v2/listings/?convert=' + convert

request = requests.get(listing_url)
results = request.json()

data = results['data']

listing_url_pair = {}

for currency in data:
	symbol = currency['symbol']
	ide = currency['id']
	listing_url_pair[symbol] = ide


url_end = '/?structure=array/&convert=' + convert

already_got = []

print()
print('tracking...\n')

while True:
	with open('alerts.txt') as inp:
		for line in inp:
			ticker, amount = line.split()
			ticker = ticker.upper()
			ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(listing_url_pair[ticker]) + url_end

			request = requests.get(ticker_url)
			results = request.json()

			data = results['data'][0]
			#print(json.dumps(data,sort_keys=True,indent=4))
			name = data['name']
			last_updated = data['last_updated']

			price = data['quotes'][convert]['price']

			if float(price) >= float(amount) and ticker not in already_got:
				os.system('espeak \"' + name + ' hit ' +amount+'\"')
				already_got.append(ticker)
				print('hit\n')

	print()
	time.sleep(300)





