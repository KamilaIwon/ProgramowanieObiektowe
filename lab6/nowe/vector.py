import math

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # print
    def __repr__(self):
        return f'[pierwsza wspolrzedna wektora: {self.a}' \
               f' \n druga wspolrzedna wektora: {self.b}]'

    def __str__(self):
        return f'[{self.a},{self.b}]'

    # dodawanie wektorow
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)

    # odejmowanie wektorow
    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)

    # dlugosc wektora
    def __len__(self):
        return math.pow(self.a*self.a + self.b*self.b, 0.5)

    def __mul__(self, other):
        return self.a * other.a + self.b * other.b

    def inner(self, other):
        return Vector(self.a * other, self.b * other)

    def __getitem__(self, item):
        if item == 1:
            return self.a
        elif item == 2:
            return self.b
        else:
            return None

    def __eq__(self, other):
        if self.a == other.b and self.b == other.b:
            return True
        return False

vec = Vector(1,2)
vec2 = Vector(3,-5)
print(vec.inner(5))
print(vec.__mul__(vec2))
print(vec.__getitem__(2))