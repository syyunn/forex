import utils
import pandas as pd

df1 = utils.load_pickle("data/KRW_USD_2019_Q1_Q2.pkl")

df2 = utils.load_pickle("data/KRW_USD_2019_Q3.pkl")

df = pd.concat([df1,
                df2],
               axis=0)

utils.standard_plot(df)

if __name__ == "__main__":
    pass
