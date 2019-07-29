import json
import requests

from Accounts import access_key

year = 2019
month = 7
date = 29

month = "{:02d}".format(month)
date = "{:02d}".format(date)

target_currencies = ['USD', 'KRW']
currencies = ''
for curr in target_currencies:
    currencies += curr + ','
currencies = currencies[:-1]


query = "http://data.fixer.io/api/{}-{}-{}?access_key={}&symbols={}&format=1".\
    format(year, month, date, access_key, currencies)
request = json.loads(requests.get(query).text)
usd = request['rates']['USD']
krw = request['rates']['KRW']

usd_over_krw = usd/krw
krw_over_usd = krw/usd

if __name__ == "__main__":
    pass
