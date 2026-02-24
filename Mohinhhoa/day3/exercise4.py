name = input("Enter the name of the vehicle: ")
max_speed = int(input("Enter the max speed of the vehicle: "))
mileage = int(input("Enter the mileage of the vehicle: "))

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"Name of vehicle: {self.name}, Max Speed: {self.max_speed} km/h, Mileage: {self.mileage} km")

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

school_bus = Bus(name, max_speed, mileage)
school_bus.display_info()
print(school_bus.seating_capacity())