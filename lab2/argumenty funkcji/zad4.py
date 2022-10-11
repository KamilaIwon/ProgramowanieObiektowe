
def multiply_ints(*args):
    wynik = 1
    for x in args:
        if isinstance(x, int):
            wynik *= x
    return wynik


print("zadanie 4: ", multiply_ints(3, 3.14, 5, "abc", 7))