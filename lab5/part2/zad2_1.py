
class MyClass():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input('podaj str ')

    def print_String(self):
        print(self.str1.upper())

str1 = MyClass()
str1.get_String()
str1.print_String()