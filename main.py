class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def avg_grade(self):
        number_grades = 0
        sum_grades = 0
        for course in self.grades:
            number_grades += len(self.grades[course])
            sum_grades += sum(self.grades[course])
        if number_grades != 0:
            return round(sum_grades / number_grades, 1)
        else:
            return 0

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __ne__(self, other):
        return self.avg_grade() != other.avg_grade()

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.avg_grade()}'
                f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"
                f"\nЗавершенные курсы: {', '.join(self.finished_courses)}")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        print('Ошибка, лекторы не выставляют оценок')

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python','C++']
best_student.finished_courses += ['Java', 'Введение в программирование']
second_student = Student('Sharon', 'Brown', 'your_gender')
second_student.courses_in_progress += ['Python', 'Java']
second_student.finished_courses += ['Pascal', 'Введение в программирование']
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'C++']
first_lecturer = Lecturer('Ralph', 'Ruiz')
first_lecturer.courses_attached += ['Python', 'Java']
second_lecturer = Lecturer('Stacey', 'Douglas')
second_lecturer.courses_attached += ['C++','Python','Pascal']
first_reviewer = Reviewer('Ronald', 'Johnson')
first_reviewer.courses_attached += ['Python', 'C++']
second_reviewer = Reviewer('Lester', 'Soto')
first_reviewer.courses_attached += ['C++', 'Java', 'Pascal']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'C++', 7)
cool_mentor.rate_hw(second_student, 'Python', 4)
cool_mentor.rate_hw(second_student, 'C++', 8)
first_reviewer.rate_hw(best_student, 'Python', 2)
first_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(best_student, 'C++', 10)
second_reviewer.rate_hw(second_student, 'Java', 6)
best_student.rate_hw(first_lecturer, 'Python', 10)
best_student.rate_hw(second_lecturer, 'Python', 7)
second_student.rate_hw(first_lecturer, 'Java', 8)
second_student.rate_hw(second_lecturer, 'Python', 9)

print(best_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)
print(first_reviewer)
print(second_reviewer)
print(best_student.avg_grade(), second_student.avg_grade())
print(best_student > second_student)
print(best_student < second_student)
print(best_student == second_student)
print(best_student != second_student)
print(best_student.avg_grade(), second_student.avg_grade())
print(first_lecturer > second_lecturer)
print(first_lecturer < second_lecturer)
print(first_lecturer == second_lecturer)
print(first_lecturer != second_lecturer)

def avg_grade_of_course(students_list, course_name):    #класс Lecturer - дочерний классов Student и Mentor, чтобы не определять дважды функции
    number_grades = 0
    sum_grades = 0
    for student in students_list:
        number_grades += len(student.grades[course_name])
        sum_grades += sum(student.grades[course_name])
    if number_grades != 0:
        return round(sum_grades / number_grades, 1)
    else:
        return 0

std_list = [best_student, second_student]
lectors_list = [first_lecturer, second_lecturer]
print(best_student.grades['Python'], second_student.grades['Python'],)
print(avg_grade_of_course(std_list, 'Python'))
print(first_lecturer.grades['Python'], second_lecturer.grades['Python'],)
print(avg_grade_of_course(lectors_list, 'Python'))

