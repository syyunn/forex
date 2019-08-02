# Data Source
# https://fxtop.com/kr/historates.php?A=1&C1=USD&C2=KRW&DD1=01&MM1=01&YYYY1=1997&B=1&P=&I=1&DD2=01&MM2=12&YYYY2=1997&btnOK=%EA%B2%80%EC%83%89%ED%95%98%EA%B8%B0
import numpy as np
import pandas as pd
import utils

year = "1998"
f = open("raw/{}.txt".format(year), "r")
lines = f.readlines()

dates =[]
rates = []

for line in lines:
    # date
    date, rate = line.split(' ')
    date_components = date.split('/')
    year = date_components[0]
    month = date_components[1]
    day = date_components[2]
    date = year + '-' + month + '-' + day

    dates.append(date)

    # rate
    rate = float(rate.split('\n')[0])
    rates.append(rate)

dates = np.array(dates, dtype='datetime64[D]')[::-1]
rates = np.array(rates, dtype='float32')[::-1]

data = {'Date': dates,
        'KRW/USD': rates}

df = pd.DataFrame(data)
utils.pickle_object(df, "data/KRW_USD_{}.pkl".format(year))

# df = utils.load_pickle("data/KRW_USD_1997.pkl")
utils.standard_plot(df)

if __name__ == "__main__":
    pass
