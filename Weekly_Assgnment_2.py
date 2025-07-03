#Part 1

#Ask the user to enter a number and convert it to an integer
num = int(input("Enter a number: "))  # input number

#Check condition
if num > 10 and num % 2 == 0:         # check condition if true
    print("Valid Number")             # if both conditions are true
else:
    print("Invalid number")           # if any condition is false


#Part 2

#Age categorization

age = int(input("Enter your age: "))  # Ask the user to input their age

# Check age group
if age < 13:
    print("You are a child")              # If age is less than 13
elif age >= 13 and age <= 19:
    print("You are a teenager")           # If age is between 13 and 19 
elif age >= 20:
    print("You are an adult")             # If age is 20 or above
else:
    print("Invalid Input")                # For any unexpected input (e.g. negative)

# Classify Number

number = int(input("Enter a number: "))   # Ask the user to input a number

# Check if the number is zero, positive or negative
if number == 0:
    print("The number is zero")
elif number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("Invalid input")            

# Temperature Check

temp = float(input("Enter temperature: "))  # Ask the user to input temperature 

# Check temperature and print message
if temp < 10:
    print("It's a cold day")                # Below 10°C is cold
elif temp >= 10 and temp <= 25:
    print("It's a nice day")                # 10°C to 25°C is moderate/nice
elif temp > 25:
    print("It's a hot day")                 # Above 25°C is hot
else:
    print("Invalid Input")                  


#Part 3:

fruits = ["kiwi", "pomegranate", "apple", "pineapple", "strawberry"]

print("All Fruits:")
for i in fruits:
    print(f"- {i}")

print("\nFruits with more than 5 letters:")
for j in fruits:
    if len(j) > 5:
        print(f"- {j}")



#Number list
num_list = [10, 15, 23, 40, 50]

# Print the square of each number
print("Square of each number: ")
for n in num_list:
    print(n * n)

# Print only the even numbers
print("\nEven numbers: ")
for n in num_list:
    if n % 2 == 0:
        print(n)


#Name list
name_list = ["Baris", "Gulum", "Hakan", "Mehmet", "Mehrimah", "Umut"]

# Greet each person
for i in name_list:
    print(f"Good morning {i}, Have a nice day!")

# Print total number of names
print(f"\nTotal number of names: {len(name_list)}")

#Number list, hghest and lowest number
number_list = [4, 5, 6, 9, 12, 13, 50, 60, 70, 33]

# Find highest number
highest = number_list[0]
for j in number_list:
    if j > highest:
        highest = j
print(f"The highest number is {highest}")

# Find lowest number
lowest = number_list[0]
for j in number_list:
    if j < lowest:
        lowest = j
print(f"The lowest number is {lowest}")

# divisible by 3
print("The numbers divisible by 3 are: ")
for j in number_list:
    if j % 3 == 0:
        print(j)

#print squares
print("The squares of numbers from 1 to 10: ")
for num in range(1, 11):
    print(f"Number= {num} , Square= {num * num}")

#print even numbers
for num in range(20, 41):
    if num % 2 == 0:
        print(num)
  

#Part 4:

 #Grading System

#Ask the user to enter marks
marks = int(input("Enter the marks please: "))

#Assign grade according to marks
if marks >= 90:
    grade = "A grade"        # If marks are 90 or above
elif marks >= 80:
    grade = "B grade"        # If marks are 80 to 89
elif marks >= 70:
    grade = "C grade"        # If marks are 70 to 79
elif marks >= 60:
    grade = "D grade"        # If marks are 60 to 69
elif marks < 60:
    grade = "Fail"           # If marks are below 60
else:
    print("invalid input")   

# Print the assigned grade
print(grade)

#Login system

# Fixed username and password
correct_username = "emaan"
correct_password = "2006"
# Get input from user
username = input("Enter username: ")
password = input("Enter password: ")
# Check both inputs
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Access Denied")
