import numpy as np
import matplotlib.pyplot as plt

#------Data set------
Grades = np.array([55, 20, 40, 66, 75, 80, 91, 95])
name = np.array(["Andy", "Sandy", "Claire", "Sam", "Luke", "Icey", "Freya", "Felix"])

# Creat four subplot(plot, scatter plots, histograms, bar charts)
fig, ax = plt.subplots(2,2)  #four graphs with two rows and two cols
ax[0,0].plot(name, Grades, marker = "o")
ax[0,0].set_title("Plot")
ax[0,0].tick_params(axis = "x", rotation = 45)  #rotate every x label with 45 degrees

ax[0,1].scatter(name, Grades)
ax[0,1].set_title("Scatter plot")
ax[0,1].tick_params(axis = "x", rotation = 45)

ax[1,0].hist(Grades, bins = [0, 20, 40, 60, 80, 100], edgecolor = "black")
ax[1,0].set_title("Histogram")

ax[1,1].bar(name, Grades)
ax[1,1].set_title("Bar chat")
ax[1,1].tick_params(axis = "x", rotation = 45)
plt.tight_layout()  #automatic adjust layout make sure all the details are visible
plt.show()  #showing the graph
