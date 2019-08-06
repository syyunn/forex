from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import autocorrelation_plot

# Data prep
import utils

df3 = utils.load_pickle("../data/KRW_USD_2019_Q1_Q2.pkl")
df4 = utils.load_pickle("../data/KRW_USD_2019_Q3.pkl")

df = utils.concat_n_dfs([df3, df4])

timesteps = df['Date']
start = timesteps[0]
series = df['KRW/USD']

# Check Auto-correlation
model = ARIMA(series, order=(5, 1, 0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

ax = autocorrelation_plot(series)
fig = ax.get_figure()
fig.savefig(fname='ARIMA_as_a_feature.png')
fig.show()

if __name__ == "__main__":
    pass
