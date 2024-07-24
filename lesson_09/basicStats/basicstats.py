import statistics

class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        return self._grade

def basic_stats(student_object_list):
    grade_list = []
    for student in student_object_list:
        grade_list.append(student.get_grade())

    student_mean = statistics.mean(grade_list)
    student_median = statistics.median(grade_list)
    student_mode = statistics.mode(grade_list)
    stats = (f'{student_mean}', f'{student_median}', f'{student_mode}')

    return stats

student_1 = Student('Joe', 86)
student_2 = Student('carol', 90)
student_3 = Student('Dan', 78)
student_4 = Student('Dant', 78)

student_list = [student_1, student_2, student_3, student_4]

print(basic_stats(student_list))