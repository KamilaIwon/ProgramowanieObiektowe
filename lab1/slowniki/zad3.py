
# ex.3

dict = {}

a = open("tekst.txt")
b = a.read()

b = b.lower()

for x in b:
    if x.isalpha():
        if x not in dict:
            dict.update({x:1})
        else:
            dict[x] += 1

print(dict)
a.close()