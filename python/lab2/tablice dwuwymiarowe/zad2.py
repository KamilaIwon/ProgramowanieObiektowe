
#wersja 1

wynik = []
while len(wynik) < 10:
    wynik.append(list(range(1,len(wynik)+2)))

print(wynik,"\n")

# wersja 2
tab = []
a = 1
suma_w_wierszu = 0
suma = 0
for i in range(1,11):
    row = []
    for j in range(1,i+1):
        row.append(a)
        suma_w_wierszu += a
        a += 1
    tab.append(row)
    print("suma wiersza nr ", i,": ",suma_w_wierszu)
    suma += suma_w_wierszu
    suma_w_wierszu = 0
print("suma całkowita: ", suma)
print(tab)