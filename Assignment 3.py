# Student List Manager 

students = []  # list to store names

while True:
    print("1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Exit")

    choice = input("Choose task to be performed (1-4): ")  # ask user for choice

    if choice == "1":                                       # add name
        name = input("Name to add: ")
        students.append(name)
        print("Name Added")

    elif choice == "2":                                     # remove name
        name = input("Name to remove: ")
        if name in students:
            students.remove(name)
            print("Name Removed")
        else:
            print("Not found")

    elif choice == "3":                                     # view list
        print("Students:")
        if len(students) == 0:
            print("No students yet.")
        else:
            for s in students:
                print(s)

    elif choice == "4":                                      # exit
        print("Exiting program.")
        break  

    else:                                                    # wrong input
        print("Wrong option.")



#Simple To-Do List Manager

to_do_list = []  #list to store the tasks

while True:                                               #loop
    print(f"\n1. Add \n2. Delete \n3. View \n4. Exit")       #print menu

    # Ask the user what they want to do
    choice = input("Choose an option (1-4): ")

    #user to add a task
    if choice == "1":
        task = input("Enter task to add: ")
        to_do_list.append(task) 
        print("Task added.")

    # If user chooses to delete a task
    elif choice == "2":
        task = input("Enter task to delete: ")
        if task in to_do_list:
            to_do_list.remove(task)               # Remove the task from list
            print("Task deleted.")
        else:
            print("Task not found.")              # Task doesn't exist

    # If user wants to view the tasks
    elif choice == "3":
        print("To-Do List:")
        if len(to_do_list) == 0:
            print("No tasks yet.")                # If list is empty
        else:
            for t in to_do_list:
                print(t)

    # If user chooses to exit
    elif choice == "4":
        print("Goodbye")
        break

else:
    print("Invalid input")


#Vowel Counter

sentence = input("\nEnter a sentence: ")                     #Enter the sentence
vowels= ["a","e","i","o","u","A","E","I","O","U"]          #list of vowels

vowel_count = 0                                            #initialize count to 0

for vowel in vowels:                                       #loop to count vowels
    vowel_count += sentence.count(vowel)

print("Total number of vowels:", vowel_count)              #print number of vowels


#Word Length Filter

the_sentence = input("\nEnter sentence: ")                     #enter sentence 
word_split = the_sentence.split()                            #split the words
for word in word_split:
    if len(word)>4:                                          #words having more than 4 letters
        print(word)                                          #print


#Word Reverser

#Ask the user for a sentence
my_sentence = input("\nEnter sentence: ")  

# Split sentence into words
words = my_sentence.split()

# Reverse each word 
for word in words:
    print(word[::-1])                                   #[end:start:step]  eg:[4:-1:-1]


#Basic Calculator that runs until the user types "exit"

while True:
    num1 = input("\nEnter first number (or type 'exit' to close): ")

    # Check if user wants to exit or continue
    if num1 == "exit":                                    #first number or exit
        print("Calculator closed.")
        break

    num2 = float(input("Enter second number: "))                 #second number
    operator = input("Enter operator: ")                   #operator

    # Convert number 1 from string to float
    num1 = float(num1)

    # Perform calculation
    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator.")
