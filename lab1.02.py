
# ex. 1a

def ileznaków(litera,znak):
    ile = 0
    for i in range(0, len(znak)):
        if litera == znak[i]:
            ile += 1
    return ile

def czyistnieje(lista):
    for i in range(0, len(lista)):
        k = 0
        for j in range(1, len(lista)):
            if lista[i] == lista[j]:
                k += 1
                if k > 1:
                    return True
    return False

def func1_a(znak):
    slownik = {}
    lista = []
    for i in range(0,len(znak)):
        if czyistnieje(lista) == False:
            lista.append(znak[i])
            slownik[znak[i]] = ileznaków(znak[i],znak)
    return slownik

znak = 'abca'
print(ileznaków(znak[0],znak))
print(func1_a(znak))


