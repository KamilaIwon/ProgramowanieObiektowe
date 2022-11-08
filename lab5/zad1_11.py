
class Student:
    pass

student1 = Student()
student2 = Student()
student1.student_id = "123"
student1.student_name = "Kamila Iwon"
student2.student_id = "345"
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr}  {getattr(student, attr)}')