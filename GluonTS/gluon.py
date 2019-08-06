import pandas as pd
url = "https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv"
df = pd.read_csv(url, header=0, index_col=0)

import matplotlib.pyplot as plt
df[:100].plot(linewidth=2)
plt.grid(which='both')
plt.show()

pass1 = df.index[0]
pass2 = df.value[df.value[:"2015.txt-04-05 00:00:00"]]

# Train
from gluonts.dataset.common import ListDataset
training_data = ListDataset(
    [{"start": df.index[0],
      "target": df.value[:"2015.txt-04-05 00:00:00"]}],
    freq="5min"
)

from gluonts.model.deepar import DeepAREstimator
from gluonts.trainer import Trainer

estimator = DeepAREstimator(freq="5min",
                            prediction_length=12,
                            trainer=Trainer(epochs=10))
predictor = estimator.train(training_data=training_data)


# Test
test_data = ListDataset(
    [{"start": df.index[0], "target": df.value[:"2015.txt-04-15 00:00:00"]}],
    freq = "5min"
)

from gluonts.dataset.util import to_pandas

for test_entry, forecast in zip(test_data, predictor.predict(test_data)):
    to_pandas(test_entry)[-60:].plot(linewidth=2)
    forecast.plot(color='g', prediction_intervals=[50.0, 90.0])
plt.grid(which='both')
plt.show()


if __name__ == "__main__":
    pass
