import pandas as pd
import matplotlib.pyplot as plt
import json
from speed._constants import __path


# plt.rcParams['toolbar'] = 'None'

def plot_it():
    with open(__path, 'r') as f:
        raw_data = json.load(f)

    data = pd.json_normalize(raw_data)
    s = pd.to_datetime(data['date'])
    data['date'] = s.dt.date
    data = data.set_index('date')
    ax = data['speed'].plot()
    ax.set(xlabel='Date',
           ylabel='Speed (Mbs)',
           title='Download Speeds')
    plt.setp(ax.get_xticklabels(), rotation=35)
    plt.subplots_adjust(bottom=.15)
    plt.show()


if __name__ == '__main__':
    plot_it()
