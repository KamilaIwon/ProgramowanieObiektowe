
def mult(a,x):
    for n in range(0, len(a)):
        for m in range(0, len(a[0])):
            a[n][m] *= x
    return a

print(mult([[1,2],[3,4]],3))