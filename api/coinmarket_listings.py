import json
import requests

listing_url = 'https://api.coinmarketcap.com/v2/listings/&limit=10'

request = requests.get(listing_url)
results = request.json()

print(json.dumps(results,sort_keys=True,indent=4))

# res = results['data']

# for currency in res:
# 	print(str(currency['id'])+":"+currency['name']+":("+currency['symbol']+")")