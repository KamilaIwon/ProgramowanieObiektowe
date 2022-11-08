

class Student:
    student_name = 'Kamila Iwon'
    marks = [2,3,4,5]


print(f"imie: {getattr(Student, 'student_name')}")
print(f"ocenki: {getattr(Student, 'marks')}")
setattr(Student, 'student_name', 'Ola Iwon')
setattr(Student, 'marks', [1,2,3])
print(f"imie: {getattr(Student, 'student_name')}")
print(f"ocenki: {getattr(Student, 'marks')}")