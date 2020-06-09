import pandas as pd
import numpy as np

embedding = np.genfromtxt('embedding.csv', delimiter=',')
grbnames = embedding[:, 0]
duration_data = pd.read_pickle('DataFrames/duration_data.dat')

conf = {
    'figsize': (12, 8),
    'radius': 5,
    'color': np.log(duration_data.loc[grbnames]),
    'cmap': 'plasma',
}
