
# zadanie1

lista = [x for x in range(1, 11)]
lista = [x*2 for x in range(0, 11)]
lista = [x**2 for x in range(1, 11)]
lista = [x*0 for x in range(1, 11)]
lista = [x % 2 for x in range(0, 10)]
lista = [x % 5 for x in range(0, 10)]
print(lista)

# zadanie2
lista2 = []

x = 0

while x < 11:
    lista2.append(x)
    x += 1

print(lista2)

lista2 = []
x = 0
while x < 11:
     lista2.append(x*2)
     x += 1
print(lista2)


lista2 = []
x = 1
while x < 11:
     lista2.append(x**2)
     x += 1
print(lista2)

lista2 = []
x = 1
while x < 11:
     lista2.append(x * 0)
     x += 1
print(lista2)

lista2 = []
x = 0
while x < 10:
     lista2.append(x % 2)
     x += 1
print(lista2)

lista2 = []
x = 0
while x < 10:
    lista2.append(x%5)
    x += 1
print(lista2)

# zadanie3
lista3 = [1, 2, -5, -7, -8, 9]


def ile_ujemnych(a):
    i = 0
    for x in range(0, len(a)):
        if a[x] < 0:
            i += 1
    return i


print('zadanie 3:', ile_ujemnych(lista3))

# zadanie4

lista4 = [1, 5, 4]

def iloczyn(a):
    i = 1
    for x in range(0, len(a)):
            i *= a[x]
    return i


print('zadanie 4:', iloczyn(lista4))

# zadanie5
lista5 = [2, 8, 5, 6]


def minmax(lista):
   min = 0
   max = 0
   for i in lista:
       if min > i:
           min = i
   for i in lista:
       if max < i:
           max = i
   return(min, max)


print('zadanie5:', minmax(lista5))
print(type(minmax(lista5)))


# zad6

lista6 = [1, 4, 16, 9, 9, 7, 4, 9, 11]


def func(lista):
    suma = 0
    for i in range(0, len(lista)):
        if i % 2 == 0:
            suma += lista[i]
        else:
            suma -= lista[i]
    return suma


print('zadanie6:', func(lista6))

#zad7

'''
def czyNaLiscie (lista, liczba):
    for x in lista:
        if x == liczba:
            return 0
    return 1


i = 0
lista7 = []
while i < 10:
    liczba = int(input("Wprowadź liczbę do listy:"))
    if czyNaLiscie(lista7, liczba) == 1:
        lista7.append(liczba)
        i += 1
    else:
        print("Podana liczba juz istnieje, spróbuj jeszcze raz")

print('zadanie7:', lista7)
'''
#zadanie8

lista8 = []


def func8(lista):
    for x in range(2,10001):
        lista.append(x)
    for x in range (2,101):
        for y in lista:
            if y % x == 0 and y != x:
                lista.remove(y)

func8(lista8)
# print("zadanie8: ", lista8)

# zadanie9a

lista9_a = [1, 2, 3, 4, 5]


def func9_a(lista):
    temp = lista[0]
    lista[0] = lista[-1]
    lista[-1]=temp
    return lista


print('zadanie 9a:',func9_a(lista9_a))


# zad9b
lista9_b = [1, 4, 9, 16, 25]


def func9_b(lista):
    i = len(lista) - 1
    while i > 0:
        temp = lista[i]
        lista[i] = lista[i-1]
        lista[i-1] = temp
        i -= 1
    return lista


print('zadanie 9b:',func9_b(lista9_b))


# zad9c
lista9_c = [1, 2, 3, 4, 5]


def func9_c (lista):
    for x in range(0,len(lista)):
        if lista[x]%2==0:
            lista[x] = 0
    return lista


print('zadanie 9c:', func9_c(lista9_c))

# zad9d

lista9_d = [1, 8, 3, 5, 7]

'''
wersja pierwsza

def func9_d(lista):
    i = 1
    temp = lista[i]
    for i in range(1, len(lista)-1):
        if lista[i - 1] > lista[i + 1]:
            lista[i] = lista[i - 1]
        else:
            lista[i] = lista[i + 1]

    return lista
    
'''
# wersja druga


def func9_d(lista):
    temp = []
    for x in lista:
        temp.append(x)

    for i in range(1,len(lista)-1):
        if lista[i-1] > lista[i+1]:
            temp[i] = lista[i-1]
        else:
            temp[i] = lista[i+1]
    i = 0
    for x in temp:
        lista[i] = x
        i += 1

    return lista


print('zadanie 9d:', func9_d(lista9_d))
print(lista9_d)

# zadanie9e
lista9_e_a = [1, 2, 3, 4, 5]
lista9_e_b = [1, 2, 3, 4, 5, 6]


def func9_e(lista):
    if len(lista) % 2 != 0:
        znak = int(len(lista)/2)
        lista.remove(lista[znak])
    else:
        znak = int(len(lista) / 2)
        lista.remove(lista[znak])
        lista.remove(lista[znak-1])

    return lista


print('zadanie 9e:', func9_e(lista9_e_a))
print('zadanie 9e:', func9_e(lista9_e_b))

# zadanie9_f

list9_f = [1, 2, 3, 4, 8, 6]


def func9_f(list):
    ileparzystych = 0
    ilenieparzystych = 0
    parzyste = []
    nieparzyste = []
    for x in list:
        if x % 2 == 0:
            ileparzystych += 1
            parzyste.append(x)
        else:
            ilenieparzystych += 1
            nieparzyste.append(x)
    i = 0
    k = 0

    while i < len(list):
        while i < ileparzystych:
            list[i] = parzyste[i]
            i += 1
        list[i] = nieparzyste[k]
        i += 1
        k += 1
    return list


print('zadanie 9_f', func9_f(list9_f))
print(list9_f)

# zadanie9g

lista9_g = [1, 3, 45, 8, 46, 56, 100]


def func9_g(lista):
    if lista[0] > lista[1]:
        pierwsza = lista[0]
        druga = lista[1]
    else:
        pierwsza = lista[1]
        druga = lista[0]

    for x in lista:
        if x > druga:
            if x > pierwsza:
                druga = pierwsza
                pierwsza = x
            else:
                druga = x

    return druga


print('zadanie 9g:', func9_g(lista9_g))

# zadanie9_h

lista9_h_a = [1, 2, 3, 4, 5, 6]
lista9_h_b = [1, 2, 3, 4, 6, 5]


def func9_h(lista):
    for i in range(1, len(lista)):
        if lista[i] < lista[i-1]:
            return False

    return True

print('zadanie 9h:', func9_h(lista9_h_a))
print('zadanie 9h:', func9_h(lista9_h_b))

# zadanie9_i

lista9_i_a = [1, 2, 5, 4, 6, 6]
lista9_i_b = [1, 2, 4, 8, 6, 5]

def func9_i (lista):
    for i in range(1, len(lista)):
        if lista[i] == lista[i-1]:
            return False

    return True


print('zadanie 9i:', func9_i(lista9_i_a))
print('zadanie 9i:', func9_i(lista9_i_b))

# zadanie9_j
lista9_j_a = [1, 2, 5, 4, 9, 6]
lista9_j_b = [1, 5, 4, 8, 6, 5]


def func9_j (lista):
    for x in lista:
        i = 0
        for y in lista:
            if x == y:
                i += 1
                if i > 1:
                    return False
    return True


print('zadanie 9j:', func9_j(lista9_j_a))
print('zadanie 9j:', func9_j(lista9_j_b))

# zadanie10

a = [1, 2, 3]
b = [4, 5, 6]
c = [1, 2, 3]


def equals(a, b):

    if len(a) != len(b):
        return 0
    else:
        for x in range(0, len(a)):
            if a[x] != b[x]:
                return False

    return True


print(equals(a, c))
