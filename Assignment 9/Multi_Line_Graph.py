import matplotlib.pyplot as plt

# Task 4: Multiple Lines
x = list(range(1, 11))
y1 = [i for i in x]       # y = x
y2 = [i**2 for i in x]    # y = x^2

plt.figure()
plt.plot(x, y1, label="y = x", color="blue", linestyle="--")
plt.plot(x, y2, label="y = x^2", color="red", linestyle="-")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Multiple Lines")
plt.legend()
plt.savefig("multiple_lines.png")
plt.show()
