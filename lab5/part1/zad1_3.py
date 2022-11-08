
class MyClass:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek =wiek

student = MyClass('Kamila','Iwon',20)
print(student.__dict__)