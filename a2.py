class Rectangle:
    def __init__(self):
        self.a = int(input("Enter the length.\n"))
        self.b = int(input("Enter the breadth.\n"))
    def area(self):
        print("The area of the rectangle is", self.a * self.b)

rectangle = Rectangle()
rectangle.area()