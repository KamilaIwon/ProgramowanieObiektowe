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