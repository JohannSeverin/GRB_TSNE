import numpy as np
import pandas as pd
from sklearn.manifold import TSNE

#loading data
non_fft_dataset = pd.read_pickle('non_fft_dataset.dat')

#taking Fast Fourier Transform
fft = np.fft.rfft(non_fft_dataset)

#running t-SNE, n_iter should be higher than 'n_termination'
emb = TSNE(verbose = 2, perplexity = 30, n_iter = 50000).fit_transform()