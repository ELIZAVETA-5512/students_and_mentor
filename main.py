class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
 
    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade(self.grades)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return some_student
 
    def rate_lecturer(self, specific_lecturer, course, grade):
        if isinstance(specific_lecturer, Lecturer) \
                and course in specific_lecturer.courses_attached \
                and course in self.courses_in_progress \
                and 0 < grade <= 10:
 
            specific_lecturer.grades.append(grade)
 
        else:
            return 'Ошибка'
 
    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return average_grade(self.grades) < average_grade(other_student.grades)
        else:
            return None
 
# Класс преподавателей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
 
# Класс лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []
 
    def __str__(self):
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades)}'
        return some_lecturer
 
    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return average_grade(self.grades) < average_grade(other_lecturer.grades)
        else:
            return None
 
# Класс экспертов
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
 
    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer
 
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in specific_student.courses_in_progress:
 
            if course in specific_student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 

def average_grade(all_grades):
    if type(all_grades) is dict:
        amount_grades = []
        for grades in all_grades.values():
            for grade in grades:
                amount_grades.append(grade)
        return average_grade(amount_grades)
    elif type(all_grades) is list and all_grades[0] != None:
        average = round(sum(all_grades) / len(all_grades), 2)
        return average
    else:
        return "Ошибка! Оценки храняться не в словаре и не в списке, или список состоит из вложенных списков"

def average_course_grade(all_students, current_course):
    all_course_grades = []
    for current_student in all_students:
        if current_course in current_student.grades.keys():
            for every_grade in current_student.grades.get(current_course):
                all_course_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у студента {current_student.name} {current_student.surname}')
    return average_grade(all_course_grades)
 

def average_lecturers_grade(all_lecturers):
    all_lecturers_grades = []
    for current_lecturer in all_lecturers:
        for every_grade in current_lecturer.grades:
            all_lecturers_grades.append(every_grade)
    return average_grade(all_lecturers_grades)
 

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
student_no_2 = Student('Kat', 'NNN', '25')
student_no_2.courses_in_progress += ['Python']
student_list = [best_student, student_no_2]

lecturer_1 = Lecturer('Mike', 'Boops')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Some', 'Buddy')
lecturer_2.courses_attached += ['Python']


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
mentor_1 = Mentor('li', 'FFF')
mentor_1.courses_attached += ['Python']



cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(some_lecturer)
print(some_mentor)
print(some_student)
 
