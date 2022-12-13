
X = [[9, 6],[3, 7],[2, 1]]
Y = [[1, 4, 6],[8, 2, 4]]


def product(a,b):
    # tworzymy macierz zerowa o dobrych wymiarach
    C = []
    while len(C) < len(a):
        C.append([])
        while len(C[-1]) < len(b[0]):
            C[-1].append(0)

    # mnozymy i zamieniamy w macierzy zerowej
    # wiersz a
    for i in range(len(a)):

        # kolumna b
        for j in range(len(b[0])):

            # wiersz a
            for k in range(len(b)):
                C[i][j] += a[i][k] * b[k][j]
    return C


print(product(X, Y))

# to samo, ale w trudniejszy sposób
def product1(A, B):
    if len(A[0]) != len(B):
        return False
    result = [[sum(A * B for A, B in zip(X_row, Y_col))
                    for Y_col in zip(*Y)]
                        for X_row in X]
    return result

print(product1(X, Y))
