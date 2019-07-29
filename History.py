import json
import requests

from Accounts import access_key
from utils import pickle_object

target_currencies = ['USD', 'KRW']
currencies = ''
for curr in target_currencies:
    currencies += curr + ','
currencies = currencies[:-1]

years = [year for year in range(2017, 2020)]
months = [month for month in range(1, 13)]
days = [day for day in range(1, 32)]

rates = []
count = 0
for year in years:
    for month in months:
        month = "{:02d}".format(month)
        for day in days:
            day = "{:02d}".format(day)
            date = '{}-{}-{}'.format(year, month, day)
            query = "http://data.fixer.io/api/" \
                    "{}-{}-{}?" \
                    "access_key={}&" \
                    "symbols={}&" \
                    "format=1".\
                format(year, month, day, access_key, currencies)

            request = json.loads(requests.get(query).text)
            count += 1
            if 'rates' not in request.keys():
                continue

            usd = request['rates']['USD']
            krw = request['rates']['KRW']

            usd_over_krw = usd/krw
            krw_over_usd = krw/usd

            item = dict()
            item[date] = krw_over_usd
            rates.append(item)

            print(date, " : ", krw_over_usd)
            if date == "2019-07-29":
                pickle_object(rates, 'KRW_USD.pkl')

if __name__ == "__main__":
    pass
