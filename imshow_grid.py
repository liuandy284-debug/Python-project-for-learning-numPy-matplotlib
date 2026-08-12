import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

grid = np.zeros((8,8))  #set a canvas with 8 rows and 8 cols
grid[0,:] = 1  # set black colors
grid[:,0] = 1
grid[7,:] = 1
grid[:,7] = 1
grid[6,6] = 3  # set red color
grid[4,4] = 2  # set green color
colors = ["white", "black", "green", "red"]
#   index: 0,       1,       2,       3
cmap = mcolors.ListedColormap(colors)
fig, ax = plt.subplots()
ax.set_title("Data visualization")
ax.set_xticks([])  # cancle x axis label
ax.set_yticks([])  # cancle y axis label 
ax.imshow(grid, cmap = cmap, vmin = 0, vmax = 3)
plt.show()