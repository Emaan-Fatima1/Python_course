import matplotlib.pyplot as plt
import numpy as np

# Task 1: Line Plot
x = list(range(1, 11))   # X values from 1 to 10
y = x

plt.plot(x, y, color="blue", linestyle="-", marker="o")  # Line plot
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Line Plot")
plt.grid(True) 
plt.savefig("line_plot.png")  # Save figure
plt.show()
