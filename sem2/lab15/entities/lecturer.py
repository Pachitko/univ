from entities.mentor import Mentor
import statistics


class Lecturer(Mentor):

    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}

    def SetGrade(self, courseId: int, grade: int):
        self.grades[courseId] = grade

    def GetGrades(self) -> dict[str, int]:
        return self.grades

    def GetAverageGrade(self) -> float:
        return statistics.mean(self.grades.values)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.GetAverageGrade()}"

    def __lt__(self, other):
        return self.GetAverageGrade() < other.GetAverageGrade()

    def __gt__(self, other):
        return self.GetAverageGrade() > other.GetAverageGrade()

    def __hash__(self):
        return hash(self.name, self.surname)
