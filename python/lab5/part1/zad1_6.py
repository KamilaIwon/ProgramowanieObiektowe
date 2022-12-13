def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name:  {kwargs['student_name']}")

    if 'student_class' in kwargs:
        print(f"\nStudent Name:  {kwargs['student_name']}")
        print(f"Student Class:  {kwargs['student_class']}")


student_data(student_id='12345', student_name='Kamila')

student_data(student_id='123456', student_name='Kamila', student_class='3c')