
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_grade(self, self_grades: dict):
        summa = 0
        for course in self_grades.keys():
            summa += sum(self_grades[course])
        avg_grade = round(summa / len(self_grades.keys()), 1)
        return avg_grade

    def __eq__(self, other):
        student_1 = self.avg_grade(self.grades)
        student_2 = other.avg_grade(other.grades)
        return student_1 == student_2

    def __lt__(self, other):
        student_1 = self.avg_grade(self.grades)
        student_2 = other.avg_grade(other.grades)
        return student_1 < student_2

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and isinstance(self, Student):
            if course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print("Check if you are enrolled to the course and mentor leads the course")
        else:
            print("Check if you are student or mentor name is correct")

    def __str__(self):
        return f'Student:\nName: {self.name}\nSurname: {self.surname}\nAverage homework grade:{self.avg_grade(self.grades)}\nCourses in progress:{", ".join(self.courses_in_progress)}\nCompleted courses:{", ".join(self.finished_courses)}'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    from statistics import mean

    def avg_grade(self, self_grades: dict):
        summa = 0
        for course in self_grades.keys():
            summa += sum(self_grades[course])
        avg_grade = round(summa / len(self_grades.keys()), 1)
        return avg_grade

    def __eq__(self, other):
        lecturer_1 = self.avg_grade(self.grades)
        lecturer_2 = other.avg_grade(other.grades)
        return lecturer_1 == lecturer_2

    def __lt__(self, other):
        lecturer_1 = self.avg_grade(self.grades)
        lecturer_2 = other.avg_grade(other.grades)
        return lecturer_1 < lecturer_2


    def __str__(self):
        return f'Lecturer:\nName: {self.name}\nSurname: {self.surname}\nAverage grade:{self.avg_grade(self.grades)}'



class Reviewer(Mentor):

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Check the Name is in Students and course is correct...'

    def __str__(self):
        return f'Reviewer:\nName: {self.name}\nSurname: {self.surname}'


'''Average grade on certain course'''

student_list = []
lecturer_list = []
reviewer_list = []

def avg_course_grade(student_list, course):
    from statistics import mean
    student_count = 1
    grade_sum = 0
    for student in student_list:
        if course in student.grades:
            student_count +=1
            grade_sum += mean(student.grades[course])
        return grade_sum / student_count

def avg_course_grade_lect(lecturer_list, course):
    from statistics import mean
    lect_count = 1
    grade_sum = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            lect_count +=1
            grade_sum += mean(lecturer.grades[course])
        return grade_sum / lect_count


''' Students input'''

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_list.append(student_1)
student_1.courses_in_progress += ['Django', 'Python']
student_1.finished_courses = ['FrontEnd', 'BackEnd']

student_2 = Student('Manny', 'Fitzel', 'unsure')
student_list.append(student_2)
student_2.courses_in_progress += ['Django', 'FrontEnd']
student_2.finished_courses = ['FrontEnd', 'Python']

''' Reviewers input'''

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_list.append(reviewer_1)
reviewer_1.courses_attached += ['Python', 'Django']

reviewer_2 = Reviewer('Peter', 'Baker')
reviewer_list.append(reviewer_2)
reviewer_2.courses_attached += ['Python', 'Django']

'''Lecturers input'''

lecturer_1 = Lecturer('John', 'Dow')
lecturer_list.append(lecturer_1)
lecturer_1.courses_attached += ['Django']

lecturer_2 = Lecturer('Otto', 'Shtifelman')
lecturer_list.append(lecturer_2)
lecturer_2.courses_attached += ['Python', 'Django']

'''Evaluations'''

student_1.rate_lecturer(lecturer_1, 'Django', 10)
student_1.rate_lecturer(lecturer_2, 'Django', 20)
reviewer_1.rate_student(student_1, 'Django', 30)
reviewer_1.rate_student(student_2, 'Django', 20)

''' task 4 average grade'''

course = 'Django'
print(f'Avarage student grade on "{course}" is {avg_course_grade(student_list, course)}')
print(f'Avarage lecturer grade on "{course}" is {avg_course_grade(lecturer_list, course)}')

'''comparison based on average grade'''
if student_1 == student_2:
    sign = "equals"
elif student_1 < student_2:
    sign = 'lower'
else:
    sign = 'higher'
print(f"Student's {student_1.name} {student_1.surname} grade rating is {sign} than student's {student_2.name} {student_2.surname}")


if lecturer_1 == lecturer_2:
    sign = "equals"
elif lecturer_1 < lecturer_2:
    sign = 'lower'
else:
    sign = 'higher'
    print(f"Lecturer's {lecturer_1.name} {lecturer_1.surname} grade rating is {sign} than lecturer's {lecturer_2.name} {lecturer_2.surname}")


print()
print(student_1)
print()
print(lecturer_1)
print()
print(reviewer_1)

