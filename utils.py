import pickle

import matplotlib.pyplot as plt
import pandas as pd


def pickle_object(python_obj, pickle_path):
    with open(pickle_path, 'wb') as f:
        pickle.dump(python_obj, f)
    return True


def load_pickle(pickle_path):
    with open(pickle_path, 'rb') as f:
        python_obj = pickle.load(f)
    return python_obj


def standard_plot(pd_dataframe):
    # print(pd_dataframe['Date'])
    plt.figure(figsize=(12, 6), dpi=100)
    plt.plot(pd_dataframe['Date'],
             pd_dataframe['KRW/USD'])
    plt.xlabel('Date')
    plt.xlabel('Rates')
    plt.grid()
    plt.show()


def concat_two_dfs(df_list):
    df = pd.concat(df_list,
                   axis=0)
    df = df.reset_index(drop=True)
    return df


def concat_n_dfs(df_list):
    df_0_1 = df_list[0:2]
    df_cat = concat_two_dfs(df_0_1)
    for df_follow in df_list[3:]:
        df_cat = concat_two_dfs([df_cat, df_follow])
    return df_cat


if __name__ == "__main__":
    data = load_pickle("KRW_USD_2017.pkl")
    print(data)
