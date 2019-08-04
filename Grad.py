import numpy as np
import utils

df = utils.load_pickle("data/KRW_USD_2019_Q3.pkl")
rates = df['KRW/USD']
values = rates.values
grads = np.gradient(values)
if __name__ == "__main__":
    pass
