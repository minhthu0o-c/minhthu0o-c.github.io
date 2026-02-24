class Person:
	def __init__(self, name, age, mom, dad):
		self.name = name
		self.age = age
		self.mom = mom
		self.dad = dad
	def showName(self):
		return f"Name: {self.name}"
	def showParent(self):
		return f"Father: {self.dad} \nMother: {self.mom}"

class Student(Person):
	def __init__(self, name, age, mom, dad, ID, note):
		super().__init__(name, age, mom, dad)
		self.ID = ID
		self.note = note
	def show(self):
		return f"Name: {self.name} \nAge: {self.age} \nID: {self.ID} \nNote: {self.note}"

name = input("Enter anen: ")
age = int(input("Enter age: "))
studentID = int(input("Enter ID: "))
note = input("Enter note: ")
ft = input("Enter father name: ")
mt = input("Enter mother name: ")

std1 = Student(name, age, mt, ft, studentID, note)

print("\nStudent info\n",std1.show())
print(f"Parent info \n{std1.showParent()}")