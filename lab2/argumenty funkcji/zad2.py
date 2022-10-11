
def mult_ints(a):
    wynik = 1
    for x in a:
        if isinstance(x, int):
            wynik *= x
    return wynik


print("zadanie 2: ", mult_ints([3, 3.14, 5, "abc", 7]))
