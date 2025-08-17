# Base Class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return f"{self.name} makes a sound."

# Subclass: Bird
class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.wing_span = wing_span
    
    def make_sound(self):
        return f"{self.name} the bird chirps."

# Subclass: Mammal
class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color
    
    def make_sound(self):
        return f"{self.name} the mammal growls."

# Subclass: Reptile
class Reptile(Animal):
    def __init__(self, name, species, is_venomous):
        super().__init__(name, species)
        self.is_venomous = is_venomous
    
    def make_sound(self):
        return f"{self.name} the reptile hisses."

# Example usage:
zoo_animals = [
    Bird("Parrot", "African Grey", 25),
    Mammal("Tiger", "Bengal Tiger", "Orange with Black Stripes"),
    Reptile("Cobra", "Indian Cobra", True)
]

# Polymorphism
for animal in zoo_animals:
    print(animal.make_sound())
