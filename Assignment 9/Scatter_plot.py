import matplotlib.pyplot as plt
import numpy as np

# Task 3: Scatter Plot
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

plt.figure()
plt.scatter(x, y, color="darkgreen", marker="o")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Scatter Plot Example")
plt.savefig("scatter_plot.png")
plt.show()
