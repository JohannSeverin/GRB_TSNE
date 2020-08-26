import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from config import conf

emb = pd.read_csv("embedding.csv", header = None).set_index(0)  

fig, ax = plt.subplots(figsize=conf['figsize'])
ax.set(yticks=(), xticks=(), title='Embedding')

emb_plot = ax.scatter(emb[1], emb[2], s=conf['radius'], c=conf['color'], cmap=conf['cmap'])

highlights = ax.scatter(emb.loc[conf['grb_highlight']][1],emb.loc[conf['grb_highlight']][2],marker='x',s=10*conf['radius'],c='k')

cbar = plt.colorbar(emb_plot, None, ax)



fig.savefig("FlotPlot.jpg")
fig.show()
