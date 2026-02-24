# 1. Get input values from the user via the keyboard
max_speed = int(input("Enter the max speed of the vehicle: "))
mileage = int(input("Enter the mileage of the vehicle: "))

# 2. Define the vehicle class structure
class vehicle():
    # Constructor method to initialize the object's attributes
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed  # Assign the max_speed attribute
        self.mileage = mileage      # Assign the mileage attribute

# 3. Display the information entered by the user
print(f"Max speed: {max_speed}, Mileage: {mileage}")