import numpy as np
import matplotlib.pyplot as plt

grid = np.zeros((15,15))

for row in range(15):
    for col in range(15):
        distance = np.linalg.norm(np.array([row,col]) - np.array([7,7]))  #calculate the distance between two possition & can's use grid[row, col] because it will return the value of that possition
        grid[row,col] = max(0, 100 - distance * 10) #calculate the temp and change the value on each possition
                        
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap = "hot")  #save the image as img
plt.colorbar(img, ax=ax)  #create a color bar based on "img" to illustrate the meaning of each color 
ax.set_xticks([])
ax.set_yticks([])
plt.show()