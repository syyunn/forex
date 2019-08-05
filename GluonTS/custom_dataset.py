import numpy as np
import pandas as pd

# NUMPY PHASE
N = 10  # number of classes in time series
T = 100  # number of time steps

prediction_length = 24
freq = "1H"
custom_dataset = np.random.normal(size=(N, T))
start = pd.Timestamp("01-01-2019", freq=freq)  # can be different for each time series

# CONVERSION TO GLUON PHASE
from gluonts.dataset.common import ListDataset

# # train is less of "prediction length" compared to test dataset
train_ds = ListDataset([{'target': x, 'start': start}
                        for x in custom_dataset[:, :-prediction_length]],
                       freq=freq)
# # test dataset: use the whole dataset, add "target" and "start" fields
test_ds = ListDataset([{'target': x, 'start': start}
                       for x in custom_dataset],
                      freq=freq)

if __name__ == "__main__":
    pass
