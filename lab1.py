
#zad1

lista = [ x for x in range (1,11)]
lista = [ x*2 for x in range (0,11)]
lista = [ x**2 for x in range (1,11)]
lista = [ x*0 for x in range (1,11)]
lista = [ x%2 for x in range (0,10)]
lista = [ x%5 for x in range (0,10)]
print(lista)

#zad2
lista2 = []

x = 0

while x < 11:
    lista2.append(x)
    x+=1

print(lista2)

lista2 = []
x = 0
while x < 11:
     lista2.append(x*2)
     x+=1
print(lista2)


lista2 = []
x = 1
while x < 11:
     lista2.append(x**2)
     x+=1
print(lista2)

lista2 = []
x = 1
while x < 11:
     lista2.append(x*0)
     x+=1
print(lista2)

lista2 = []
x = 0
while x < 10:
     lista2.append(x%2)
     x+=1
print(lista2)

lista2 = []
x = 0
while x < 10:
    lista2.append(x%5)
    x+=1
print(lista2)

#zad3
lista3 = [1,2,-5,-7,-8,9]
def ile_ujemnych (a):
    i = 0
    for x in range (0,len(a)):
        if(a[x]<0):
            i+=1
    return i

print('zadanie 3:',ile_ujemnych(lista3))

#zad4

lista4 = [1,5,4]
def iloczyn (a):
    i = 1
    for x in range (0,len(a)):
            i*=a[x]
    return i
print('zadanie 4:',iloczyn(lista4))

#zad5
lista5 = [2,8,5,6]
def minmax(lista):
   min = 0
   max = 0
   for i in lista:
       if min> i:
           min = i
   for i in lista:
       if max< i:
           max = i
   return(min,max)

print('zadanie5:',minmax(lista5))
print(type(minmax(lista5)))

#zad6

lista6 = [1,2,3,4]
def func(lista):
    i = 0
    for x in lista:
        if x<0:
            i+=x
        else:
            i-=x
    return i

print('zadanie6:',func(lista6))

#zad7
lista7 = []

def func7(lista):
    for x in lista:
        liczba = input()
#zad10
a = [1,2,3]
b = [4,5,6]
c = [1,2,3]

def equals(a,b):

    if len(a) != len(b):
        return 0
    else:
        for x in range (0,len(a)):
            if a[x]!= b[x] :
                return 0

    return 1


print(equals(a,c))