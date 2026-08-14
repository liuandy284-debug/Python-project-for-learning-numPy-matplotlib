import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolor

# ===== Part 1: Slice operations ======
colors = ["white", "black", "orange"]
cmap = mcolor.ListedColormap(colors)
grid = np.zeros((6,6))
grid[0, :] = 1
grid[:, 0] = 1
grid[5, :] = 1
grid[3,3] = 2
grid[:, 5] = 1
fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])
ax.imshow(grid, cmap = cmap, vmin= 0, vmax = 2)
plt.show()

# ===== Part 2: Distance Calculation ======
p1 = np.array([0,0])
p2 = np.array([3,4])
manhaten = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
linalg = np.linalg.norm(p1 - p2)
print(manhaten, linalg)


# ===== Part 3: Conditional Operations ======

colors = ["white", "black"]
cmap = mcolor.ListedColormap(colors)

grid = np.random.randint(0,11,(5,5))
mean = np.mean(grid)
grid_max = np.max(grid)
grid_min = np.min(grid)
grid = np.where(grid > 5, 1, 0)
fig, ax = plt.subplots()
ax.imshow(grid, cmap = cmap, vmin = 0, vmax = 1)
plt.show()
print(f"Mean: {mean}")
print(f"Max: {grid_max}")
print(f"Min: {grid_min}")



