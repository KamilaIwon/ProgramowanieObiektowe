
class MyClass:
    def __init__(self):
        self.data = 123

def func(klasa):
    x = klasa()
    print(dir(x))

func(MyClass)