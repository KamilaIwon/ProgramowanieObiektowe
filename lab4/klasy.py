
# skracanie ułamka
def nwd(a: int, b: int) -> int:
    if b == 0:
        return a
    return nwd(b, a % b)


class Wymierna:
    def __init__(self, p: int = 0, q: int = 1):
        if type(p) != int:
            p = int(p)
        if type(q) != int:
            q = int(q)
        if q < 0:
            p = -p
            q = -q

        nwdValue = nwd(q, p)

        if nwdValue != 1:
            q = int(q / nwdValue)
            p = int(p / nwdValue)

        self.licznik = p
        self.mianownik = q

    def get_licznik(self):
        return self.licznik

    def get_mianownik(self):
        return self.mianownik

    def __repr__(self):
        return f'{self.licznik} / {self.mianownik}'

    def __float__(self) -> float:
        return self.licznik / self.mianownik

# dodawanie
    def __add__(self, other):
        iloczyn_m = self.mianownik * other.mianownik
        if iloczyn_m < 0:
            iloczyn_m = -iloczyn_m

        self.licznik *= int(iloczyn_m / self.mianownik)
        other.licznik *= int(iloczyn_m / other.mianownik)

        return Wymierna(self.licznik + other.licznik, iloczyn_m)

# odejmowanie

    def __sub__(self, other):
        return self + Wymierna(-other.licznik, other.mianownik)

# czy takie same

    def __eq__(self, other):
        if self.licznik == other.licznik and self.mianownik == other.mianownik:
            return True
        return False

# czy nie są równe
    def __ne__(self, other):
        if self.licznik == other.licznik and self.mianownik == other.mianownik:
            return False
        return True

# czy a < b
    def __lt__(self, other):
        return self.licznik / self.mianownik < other.licznik / other.mianownik

# czy a <= b
    def __le__(self, other):
        return self.licznik / self.mianownik <= other.licznik / other.mianownik

# czy a > b
    def __gt__(self, other):
        return self.licznik / self.mianownik > other.licznik / other.mianownik

# czy a >= b
    def __ge__(self, other):
        return self.licznik / self.mianownik >= other.licznik / other.mianownik
# mnozenie
    def __mul__(self, other):
        return Wymierna(self.licznik * other.licznik, self.mianownik * other.mianownik)
# dzielenie
    def __div__(self, other):
        return Wymierna(self.licznik * other.mianownik, self.mianownik * other.licznik)

    def eq2(self, other):
        return not (self > other or self < other)
a = Wymierna(4,1)
b = Wymierna(8,2)
'''
print(b.get_licznik())
print(b.get_mianownik())
print(b.__repr__())
print(b.__float__())
print(a.__add__(b))
print(a.__sub__(b))

'''
print(a.__repr__())
#print(a.__eq__(b))
print(a.__ne__(b))
print(a.__lt__(b))
print(a.__le__(b))
print(a.__gt__(b))
print(a.__ge__(b))
print(a.__mul__(b))
print(a.__div__(b))
print(a.eq2(b))

