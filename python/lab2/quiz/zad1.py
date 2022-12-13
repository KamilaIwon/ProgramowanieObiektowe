
def func(a, b=4, c=5):
    print(a, b, c)


func(1, 2)
# nadpisuje wartości


def func1(a, b, c=5):
    print(a, b, c)


func1(1, c=3, b=2 )

#  nadpisuje wartości


def func2(a, *args):
    print(a, args)


func2(1, 2, 3)
# zamienia w krotki


def func3(a, **kwargs):
    print(a, kwargs)


func3(a=1, c=3, b=2)

# zamienia w słownik


def func4(a, b, c=3, d=4):
    print(a, b, c, d)


func4(1, *(5, 6))
