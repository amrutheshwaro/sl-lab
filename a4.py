class Student:
    def __init__(self):
        self.name = input("Enter the name of the student.\n")
        self.age = int(input("Enter the age of the student.\n"))
    def accept(self):
        self.marks = list(map(int, input("Enter the marks of 3 subjects.\n").strip().split()))
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks of three subjects:", self.marks)

student = Student()
student.accept()
student.display()