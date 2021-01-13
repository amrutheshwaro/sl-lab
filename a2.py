#Create a class rectangle
class Rectangle:
    #Constructor to initialise the dimensions
    def __init__(self):
        self.a = int(input("Enter the length.\n"))
        self.b = int(input("Enter the breadth.\n"))

    #Function to compute the area of the rectangle
    def area(self):
        print("The area of the rectangle is", self.a * self.b)

#Create objects of the class and print the area
rectangle = Rectangle()
rectangle.area()