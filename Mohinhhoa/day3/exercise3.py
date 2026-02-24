name = input("Enter the name of the vehicle: ")
max_speed = int(input("Enter the max speed of the vehicle: "))
mileage = int(input("Enter the mileage of the vehicle: "))
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def hien_thi_thong_tin(self):
        print(f"Name of vehicle: {self.name}, Max Speed: {self.max_speed} km/h, Mileage: {self.mileage} km")

class Bus(Vehicle):
    pass 

school_bus = Bus(name, max_speed, mileage)
school_bus.hien_thi_thong_tin()