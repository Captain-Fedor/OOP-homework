
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_grade(self, self_grades: dict):
        sum = 0
        count = 0
        for course, grade in self_grades.items():
            for i in grade:
                sum += i
                count += 1
        avg_grade = round(sum / count, 1)
        return avg_grade

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

    def student_compare(self, student, course):
        if course in self.grades and course in student.grades:
            if sum(self.grades[course])/len(self.grades[course]) > sum(student.grades[course])/len(student.grades[course]):
                rate_high = f'{self.surname} {self.name}'
                rate_low = f'{student.surname} {student.name}'
            elif sum(self.grades[course])/len(self.grades[course]) < sum(student.grades[course])/len(student.grades[course]):
                rate_low = f'{self.surname} {self.name}'
                rate_high = f'{student.surname} {student.name}'
            else:
                return f'Students {self.name} {self.surname} and {student.name} {student.surname} have the same rating'
        else:
            return f'Please check that {self.name} {self.surname} and {student.name} {student.surname} are on the same course'
        return f'Student {rate_high} has higher rating than student {rate_low}'


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
        sum = 0
        count = 0
        for course, grade in self_grades.items():
            for i in grade:
                sum += i
                count += 1
        avg_grade = round(sum / count, 1)
        return avg_grade

    def lecturer_compare(self, lecturer, course):
        if course in self.grades and course in lecturer.grades:
            if sum(self.grades[course])/len(self.grades[course]) > sum(lecturer.grades[course])/len(lecturer.grades[course]):
                rate_high = f'{self.surname} {self.name}'
                rate_low = f'{lecturer.surname} {lecturer.name}'
            elif sum(self.grades[course])/len(self.grades[course]) < sum(lecturer.grades[course])/len(lecturer.grades[course]):
                rate_low = f'{self.surname} {self.name}'
                rate_high = f'{lecturer.surname} {lecturer.name}'
            else:
                return f'Lecturers {self.name} {self.surname} and {lecturer.name} {lecturer.surname} have the same rating'
        else:
            return f'Please check that {self.name} {self.surname} and {lecturer.name} {lecturer.surname} are on the same course'
        return f'Lecturer {rate_high} has higher rating than lecturer {rate_low}'




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
reviewer_1.rate_student(student_2, 'Django', 50)

''' task 4 average grade'''

course = 'Django'
print(f'Avarage student grade on "{course}" is {avg_course_grade(student_list, course)}')
print(f'Avarage lecturer grade on "{course}" is {avg_course_grade(lecturer_list, course)}')

'''comparison based on average grade'''

print(lecturer_1.lecturer_compare(lecturer_2, 'Django'))
print(student_1.student_compare(student_2, 'Django'))
print()

print(student_1)
print()
print(lecturer_1)
print()
print(reviewer_1)