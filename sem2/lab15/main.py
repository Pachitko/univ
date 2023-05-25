from entities.lecturer import Lecturer
from entities.reviewer import Reviewer
from entities.student import Student
from entities.course import Course

def CalcAvgLecturerGradeByCourse(lecturers: list[Lecturer], courseId: int):
    sum = 0
    count = 0

    for lecturer in lecturers:
        grades = lecturer.GetGrades()
        if courseId in grades:
            grade = grades[courseId]
            sum = sum + grade
            count = count + 1
    average_grade = 0
    if count != 0:
        average_grade = sum / count
    return average_grade


def CalcAvgStudentGradeByCourse(students: list[Student], courseId: int):
    sum = 0
    count = 0
    for student in students:
        student_grades = student.get_grades()
        if courseId in student_grades:
            grade = student_grades[courseId]
            sum = sum + grade
            count = count + 1
    average_grade = 0
    if count != 0:
        average_grade = sum / count
    return average_grade

# Courses
pythonCourse1 = Course(1, "Python")
pythonCourse2 = Course(1, "Python")
pythonCourse3 = Course(1, "Python")
csharpCourse = Course(2, "C#")
cppCourse = Course(3, "C++")

# Lecturers
lecturer1 = Lecturer('Some1', 'Buddy1')
lecturer1.AddCourse(pythonCourse1)
pythonCourse1.SetLecturer(lecturer1)

lecturer2 = Lecturer('Some2', 'Buddy2')
lecturer2.AddCourse(pythonCourse2)
pythonCourse2.SetLecturer(lecturer2)

lecturer3 = Lecturer('Some3', 'Buddy3')
lecturer3.AddCourse(pythonCourse3)
pythonCourse3.SetLecturer(lecturer3)

# Students
student1 = Student("name1", "surname1")

student1.AddCourse(pythonCourse1)
student1.AddCourse(pythonCourse2)
student1.AddCourse(pythonCourse3)
student1.AddCourse(csharpCourse)
student1.AddCourse(cppCourse)

student1.StartCourse(pythonCourse1.GetId())
student1.StartCourse(csharpCourse.GetId())
student1.FinishCourse(cppCourse.GetId())

student2 = Student("name2", "surname2")
student2.AddCourse(pythonCourse1)
student2.StartCourse(pythonCourse1.GetId())

reviewer = Reviewer('name1', 'surname1')
reviewer + pythonCourse1
reviewer.SetStudentGrade(student1, pythonCourse1.GetId(), 9)
reviewer.SetStudentGrade(student2, pythonCourse1.GetId(), 5)
reviewer + csharpCourse

students = [student1, student2]

print("Средняя оценка студентов за курс Python от проверяющих: ",
        CalcAvgStudentGradeByCourse(students, pythonCourse1.GetId()))

student1.RateLecturer(pythonCourse1.GetId(), 3)
student2.RateLecturer(pythonCourse1.GetId(), 7)

lecturers = [lecturer1, lecturer2, lecturer3]

print("Средняя оценка лекторов за курс Python от студентов: ",
        CalcAvgLecturerGradeByCourse(lecturers, pythonCourse1.GetId()))

if 1 > 2:
    print("Лучше ли первый студент второго? ", best_student > not_best_student)
    print()
    print(lecturer1)
    print()
    print(best_student)
    print()

    print("Имя студента: ", best_student.GetName())
    print("Имя преподавателя: ", lecturer1.GetName())
    print("Оценки лектора по курсам: ", lecturer1.GetGrades())
    print("Оценки студента по курсам: ", best_student.get_grades())