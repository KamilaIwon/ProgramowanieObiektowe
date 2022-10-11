

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