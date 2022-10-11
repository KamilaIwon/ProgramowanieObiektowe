import math

# zad1

matrix = []
for i in range(1,4):
    row = []
    for j in range(1,11):
        row.append(j**i)
    matrix.append(row)

print(matrix)

# zad2

x = 1
wynik = []
while len(wynik) < 10:
    wynik.append(list(range(1,len(wynik)+2)))

print(wynik)

tab = []
a = 1
for i in range(1,10):
    row = []
    for j in range(1,i):
        row.append(a)
        a += 1
    tab.append(row)

print(tab)