import json
import requests

from Accounts import access_key
from utils import pickle_object

target_currencies = ['USD', 'KRW']
currencies = ''
for curr in target_currencies:
    currencies += curr + ','
currencies = currencies[:-1]


years = [year for year in range(2000, 2020)]
months = [month for month in range(1, 13)]
days = [day for day in range(1, 32)]

rates = dict()
for year in years:
    for month in months:
        month = "{:02d}".format(month)
        for day in days:
            date = '{}-{}-{}'.format(year, month, day)
            day = "{:02d}".format(day)
            query = "http://data.fixer.io/api/" \
                    "{}-{}-{}?" \
                    "access_key={}&" \
                    "symbols={}&" \
                    "format=1".\
                format(year, month, day, access_key, currencies)
            request = json.loads(requests.get(query).text)

            if 'rates' not in request.keys():
                rates[date] = None
                continue

            usd = request['rates']['USD']
            krw = request['rates']['KRW']

            usd_over_krw = usd/krw
            krw_over_usd = krw/usd

            rates[date] = krw_over_usd

            print(date, ": ", krw_over_usd)

pickle_object(rates, 'KRW_USD.pkl')

if __name__ == "__main__":
    pass
