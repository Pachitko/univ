from abc import ABC
from entities.course import Course


class Mentor(ABC):
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses = []

    # getters #
    def GetName(self):
        return self.name

    def GetSurname(self):
        return self.surname

    def GetCourses(self):
        return self.courses

    # setters #
    def AddCourse(self, course: Course):
        self.courses.append(course)

    def RemoveCourse(self, courseTitile: str):
        self.courses = filter(lambda c: c.RemoveLecturer(this), self.courses)
