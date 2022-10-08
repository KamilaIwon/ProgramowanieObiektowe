
# ex. 1a


def ileznaków(litera, znak):
    ile = 0
    for i in range(0, len(znak)):
        if litera == znak[i]:
            ile += 1
    return ile


def czyistnieje(znak, lista):
    for x in lista:
        if x == znak:
            return True
    return False


def func1_a(znak):
    slownik = {}
    lista = []
    for i in range(0, len(znak)):
        if not czyistnieje(znak[i], lista):
            lista.append(znak[i])
            slownik[znak[i]] = ileznaków(znak[i], znak)
    return slownik


znak = 'abca'
print(ileznaków(znak[0], znak))


# ex.1b

def func1_b(znak):
    slownik = {}
    lista = []
    for i in range(0, len(znak)):
        if znak[i].isalpha():
            if not czyistnieje(znak[i], lista):
                lista.append(znak[i])
                slownik[znak[i]] = ileznaków(znak[i], znak)
    return slownik


# ex.1c


def func1_c(znak):
    slownik = {}
    lista = []
    znak = znak.lower()
    for i in range(0, len(znak)):
        if znak[i].isalpha():
            if not czyistnieje(znak[i], lista):
                lista.append(znak[i])
            slownik[znak[i]] = ileznaków(znak[i], znak)
    return slownik


# ex. 1d

def func1_d(znak):
    ile = 0
    znak1 = ''
    for i in range(0, len(znak)):
        k = 0
        if znak[i].isalpha():
            for j in range(0, len(znak)):
                if znak[i] == znak[j]:
                    k += 1
            if ile < k:
                ile = k
                znak1 = znak[i]
    return znak1


lancuch = input("wprowadz dowolny łańcuch znaków: ")
lancuch1 = open('tekst.txt')
print('zadanie 1a: ', func1_a(lancuch))
print('zadanie 1b: ', func1_b(lancuch))
print('zadanie 1c: ', func1_c(lancuch1.read()))
lancuch1 = open('tekst.txt')
print('zadanie 1d: ', func1_d(lancuch1.read()))
