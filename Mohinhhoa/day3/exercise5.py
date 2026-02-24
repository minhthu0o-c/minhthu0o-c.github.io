class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

name = input("Enter the name of the vehicle: ")
max_speed = int(input("Enter the max speed of the vehicle: "))
mileage = int(input("Enter the mileage of the vehicle: "))

vehicle = Car(name, max_speed, mileage)

print(f"Color: {vehicle.color}, Name: {vehicle.name}, Speed: {vehicle.max_speed}, Mileage: {vehicle.mileage}")