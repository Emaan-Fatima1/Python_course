import matplotlib.pyplot as plt

# Task 6: Pie Chart
activities = ["Sleeping", "School/Work", "Hobbies", "Exercise", "Other"]
hours = [8, 7, 4, 2, 3]

plt.figure(figsize=(8,5))  # Bigger size 
plt.pie(hours, labels=activities, autopct="%1.1f%%", startangle=90)
plt.title("Daily Activities")
plt.savefig("pie_chart.png")
plt.show()
