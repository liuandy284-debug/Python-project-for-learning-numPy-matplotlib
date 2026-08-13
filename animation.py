from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.colors as mcolor
import numpy as np

colors = ["white", "orange"]  #two colors, Orange means current possition
cmap = mcolor.ListedColormap(colors)

grid = np.zeros((8,8))  #create a canva with 8 rows and 8 cols 
fig, ax = plt.subplots()
ax.set_title("Animation Visualization")
ax.set_xticks([])
ax.set_yticks([])

img = ax.imshow(grid, cmap = cmap, vmin = 0, vmax = 1)
def update(frame):  #update the animation
    grid[:,:] = 0
    if frame < 7:
        grid[0, frame] = 1
    else:
        grid[frame % 7, 7] = 1
    img.set_data(grid)
    return img

anim = FuncAnimation(fig, update, frames = 15, interval = 300, repeat = False) #update 15 times
plt.show()