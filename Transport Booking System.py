# Base Class
class Transport:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def book_ticket(self):
        return f"Booking ticket for {self.name} (Capacity: {self.capacity})"

# Subclass: Bus
class Bus(Transport):
    def __init__(self, name, capacity, route_number):
        super().__init__(name, capacity)
        self.route_number = route_number
    
    def book_ticket(self):
        return f"Bus ticket booked on route {self.route_number} on {self.name}."

# Subclass: Train
class Train(Transport):
    def __init__(self, name, capacity, coach_type):
        super().__init__(name, capacity)
        self.coach_type = coach_type
    
    def book_ticket(self):
        return f"Train ticket booked in {self.coach_type} coach on {self.name}."

# Subclass: Flight
class Flight(Transport):
    def __init__(self, name, capacity, airline):
        super().__init__(name, capacity)
        self.airline = airline
    
    def book_ticket(self):
        return f"Flight ticket booked with {self.airline} on {self.name}."

# Example usage:
bookings = [
    Bus("Faisal Movers", 50, "H12"),
    Train("Shalimar", 300, "First Class"),
    Flight("Boeing 737", 180, "Etihad Airlines")
]

# Polymorphism 
for transport in bookings:
    print(transport.book_ticket())
