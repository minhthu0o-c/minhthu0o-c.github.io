class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

name = input("Enter the name of the vehicle: ")
max_speed = int(input("Enter the max speed of the vehicle: "))
mileage = int(input("Enter the mileage of the vehicle: "))

school_bus = Bus(name, max_speed, mileage)

print(type(school_bus))