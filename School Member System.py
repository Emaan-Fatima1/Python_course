#base class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

#subclass student
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def introduce(self):
        print(f"Hello! I am {self.name}, {self.age} years old, and I study in grade {self.grade}.")

# Subclass: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def introduce(self):
        print(f"Hello! I am {self.name}, {self.age} years old, and I teach {self.subject}.")

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role
    
    def introduce(self):
        print(f"Hi there! I am {self.name}, {self.age} years old, and I work as a {self.role}.")

# Example usage:
members = [
    Student("Ali", 15, "10th"),
    Teacher("Ahmed", 40, "Mathematics"),
    Staff("Sara", 35, "Librarian")
]

# Polymorphism in action
for member in members:
    member.introduce()
