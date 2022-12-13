
class Student:
    def __init__(self, imie: str, nazwisko: str, *args):
        self.imie = imie
        self.nazwisko = nazwisko
        self.liczba_quizow = len(args)
        try:
            suma = 0
            for i in args:
                suma += i
            self.srednia_quizow = suma / self.liczba_quizow
        except ZeroDivisionError:
            self.srednia_quizow = 0


    def add_quiz(self, score):
        self.srednia_quizow = ((self.srednia_quizow * self.liczba_quizow) + score) / (self.liczba_quizow + 1)
        self.liczba_quizow += 1

    def get_total_score(self):
        return self.srednia_quizow * self.liczba_quizow

    def get_average_score(self):
        return self.srednia_quizow

    def get_name(self, imie):
        self.imie = imie


uczen1 = Student('Kamila','Iwon')
uczen1.get_name('Ania')
print(uczen1.imie)
uczen1.add_quiz(20)
uczen1.add_quiz(10)
print(uczen1.liczba_quizow)
print(uczen1.get_total_score())
print(uczen1.get_average_score())