import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from utils import load_pickle, pickle_object

data = load_pickle("data/KRW_USD_2019_Q1_Q2.pkl")

# # prices = []
# # dates = []
# # for item in data:
# #     date = list(item.keys())[0]
# #     price = list(item.values())[0]
# #
# #     dates.append(date)
# #     prices.append(price)
# #
# # dates = np.array(dates, dtype='datetime64[D]')
# #
# # data = {'Date': dates,
#         'KRW/USD': prices}
df = pd.DataFrame(data)

print(df['Date'])
plt.figure(figsize=(12, 6), dpi=100)
plt.plot(df['Date'],
         df['KRW/USD'],
         c='blue')
plt.xlabel('Date')
plt.grid()
plt.show()

if __name__ == "__main__":
    pass
