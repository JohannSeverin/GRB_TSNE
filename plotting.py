import matplotlib.pyplot as plt
import numpy as np
from config import conf

embedding = np.genfromtxt('embedding.csv', delimiter=',')
grbnames = embedding[:,0]
emb = embedding[:,1:]

fig, ax = plt.subplots(conf{'figsize'})

emb_plot = ax.scatter(emb[:,0],emb[:,1],s=conf{'radius'},c=conf{'color'},cmap=conf{'cmap'})

<<<<<<< HEAD
cbar = plt.colorbar(emb_plot,ax)

ax.set(yticks = (), xticks = ())
=======
print('hello')
>>>>>>> a5c23297788ebe6b07c017edbc75d02e823b5bdc
