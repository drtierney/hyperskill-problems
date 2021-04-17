class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = name[0] + last_name + birth_year


s_name, s_last_name, s_birth_year = [input() for n in range(3)]

new_student = Student(s_name, s_last_name, s_birth_year)
print(new_student.student_id)
