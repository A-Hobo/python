import datetime
class MyNumbers(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def Add(self):
        return self.a + self.b + self.c
    def Multiply(self):
        return self.a * self.b * self.c
    def Middle(self):
        if self.a < self.c and self.a > self.b or self.a > self.c and self.a < self.b:
            return self.a
        if self.c < self.a and self.c > self.b or self.c < self.b and self.c > self.a:
            return self.c
        if self.b < self.c and self.b > self.a or self.b > self.c and self.b < self.a:
            return self.b
        else:
            return False
    def Largest(self):
        return max(self.a, self.b, self.c)
    def Smallest(self):
        return min(self.a, self.b, self.c)
    def Average(self):
        return (self.a + self.b + self.c) / 3
    def Triangle(self):
        if self.a == self.b and self.b == self.c:
            return "Equilateral"
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isoscles"
        else:
            return "Scalene"
    def __str__(self):
        return "MyNumbers contains the following numbers: %s, %s and %s" % (self.a, self.b, self.c)
    def __add__(self, other):
        list1 = []
        a1 = self.a + other.a
        b1 = self.b + other.b
        c1 = self.c + other.c
        list1.append(a1)
        list1.append(b1)
        list1.append(c1)
        return list1
    def __sub__(self,other):
        list1 = []
        a1 = self.a - other.a
        b1 = self.b - other.b
        c1 = self.c - other.c
        list1.append(a1)
        list1.append(b1)
        list1.append(c1)
        return list1
    def IsMinute(self):
        time = datetime.datetime.now()
        if self.a == time.minute or self.b == time.minute or self.c == time.minute:
            return True
        else:
            return False
num1 = MyNumbers(5, 6, 10)
num2 = MyNumbers(4, 5, 6)

print num1.Add()
print num1.Multiply()
print num1.Middle()
print num1.Largest()
print num1.Smallest()
print num1.Average()
print num1.Triangle()
print num1
print num1 + num2
print num1 - num2
print num1.IsMinute()
