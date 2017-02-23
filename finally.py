import math
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def retLength(self):
        return self.length
    def retWidth(self):
        return self.width
    def retPer(self):
        return self.width * 2 + self.length * 2
    def retArea(self):
        return self.width * self.length
    def retDig(self):
        x = self.width * self.width + self.length * self.length
        return math.sqrt(x)
class Cube(Rectangle):
    def __init__(self, length, width, height):
        super(Cube, self).__init__(length, width)
        self. height = height
    def Height(self):
        return self.height
    def Volume(self):
        return self.height * self.width * self.length
    def Length(self):
        return self.height * 4 + self.width * 4 + self.length * 4
    def List(self):
        areas = []

        for i in range(1, 7):

            if i == 1 or i == 2:
                areas.append(self.height * self.length)
            if i == 3 or i == 4:
                areas.append(self.height * self.width)
            if i == 5 or i == 6:
                areas.append(self.width * self.length)
        return areas




rect = Rectangle(3,4)
cube = Cube(3, 4, 5)
print rect.retLength()
print rect.retWidth()
print rect.retPer()
print rect.retArea()
print rect.retDig()
print cube.Height()
print cube.Volume()
print cube.Length()
print cube.List()
