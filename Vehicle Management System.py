#Base Class
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand} Model: {self.model}")

#Subclass Car
class Car(Vehicle):
    def __init__(self, brand, model,fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Vehicle: Car  Brand: {self.brand}  Model: {self.model}  Fuel Type: {self.fuel_type}")

#Subclass Bike
class Bike(Vehicle):
    def __init__(self, brand, model,engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Vehicle: Bike  Brand: {self.brand}  Model: {self.model}  Engine Capacity: {self.engine_capacity}")
              
#Subclass Truck
class Truck(Vehicle):
    def __init__(self, brand, model,load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def display_info(self):
        print(f"Vehicle: Truck  Brand: {self.brand}  Model: {self.model}  Load Capacity: {self.load_capacity}")

#Objects
vehicles = [
    Car("Toyota", "Corolla", "Petrol"),
    Bike("Honda", "CBR500R", 500),
    Truck("Volvo", "FH16", 25)
]

for v in vehicles:
    v.display_info()
