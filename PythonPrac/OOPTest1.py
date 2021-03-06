__author__ = 'Esmidth'


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print("Current Value = %s" % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __mul__(self, other):
        self.data = self.data * other

a = ThirdClass("abc")
a.display()

b = a + 'xyz'
b.display()

a * 3
a.display()