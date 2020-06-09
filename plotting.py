import matplotlib.pyplot as plt
import numpy as np
from config import conf

embedding = np.genfromtxt('embedding.csv', delimiter=',',dtype=str)
grbnames = embedding[:,0]
emb = embedding[:,1:].astype(float)

fig, ax = plt.subplots(figsize = conf{'figsize'})

emb_plot = ax.scatter(emb[:, 0], emb[:, 1], s=conf{'radius'}, c=conf{'color'}, cmap=conf{'cmap'})
ax.set(xticks=[], yticks=[])

cbar = plt.colorbar(emb_plot,ax)

ax.set(yticks = (), xticks = ())

