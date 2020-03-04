import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Circle:

    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def perimetr(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*self.radius**2
    
    def plusvector(self, vector):
        self.center.x = self.center.x + vector.x
        self.center.y = self.center.y + vector.y
        return self.center


def main():
    p = Point(2, 2)

    print(Point.get_x(p)+Point.get_y(p))
    circ = Circle(5, p)

    print(Circle.area(circ))
    print(Circle.perimetr(circ))
    print(circ.center.x)
    Circle.plusvector(circ, p)
    print(circ.center.x)
    print(circ.center.y)

        



main()
