# https://gluon-ts.mxnet.io/examples/basic_forecasting_tutorial/tutorial.html

# Third-party imports
import mxnet as mx
from mxnet import gluon
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

# Available Dataset

from gluonts.dataset.repository.datasets import get_dataset, dataset_recipes
from gluonts.dataset.util import to_pandas

print(f"Available datasets: {list(dataset_recipes.keys())}")
# Available datasets:
# ['exchange_rate',
# 'solar-energy',
# 'electricity',
# 'traffic',
# 'm4_hourly',
# 'm4_daily',
# 'm4_weekly',
# 'm4_monthly',
# 'm4_quarterly',
# 'm4_yearly']

# Download of Exemplary Data
dataset = get_dataset("m4_hourly", regenerate=True)

# SAMPLE DATA
entry = next(iter(dataset.train))
train_series = to_pandas(entry)
train_series.plot()
plt.grid(which="both")
plt.legend(["train series"], loc="upper left")
plt.show()

# ADD TEST SERIES

entry = next(iter(dataset.test))
test_series = to_pandas(entry)
test_series.plot()
plt.axvline(test_series.index[1], color='orange')  # end of test dataset
plt.axvline(train_series.index[-1], color='green')  # end of tEST dataset
plt.axvline(test_series.index[-1], color='red')  # end of tEST dataset
plt.grid(which="both")
plt.legend(["test series",
            "start of train/test series",
            "end of train series",
            "end of test series"], loc="upper left")
plt.show()

# TASK DESCRIPTION
print(f"Length of test series: {len(test_series)}")
print(f"Length of train series: {len(train_series)}")
print(f"Length of forecasting window in test dataset: {len(test_series) - len(train_series)}")
print(f"Recommended prediction horizon: {dataset.metadata.prediction_length}")
print(f"Frequency of the time series: {dataset.metadata.freq}")


if __name__ == "__main__":
    pass
