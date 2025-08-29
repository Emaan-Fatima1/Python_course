import matplotlib.pyplot as plt

# Task 2: Bar Chart
students = ["Ali", "Sara", "John", "Ayesha", "Tom"]
marks = [80, 90, 70, 85, 60]
colors = ["red", "blue", "green", "orange", "purple"]  # Different colors 

plt.figure()
plt.bar(students, marks, color=colors)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Students")
plt.xticks(rotation=45)  # Rotate labels
plt.savefig("bar_chart.png")
plt.show()
