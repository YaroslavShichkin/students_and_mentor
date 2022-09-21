class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:\nКурсы в процессе изучения:\nЗавершенные курсы:"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rating(self):
        res = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return res

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self._average_rating()}"
        return res


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
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Alex', 'Green')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lecture(cool_lecturer, 'Python', 9)

print(best_student.grades)
print(cool_lecturer.grades)

print(best_student)
print(cool_lecturer)
print(cool_reviewer)