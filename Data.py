import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def get_technical_indicators(dataset):
    rates = dataset.columns.values[1]

    # Create 7 and 21 days Moving Average
    dataset['ma7'] = dataset[rates].rolling(window=7).mean()
    dataset['ma14'] = dataset[rates].rolling(window=14).mean()
    dataset['ma21'] = dataset[rates].rolling(window=21).mean()

    # Create Gradients w/ 14 days of window
    values = dataset['ma14'].values
    grads = np.gradient(values)
    dataset['grad_ma14'] = grads

    dataset['grad_14sd'] = dataset['grad_ma14'].rolling(14).std()
    dataset['grad_upper_band'] = dataset['grad_ma14'] + (dataset['grad_14sd'] * 2)
    dataset['grad_lower_band'] = dataset['grad_ma14'] - (dataset['grad_14sd'] * 2)

    # Create MACD
    dataset['26ema'] = dataset[rates].ewm(span=26).mean()
    dataset['12ema'] = dataset[rates].ewm(span=12).mean()
    dataset['MACD'] = (dataset['12ema'] - dataset['26ema'])

    # Create Bollinger Bands
    dataset['20sd'] = dataset[rates].rolling(20).std()
    dataset['upper_band'] = dataset['ma21'] + (dataset['20sd'] * 2)
    dataset['lower_band'] = dataset['ma21'] - (dataset['20sd'] * 2)

    # Create std of std
    dataset['ma14_of_grads_ma14'] = dataset['grad_ma14'].rolling(window=14).mean()

    # Create Exponential moving average
    dataset['ema'] = dataset[rates].ewm(com=0.5).mean()

    # Create Momentum
    dataset['momentum'] = dataset[rates] - 1

    # Create Log Momentum
    dataset['log_momentum'] = np.log(dataset['momentum'])

    return dataset


def plot_technical_indicators(dataset,
                              last_days=None):
    ticker = dataset.columns.values[1]
    plt.figure(figsize=(30, 10), dpi=150)
    # shape_0 = dataset.shape[0]
    # xmacd_ = shape_0 - last_days
    #
    if last_days:
        dataset = dataset.iloc[-last_days:, :]

    x_ = list(dataset.index)
    zeros = [0] * len(x_)
    roots = np.argwhere(np.diff(np.sign(zeros - dataset['ma14_of_grads_ma14']))).flatten()

    roots_indices = dataset.index[roots]
    roots_dates = dataset['Date'][roots_indices]
    # x_ = range(3, dataset.shape[0])
    # x_ = list(dataset.index)

    ax = plt.axes()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m'))

    # Plot first subplot
    plt.subplot(2, 1, 1)
    plt.plot(dataset['Date'], dataset['ma7'], label='MA 7', color='g', linestyle='--')
    plt.plot(dataset['Date'], dataset['ma14'], label='MA 14', color='black', linestyle='--')
    plt.plot(dataset['Date'], dataset['ma21'], label='MA 21', color='r', linestyle='--')
    plt.plot(dataset['Date'], dataset[ticker], label='Closing Price', color='b')
    plt.plot(dataset['Date'], dataset['upper_band'], label='Upper Band', color='c')
    plt.plot(dataset['Date'], dataset['lower_band'], label='Lower Band', color='c')
    plt.fill_between(dataset['Date'], dataset['lower_band'], dataset['upper_band'], alpha=0.35)
    plt.title('Technical indicators for FOREX RATES')
    plt.ylabel('Rates')
    plt.legend()

    #Plot second subplot
    plt.subplot(2, 1, 2)
    plt.plot(dataset['Date'], dataset['grad_ma14'], label='Grad MA 14', color='orange', linestyle='--')
    plt.plot(dataset['Date'], dataset['grad_upper_band'], label='Grad14 Upper Band', color='c')
    plt.plot(dataset['Date'], dataset['grad_lower_band'], label='Grad14 Lower Band', color='c')
    plt.plot(dataset['Date'], dataset['ma14_of_grads_ma14'], label='14MA of Grad14', color='black')
    plt.axhline(y=0, color='r', linestyle='-')
    dates_ticks = [i.strftime('%y-%m-%d') for i in roots_dates]

    plt.xticks(roots_dates, dates_ticks)
    for root_date in roots_dates:
        plt.axvline(x=root_date, linestyle='--', ymax=0.445)

    # plt.plot(dataset['Date'], [0]*len(dataset), markevery=roots_dates, marker='o', color='b')

    # plt.title('MACD')
    # plt.plot(dataset['MACD'], label='MACD', linestyle='-.')
    # plt.hlines(15, xmacd_, shape_0, colors='g', linestyles='--')
    # plt.hlines(-15, xmacd_, shape_0, colors='g', linestyles='--')
    # plt.plot(dataset['log_momentum'], label='Momentum', color='b',
    #          linestyle='-')
    # plt.savefig(
    #     '../assets/Techinical_indicators_for_Goldman_Sachs_last_400_days.png')
    plt.legend()

    plt.show()
