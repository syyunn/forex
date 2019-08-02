![png](assets/teaser.png)

# About
`forex` is to model the successful prediction of foreign exchange rate. `forex` entails `data collection` phase where the first version of data would be mainly targeting on the `USD/KRW`.


# Data
`data/KRW_USD.pkl` includes `KRW/USD` rates from `2017-01-01` to `2019-07-29`

# Standard of TimeSeries Representation 
    dates = np.array(dates, dtype='datetime64[D]')
    rates = np.array(rates, dtype='float64')
    data = {'Date': dates,
            'KRW/USD': prices}
