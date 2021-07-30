from turtle import color
from matplotlib.colors import Colormap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(0,10,0.1)
a = np.sin(x)
b = np.cos(x)
t = np.arange(0,100)

print(t)
# Creare your figure and axes
fig,ax = plt.subplots(1)

# Set whitespace to 0
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
#print(x)
for i in range(0,len(x)-16):
    ax.plot([x[i+16],x[i]],[a[i+16],b[i]], c='black')
ax.scatter(x,a, c=t)
ax.scatter(x,b, c=t)

ax.grid = 'none'
ax.axis('off')
ax.set_facecolor('white') 
ax.set_aspect(1)

plt.show()


