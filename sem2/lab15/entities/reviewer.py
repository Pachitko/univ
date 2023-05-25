from entities.mentor import Mentor
from entities.student import Student


class Reviewer(Mentor):

    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)

    def PrintCourses(self):
        for elemement in self.GetCourses():
            print(elemement)

    def __add__(self, other: str):
        self.AddCourse(other)

    def __sub__(self, other: str):
        self.RemoveCourse(other)

    def __hash__(self):
        return hash((self.name, self.surname))

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def SetStudentGrade(self, student: Student, courseTitle: str, grade: int):
        student.SetGrade(courseTitle, grade)
