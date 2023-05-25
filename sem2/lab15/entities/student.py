from entities.course import Course
from enum import Enum
import statistics


class CourseProgess(Enum):
    NotStarted = 0
    Finished = 1
    InProgess = 2


class CourseState:
    def __init__(self, course: Course):
        self.course = course
        self.progress = CourseProgess.NotStarted

    def GetProgess(self):
        return self.progress

    def StartCourse(self):
        self.courseProgess = CourseProgess.InProgess

    def FinishCourse(self):
        self.courseProgess = CourseProgess.Finished

    def GetCourse(self) -> Course:
        return self.course


class Student:
    def __init__(self, name: str, surname: str):
        self.__name = name
        self.__surname = surname
        self.courses: dict[str, CourseState] = {}
        self.grades = {}

    def AddCourse(self, course: Course):
        self.courses[course.GetTitle()] = CourseState(course)

    def StartCourse(self, courseTitle: str):
        self.courses[courseTitle].StartCourse()

    def FinishCourse(self, courseTitle: str):
        self.courses[courseTitle].FinishCourse()

    def SetGrade(self, courseTitle: str, grade: int):
        self.grades[courseTitle] = grade

    def RateLecturer(self, courseTitle: str, grade: int):
        self.courses[courseTitle].GetCourse().GetLecturer().SetGrade(grade)

    def GetName(self):
        return self.__name

    def GetSurname(self):
        return self.__surname

    def GetFinishedCourses(self) -> list[CourseState]:
        return list(filter(lambda c: c.GetProgress() == CourseProgess.Finished, self.courses))

    def GetCoursesInProgress(self) -> list[CourseState]:
        return list(filter(lambda c: c.GetProgress() == CourseProgess.InProgess, self.courses))

    def get_grades(self):
        return self.grades

    def GetAverageGrade(self) -> float:
        return statistics.mean(self.grades.values)

    def GetCourseTitlesByCourseProgress(self, courseProgess: CourseProgess):
        return ", ".join(list(
            map(lambda c: c.GetTitle(),
                filter(lambda c: c.GetProgress() == courseProgess,
                       self.courses))))

    def __str__(self):
        return f"Имя: {self.__name}\nФамилия: {self.__surname}\nСредняя оценка за лекции: {self.GetAverageGrade()}\nКурсы в процессе изучения: {self.GetCourseTitlesByCourseProgress(CourseProgess.InProgess)} \nЗавершенные курсы: {self.GetCourseTitlesByCourseProgress(CourseProgess.Finished)}"

    def __lt__(self, other):
        return self.GetAverageGrade() < other.calculate_average_grade()

    def __gt__(self, other):
        return self.GetAverageGrade() > other.calculate_average_grade()

    def __hash__(self):
        return hash((self.__name, self.__surname))
