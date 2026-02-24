class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return capacity

    def fare(self, capacity):
        return self.seating_capacity(capacity) * 100

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def fare(self, capacity=50):
        amount = super().fare(capacity)
        amount += amount * 0.10
        return amount

name = input("Enter the name of the vehicle: ")
max_speed = int(input("Enter the max speed of the vehicle: "))
mileage = int(input("Enter the mileage of the vehicle: "))
capacity = int(input("Enter the seating capacity: "))

school_bus = Bus(name, max_speed, mileage)

print(f"Color: {school_bus.color}, Name: {school_bus.name}, Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")
print(f"Total Fare: {school_bus.fare(capacity)}")