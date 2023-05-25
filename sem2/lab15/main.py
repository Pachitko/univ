from entities.lecturer import Lecturer
from entities.reviewer import Reviewer
from entities.student import Student
from entities.course import Course


def CalculateAverageGradeByCourseToLecturers(lecturers: list[Lecturer], course_name: str):
    sum = 0
    count = 0

    for lecturer in lecturers:
        grades = lecturer.GetGrades()
        if course_name in grades:
            grade = grades[course_name]
            sum = sum + grade
            count = count + 1
    average_grade = 0
    if count != 0:
        average_grade = sum / count
    return average_grade


def CalculateAverageGradeByCourseToStudents(students: list[Student], course_name: str):
    sum = 0
    count = 0
    for student in students:
        student_grades = student.get_grades()
        if course_name in student_grades:
            grade = student_grades[course_name]
            sum = sum + grade
            count = count + 1
    average_grade = 0
    if count != 0:
        average_grade = sum / count
    return average_grade

# Lecturers
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.AddCourse("Python")

not_so_cool_lecturer = Lecturer("Vince", "Carter")
not_so_cool_lecturer.AddCourse("Python")

bad_lecturer = Lecturer("Jason", "Tatum")
bad_lecturer.AddCourse("Python")

# Courses
pythonCourse = Course("Python")
pythonCourse = Course("Python")

# Students
best_student = Student("Joel", "Embiid")
best_student.AddCourse(pythonCourse)
best_student.StartCourse("Python")
best_student.StartCourse("Java")
best_student.FinishCourse("ML")

not_best_student = Student("Lebron", "James")
not_best_student.StartCourse('Python')

almost_best_student = Student("Stephen", "Curry")
almost_best_student.StartCourse("Python")

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.AddCourse("Python")
cool_reviewer.RateStudentWork(best_student, "Python", 10)
cool_reviewer.RateStudentWork(not_best_student, "Python", 8)
cool_reviewer.RateStudentWork(almost_best_student, "Python", 9)
cool_reviewer + "Java"

students = [best_student, almost_best_student, not_best_student]

print("Средняя оценка студентов за курс Python от проверяющих: ",
        CalculateAverageGradeByCourseToStudents(students, "Python"))

best_student.RateLecturer("Python", cool_lecturer, 10)
best_student.RateLecturer("Python", not_so_cool_lecturer, 7)
best_student.RateLecturer("Python", bad_lecturer, 4)

lecturers = [cool_lecturer, not_so_cool_lecturer, bad_lecturer]

print("Средняя оценка лекторов за курс Python от студентов: ",
        CalculateAverageGradeByCourseToLecturers(lecturers, "Python"))

print("Лучше ли первый студент второго? ", best_student > not_best_student)
print()
print(cool_lecturer)
print()
print(best_student)
print()

print("Имя студента: ", best_student.GetName())
print("Имя преподавателя: ", cool_lecturer.GetName())
print("Оценки лектора по курсам: ", cool_lecturer.GetGrades())
print("Оценки студента по курсам: ", best_student.get_grades())