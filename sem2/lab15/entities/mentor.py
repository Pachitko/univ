from abc import ABC


class Mentor(ABC):
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses = []

    # getters
    def GetName(self):
        return self.name

    def GetSurname(self):
        return self.surname

    def GetCourses(self):
        return self.courses

    # setters
    def AddCourse(self, courseName: str):
        self.courses.append(courseName)

    def RemoveCourse(self, course_name: str):
        self.courses.remove(course_name)
