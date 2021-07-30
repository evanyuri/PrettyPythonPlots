import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

spacing = 0.2
max=10
n = int(max/spacing)
x = np.arange(0,max,spacing)
a = np.sin(x)
b = np.cos(x)
t = np.arange(0,n)


print(t)
# Creare your figure and axes
fig,ax = plt.subplots(1)
# Set whitespace to 0
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
#print(x)

ax.scatter(x,a, c=t, cmap ='jet' )
ax.scatter(x,b, c=t,cmap='jet' ), 

ax.grid = 'none'
ax.axis('off')
ax.set_facecolor('white') 
ax.set_aspect(1)

plt.show()
