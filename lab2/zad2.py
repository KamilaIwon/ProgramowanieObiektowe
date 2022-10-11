
def mult(a):
    wynik = 1
    for x in a:
        wynik *= x
    return wynik

print("zadanie 1: ", mult([3, 5, 7]))
print("zadanie 1: ", mult(range(2,8,2)))

def mult_ints(a):
    wynik = 1
    for x in a:
        if isinstance(x, int):
            wynik *= x
    return wynik


print("zadanie 2: ", mult_ints([3, 3.14, 5, "abc", 7]))

# zad3


def multiply(*args):
    wynik = 1
    for x in args:
        wynik *= x
    return wynik

print("zadanie 3: ", multiply(3, 5, 7))

# zad4

def multiply_ints(*args):
    wynik = 1
    for x in args:
        if isinstance(x, int):
            wynik *= x
    return wynik


print("zadanie 4: ", multiply_ints(3, 3.14, 5, "abc", 7))

# zad5

def make_car(firma, model, **kwargs):
    dict = {"firma" : firma, "model" : model}
    dict.update(kwargs)
    return dict

print("zadanie 5: ", make_car("Kia","Picanto",kolor="cafe mocca", poj_silnika=900))
