import matplotlib.pyplot as plt

# Task 5: Histogram
data = [7,8,5,6,5,7,8,9,6,5,7,6,8,9,7,6,5,8,9,7]

plt.figure()
plt.hist(data, bins=5, color="skyblue", edgecolor="black")
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.title("Histogram of Data")
plt.savefig("histogram.png")
plt.show()
