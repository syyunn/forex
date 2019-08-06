import numpy as np
import pandas as pd
from gluonts.model import deepar

import utils

years = [i for i in range(1997, 2019)]
dfs = []
for year in years:
    df = utils.load_pickle("../data/KRW_USD_{}.pkl".format(year))
    dfs.append(df)

df = utils.concat_n_dfs(dfs)

utils.standard_plot(df)

timesteps = df['Date']
start = timesteps[0]
custom_dataset = np.array(df['KRW/USD'])

# NUMPY PHASE
N = 1  # number of classes in time series
T = len(custom_dataset) # number of time steps

prediction_length = 21
freq = "1D"

# CONVERSION TO GLUON PHASE
from gluonts.dataset.common import ListDataset

# # train is less of "prediction length" compared to test dataset
train_ds = ListDataset([{'target': custom_dataset,
                         'start': start}],
                       freq=freq)
# # test dataset: use the whole dataset, add "target" and "start" fields
test_ds = ListDataset([{'target': custom_dataset,
                        'start': start}],
                      freq=freq)

estimator = deepar.DeepAREstimator(freq=freq,
                                   prediction_length=prediction_length)

predictor = estimator.train(training_data=train_ds)

prediction = next(predictor.predict(train_ds))
print(prediction.mean)
prediction.plot(output_file='graph.png')


if __name__ == "__main__":
    pass
