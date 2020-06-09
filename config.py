import pandas as pd
import numpy as np

<<<<<<< HEAD
embedding = np.genfromtxt('embedding.csv', delimiter=',',dtype=str)
grbnames = embedding[:,0]
=======
embedding = np.genfromtxt('embedding.csv', delimiter=',')
grbnames = embedding[:, 0]
>>>>>>> 64558c756966238067f00b6304c03b5e77bdd856
duration_data = pd.read_pickle('DataFrames/duration_data.dat')

conf = {
    'figsize': (12, 8),
    'radius': 5,
<<<<<<< HEAD
    'color': duration_data.loc[grbnames].T90,
=======
    'color': np.log(duration_data.loc[grbnames]),
>>>>>>> 64558c756966238067f00b6304c03b5e77bdd856
    'cmap': 'plasma',
}
