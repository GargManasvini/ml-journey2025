class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks


    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")

s1 = Student('Manasvini Garg', 165, 99)
s1.display()