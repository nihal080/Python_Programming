class Circle:
    PI=3.14
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        print("Area of Circle",self.PI*self.radius*self.radius)
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        print("Area of Rectangle",self.length*self.width)

def area(shape):
    shape.calculate_area()
cir=Circle(5)
rect=Rectangle(10,5)

area(cir)
area(rect)
