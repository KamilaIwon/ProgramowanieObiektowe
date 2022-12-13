
Y = [[1, 4, 6],[8, 2, 4]]

def transp(a):

    #tworzymy macierz zerowa:

    C = []
    while len(C) < len(a[0]):
        C.append([])
        while len(C[-1]) < len(a):
            C[-1].append(0)

    for i in range(len(a)):
        for j in range(len(a[0])):
            C[j][i] = a[i][j]
    return C


print(transp(Y))
