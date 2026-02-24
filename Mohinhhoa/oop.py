# class abc():
#     x = 10
# p = abc.x
# print(p)

# class student():
#     name = "John"
#     age = 20
#     ID_code = "S12345"
#     note = "Excellent student"
# p = student.name
# print(p)

name = input("Enter name: ")
age = int(input("Enter age: "))
ID_code = input("Enter ID code: ")
note = input("Enter note: ")

class students():
    def __init__(self, name, age, ID_code, note):
        self.name = name
        self.age = age
        self.ID_code = ID_code
        self.note = note
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, ID Code: {self.ID_code}, Note: {self.note}")
s = students(name, age, ID_code, note)
s.display()
