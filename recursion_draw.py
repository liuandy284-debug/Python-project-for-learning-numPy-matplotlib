import numpy as np
import matplotlib.pyplot as plt

#define a recursion function for drawing
def draw_branch(ax, x, y, angle, length, depth):
    if depth == 0:   #shut down statement
        return 
    # calculate the movement each time
    end_x = x + length * np.cos(np.radians(angle))
    end_y = y + length * np.sin(np.radians(angle))

    ax.plot([x, end_x], [y, end_y])  #draw a line each time

    draw_branch(ax, end_x, end_y, angle - 30, length * 0.7, depth - 1)
    draw_branch(ax, end_x, end_y, angle + 30, length * 0.7, depth - 1)


fig, ax = plt.subplots()
ax.axis("off")   #clean the x and y lable from the canva
draw_branch(ax, 0, 0, 90, 100, 7)
plt.show()


"""
PRACTICE: 
============================
def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + recursive_sum(lst[1:])

============================
def reverse(s):
    if len(s) == 1:
        return s[0]
    return reverse(s[1:]) + s[0]

"""