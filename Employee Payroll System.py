# Base Class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def __str__(self):
        return f"Employee: {self.name}"


# Subclass: Manager
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


# Subclass: Developer
class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours, hourly_rate):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.base_salary + (self.overtime_hours * self.hourly_rate)


# Subclass: Intern
class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name, 0)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


# Demonstration (Polymorphism)
employees = [
    Manager("Eugene", 50000, 10000),
    Developer("Rose", 40000, 15, 800),
    Intern("Hassan", 15000)
]

for emp in employees:
    print(f"{emp.name}'s Salary: {emp.calculate_salary()}")
