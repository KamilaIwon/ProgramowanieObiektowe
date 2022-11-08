
class MyClass:
    def __init__(self):
        self.data = 123


for name in MyClass.__dict__:
    print(name)