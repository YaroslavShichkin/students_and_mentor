def average_rating_hw(course, students):
    x = []
    for student in students:
        if course in student.grades.keys():
            x += student.grades[course]
    return sum(x) / len(x)


def average_rating_lecture(course, lecturers):
    x = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            x += lecturer.grades[course]
    return sum(x) / len(x)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rating(self):
        if len(sum(self.grades.values(), [])) == 0:
            return 0
        res = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return res

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_rating()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        return self._average_rating() < other._average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers.append(self)

    def _average_rating(self):
        res = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return res

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating()}\n"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        return self._average_rating() < other._average_rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n"
        return res


students = []
lecturers = []

student_1 = Student('Иван', 'Иванов', 'мужской')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Анна', 'Лазарева', 'женский')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Александр', 'Коган')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Анатолий', 'Владимиров')
lecturer_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Максим', 'Горшков')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Илья', 'Башкин')
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 7)

student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'Git', 10)
student_1.rate_lecture(lecturer_1, 'Git', 8)
student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Python', 5)
student_1.rate_lecture(lecturer_2, 'Python', 10)

print(student_1.grades, student_2.grades, lecturer_1.grades, lecturer_2.grades, sep="\n")

print(student_1, student_2, lecturer_1, lecturer_2, reviewer_1, reviewer_2, sep="\n")

print(student_1 > student_2, lecturer_1 < lecturer_2, sep="\n")

print(average_rating_hw("Python", students))
print(average_rating_lecture("Python", lecturers))
