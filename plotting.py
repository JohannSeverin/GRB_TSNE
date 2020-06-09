import matplotlib.pyplot as plt
import numpy as np
from config import conf

embedding = np.genfromtxt('embedding.csv', delimiter=',')
grbnames = embedding[:,0]
emb = embedding[:,1:]

fig, ax = plt.subplots(conf{'figsize'})

emb_plot = ax.scatter(emb[:,0],emb[:,1],s=conf{'radius'},c=conf{'color'},cmap=conf{'cmap'})

print('hello')