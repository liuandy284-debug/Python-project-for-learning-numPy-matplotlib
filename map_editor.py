import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolor

colors = ["white", "black"]  #set two colors
cmap = mcolor.ListedColormap(colors)
grid = np.zeros((10,10))  #creat a map with 10 rows and 10 cols

fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])
img = ax.imshow(grid, cmap = cmap, vmin = 0, vmax = 1)  #save image

def on_click(event):
    if event.inaxes:
        col = int(event.xdata + 0.5)  #round row to nearest integer
        row = int(event.ydata + 0.5)  #round col to nearest integer
        """
        event.button == 1   # left
        event.button == 2   # middel
        event.button == 3   # right
        """
        if event.button == 1:
            grid[row, col] = 1
        elif event.button == 3:
            grid[row,col] = 0
        img.set_data(grid)  #update the value of img
        fig.canvas.draw()  #update the canvas (the difference between animation, animation will automaticallt call fig.canvas.draw() function, so we don't need to write it)

fig.canvas.mpl_connect("button_press_event", on_click)
# formula of this function: (event, function)
"""
events:
'button_press_event'
'button_release_event'
'motion_notify_event'
'key_press_event'
'scroll_event'
we can use multiple mpl_connect() function to change the canvas
"""

plt.show()
        
