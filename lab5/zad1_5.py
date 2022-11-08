
class Student:
    def __init__(self, nazwa_ucznia, klasa_ucznia, student_id):
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id


numer1 = Student('Kamila','3c',12345)
print(numer1.nazwa_ucznia)
print(numer1.klasa_ucznia)
print(numer1.student_id)
# print(getattr(numer1,'student_id'))
