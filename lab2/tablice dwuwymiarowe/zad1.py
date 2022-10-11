
tab = []
for i in range(1,4):
    row = []
    for j in range(1,11):
        row.append(j**i)
    tab.append(row)

print(tab)