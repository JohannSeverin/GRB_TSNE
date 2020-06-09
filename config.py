import pandas as pd
import numpy as np

embedding = np.genfromtxt('embedding.csv', delimiter=',',dtype=str)
grbnames = embedding[:,0]
duration_data = pd.read_pickle('DataFrames/duration_data.dat')

conf = {
    'figsize': (12, 8),
    'radius': 5,
    'color': np.log(duration_data.loc[grbnames].T90),
    'cmap': 'plasma',
    'grb_highlight': ['GRB191019A']
}

tsne_params = {
<<<<<<< HEAD
    'perplexity':  40,
    'verbose':     2,  
=======
    'perplexity':  35,
    'verbose':      2,
>>>>>>> c1a5fba75ce3170a3b171e6a6455276b1b648da8
    'n_iter':   15000,
}