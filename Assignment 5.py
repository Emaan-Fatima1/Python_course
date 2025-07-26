# Student Management System

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    with open("students.txt", "a") as file:
        file.write(f"{name},{marks}\n")
    print("Student added successfully.")

def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            if not students:
                print("No students found.")
                return
            for student in students:
                name, marks = student.strip().split(",")
                print(f"Name: {name}, Marks: {marks}")
    except FileNotFoundError:
        print("File not found. No students added yet.")

def remove_student():
    name_to_remove = input("Enter the name of the student to remove: ")
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
        with open("students.txt", "w") as file:
            removed = False
            for student in students:
                name, marks = student.strip().split(",")
                if name != name_to_remove:
                    file.write(f"{name},{marks}\n")
                else:
                    removed = True
            if removed:
                print("Student removed successfully.")
            else:
                print("Student not found.")
    except FileNotFoundError:
        print("File not found.")

# Menu
while True:
    print("\n1. Add Student\n2. View All Students\n3. Remove Student\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")


#JSON Book Manager

import json

def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def add_books():
    books = load_books()
    while True:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        books.append({"title": title, "author": author})
        more = input("Add another book? (y/n): ").lower()
        if more != "y":
            break
    save_books(books)
    print("Books added successfully.")

def view_books():
    books = load_books()
    if not books:
        print("No books found.")
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}")

# Menu
while True:
    print("\n1. Add Books\n2. View All Books\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_books()
    elif choice == "2":
        view_books()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")


#Expense Manager

def add_expense():
    item = input("Enter item name: ")
    amount = input("Enter amount: ")
    with open("expenses.txt", "a") as file:
        file.write(f"{item},{amount}\n")
    print("Expense added successfully.")

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            if not expenses:
                print("No expenses found.")
                return
            total = 0
            print("\nRecorded Expenses:")
            for expense in expenses:
                item, amount = expense.strip().split(",")
                print(f"{item}: Rs.{amount}")
                total += float(amount)
            print(f"\nTotal Spent: Rs.{total}")
    except FileNotFoundError:
        print("No expenses file found.")

# Menu
while True:
    print("\n1. Add Expense\n2. View All Expenses\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")
