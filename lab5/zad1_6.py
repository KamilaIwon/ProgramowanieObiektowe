
class Student:
    def __init__(self, nazwa_ucznia, klasa_ucznia, student_id):
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id

    def student_data(self,*dodatek):
        print(self.student_id)
        if 'nazwa_ucznia' in dodatek:
            print(self.nazwa_ucznia)
        if 'klasa_ucznia' in dodatek:
            print(self.klasa_ucznia)

numer1 = Student('Kamila','3c',12345)
numer1.student_data()
numer1.student_data('klasa_ucznia')