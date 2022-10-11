
dict = {}

while True:
    a = input("Podaj liczbę: ")
    if not a:
        break
    else:
        if a not in dict.keys():
            dict.update({a:1})
        else:
            dict[a] += 1

print(dict)