from entities.lecturer import Lecturer


class Course:
    def __init__(self, title: str, lecturer: Lecturer):
        self.title = title
        self.lecturer = lecturer

    def GetLecturer(self) -> Lecturer:
        return self.lecturer

    def GetTitle(self) -> str:
        return self.title

    def __str__(self):
        return f"Course: {self.title}\nLecturer:\n{self.lecturer}"

    def __hash__(self):
        return hash((self.title, self.lecturer))
