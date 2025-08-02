# 1. Class and Object Creation
class Car:
    def __init__(self, brand, model, year):  
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

print("Q1 Output:")

print(car1.brand, car1.model, car1.year)
print(car2.brand, car2.model, car2.year)
print("\n")


# 2. Use of self and Instance Variables
class Car:
    def __init__(self, brand, model, year): 
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):  # Shows all info about the car
        print(f"{self.year} {self.brand} {self.model}")

print("Q2 Output:")
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Call the display method
car1.display_info()
car2.display_info()
print("\n")


# 3. Class vs Instance Variables
class Student:
    school_name = "ABC School"  # Same for every student

    def __init__(self, name, grade):  # Set unique name and grade
        self.name = name
        self.grade = grade

print("Q3 Output:")
student1 = Student("Ali", "8th")
student2 = Student("Sara", "9th")

# Show details for both students
print(student1.name, student1.grade, student1.school_name)
print(student2.name, student2.grade, student2.school_name)

# Change school name
Student.school_name = "XYZ Grammar School"

# See the change in both students
print(student1.school_name)
print(student2.school_name)
print("\n")


# 4. Constructor and Initialization
class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def introduce(self):  
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

print("Q4 Output:")

p1 = Person("Zara", 25)
p2 = Person("Usman", 30)
p1.introduce()
p2.introduce()
print("\n")


# 5. Inheritance Basics
# Main animal class
class Animal:
    def make_sound(self):  # Default sound
        print("sound")

class Dog(Animal):
    def make_sound(self):  # Dog sound
        print("Bark")

class Cat(Animal):
    def make_sound(self):  # Cat sound
        print("Meow")

print("Q5 Output:")
d = Dog()
c = Cat()
d.make_sound()
c.make_sound()
print("\n")


# 6. Using super()
# Basic employee class
class Employee:
    def __init__(self, name, salary):  # Set name and salary
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Use parent class to set name and salary
        self.department = department    # Extra info for manager

print("Q6 Output:")
m = Manager("Hina", 70000, "Sales")
print(m.name, m.salary, m.department)
print("\n")


# 7. Constructor Chaining with Inheritance
# Vehicle class with brand
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

# Bike class that also has engine size
class Bike(Vehicle):
    def __init__(self, brand, engine_cc):
        super().__init__(brand)      # Get brand from Vehicle class
        self.engine_cc = engine_cc   # Add engine size

    def show_info(self):
        print(f"Brand: {self.brand}, Engine: {self.engine_cc}cc")

print("Q7 Output:")
b = Bike("Yamaha", 150)
b.show_info()
print("\n")


# 8. Count Number of Objects
# Counts how many times we made objects
class Counter:
    count = 0  # Starts at 0

    def __init__(self):
        Counter.count += 1  # Add 1 every time an object is made

print("Q8 Output:")
# Make objects
o1 = Counter()
o2 = Counter()
o3 = Counter()
o4 = Counter()
o5 = Counter()

# Print count of objects
print("Total objects created:", Counter.count)
print("\n")


# 9. Inheritance with Polymorphism
# Shape class for different shapes
import math

class Shape:
    def area(self):  # Base method (empty)
        pass

# Rectangle shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):  # Rectangle area = length * width
        return self.length * self.width

# Circle shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Circle area = π * r^2
        return math.pi * self.radius ** 2

print("Q9 Output:")
# Make list of shapes
shapes = [Rectangle(5, 3), Circle(4)]

# Call the same method (area) for both shapes
for shape in shapes:
    print("Area:", shape.area())
