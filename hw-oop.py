class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.avg_rate()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Разные категории людей не сравниваем.")
            return
        return self.avg_rate() < other.avg_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res
        
    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Разные категории людей не сравниваем.")
            return
        return self.avg_rate() < other.avg_rate()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


student_01 = Student('Вася', 'Васин', 'unknown')
student_01.courses_in_progress += ['Python', 'VC']
student_01.finished_courses += ['C+']

student_02 = Student('Коля', 'Колин', 'unknown')
student_02.courses_in_progress += ['Python', 'C+']
student_02.finished_courses += ['Java', 'VC']

reviewer_01 = Reviewer('Петя', 'Петин')
reviewer_01.courses_attached += ['Python', 'C+', 'Java']

reviewer_02 = Reviewer('Маша', 'Машина')
reviewer_02.courses_attached += ['Python', 'VC']

lecturer_01 = Lecturer('Саша', 'Сашин')
lecturer_02 = Lecturer('Оля', 'Олина')


reviewer_01.rate_hw(student_01, 'Python', 40)
reviewer_01.rate_hw(student_02, 'Python', 50)
reviewer_02.rate_hw(student_01, 'Python', 60)
reviewer_02.rate_hw(student_02, 'Python', 70)

student_01.rate_lect(lecturer_01, 'Python', 4)
student_01.rate_lect(lecturer_02, 'Python', 5)
student_02.rate_lect(lecturer_01, 'Python', 6)
student_02.rate_lect(lecturer_02, 'Python', 7)

student_list = [student_01, student_02]
lector_list = [lecturer_01, lecturer_02]

import gc

print("Список проверяющих дз:")
for obj in gc.get_objects():
    if isinstance(obj, Reviewer):
        print(obj)

print("Список лекторов:")
for obj in gc.get_objects():
    if isinstance(obj, Lecturer):
        print(obj)

print("Список студентов:")
for obj in gc.get_objects():
    if isinstance(obj, Student):
        print(obj)

print('Сравнение по средним оценкам:')
print('student_01 < student_02 ',student_01 < student_02)
print('lecturer_01 > lecturer_02 ',lecturer_01 > lecturer_02)
print('student_01 < lecturer_01 ', student_01 < lecturer_01)
print()

def avg_rate_course_std(course, student_list):
    sum_ = 0
    qty_ = 0
    for std in student_list:
        for crs in std.grades:
            std_sum_rate = std.avg_rate_course(course)
            sum_ += std_sum_rate
            qty_ += 1
    res = round(sum_ / qty_, 2)
    return res


def avg_rate_course_lct(course, lector_list):
    sum_ = 0
    qty_ = 0
    for lct in lector_list:
        for crs in lct.grades:
            lct_sum_rate = lct.avg_rate_course(course)
            sum_ += lct_sum_rate
            qty_ += 1
    res = round(sum_ / qty_, 2)
    return res

print('Подсчет средней оценки за домашние задания')
print(avg_rate_course_std('Python', student_list))

print('Подсчет средней оценки за лекции')
print(avg_rate_course_lct('Python', lector_list))

