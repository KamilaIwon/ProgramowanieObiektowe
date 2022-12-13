
def multiply(*args):
    wynik = 1
    for x in args:
        wynik *= x
    return wynik

print("zadanie 3: ", multiply(3, 5, 7))