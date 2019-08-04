from Data import get_technical_indicators, plot_technical_indicators
import utils

df1 = utils.load_pickle("data/KRW_USD_2017.pkl")
df2 = utils.load_pickle("data/KRW_USD_2018.pkl")
df3 = utils.load_pickle("data/KRW_USD_2019_Q1_Q2.pkl")
df4 = utils.load_pickle("data/KRW_USD_2019_Q3.pkl")

df = utils.concat_n_dfs([df1, df2, df3, df4])

df_ti = get_technical_indicators(df)

plot_technical_indicators(df_ti,
                          last_days=420)

if __name__ == "__main__":
    pass
