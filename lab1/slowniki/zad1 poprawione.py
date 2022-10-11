
# ex.1a

def func1a (a):
    dict = {}
    for x in a:
        if x not in dict.keys():
            dict.update({x:1})
        else:
            dict[x] += 1
    return dict

# ex.1b

def func1b (a):
    dict = {}
    for x in a:
        if x.isalpha():
            if x not in dict.keys():
                dict.update({x:1})
            else:
                dict[x] += 1
    return dict

# ex.1c

def func1c (a):
    dict = {}
    a = a.lower()
    for x in a:
        if x.isalpha():
            if x not in dict.keys():
                dict.update({x:1})
            else:
                dict[x] += 1
    return dict

# ex.1d

def func1d(a):
    a = a.lower()
    dict = {}
    i = 0
    for x in a:
        if x.isalpha():
            if x not in dict.keys():
                dict.update({x: 1})
            else:
                dict[x] += 1
        else:
            i += 1
    if len(a) == i:
        return "Brak liter"
    return max(dict, key=dict.get)

# czytanie ze standardowego wejścia

a = input("Podaj łańcuch znaków: ")
print(func1a(a))
print(func1b(a))
print(func1c(a))
print(func1d(a))

# czytanie z pliku

f = open("tekst.txt")
c = f.read()
print(func1a(c))
print(func1b(c))
print(func1c(c))
print(func1d(c))
f.close()


