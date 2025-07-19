# Currency Converter from USD, EUR, or SAR to PKR

# Predefined exchange rates
exchange_rates = {
    "USD": 278.5,
    "EUR": 300.0,
    "SAR": 74.2
}

# Function to convert currency
def convert_to_pkr(amount, currency):
    currency = currency.upper()
    if currency in exchange_rates:
        return amount * exchange_rates[currency]
    else:
        return None

# Main Program
print("Welcome to Currency Converter (USD, EUR, SAR ➝ PKR)")
currency = input("Enter the currency (USD, EUR, SAR): ")
amount = float(input("Enter the amount: "))

converted = convert_to_pkr(amount, currency)

if converted:
    print(f"{amount} {currency.upper()} = {converted:.2f} PKR")
else:
    print("Invalid currency entered.")


# Function-based Basic Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Main loop
while True:
    print("\nBasic Calculator")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Choose operation (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please select between 1-5.")



# Simple Contact Book

contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print("Contact added.")

def view_contacts():
    if contacts:
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found.")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main Menu Loop
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
    option = input("Choose an option (1-5): ")

    if option == '1':
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)
    elif option == '2':
        view_contacts()
    elif option == '3':
        name = input("Enter name to search: ")
        search_contact(name)
    elif option == '4':
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif option == '5':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid option. Try again.")
