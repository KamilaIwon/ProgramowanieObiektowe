

def sum(a,b):
    c = []
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            c.append(a[i][j] + b[i][j])
    return c

print(sum([[1,1,1],[1,1,1]],[[1,1],[1,1]]))
print(sum([[1,2],[3,4]],[[1,2],[3,4]]))

X = [[9, 6],
    [3, 7],
    [2, 1]]

Y = [[1, 4, 6],
    [8, 2, 4]]

print(sum(X,Y))