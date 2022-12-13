
def mult(a):
    wynik = 1
    for x in a:
        wynik *= x
    return wynik

print("zadanie 1: ", mult([3, 5, 7]))
print("zadanie 1: ", mult(range(2,8,2)))