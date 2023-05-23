class Student(object):
    name = "Ivan"
    age = 18
    groupNumber = "10A"

    def __init__(self, name, age, groupNumber) -> None:
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def getGroupNumber(self) -> str:
        return self.groupNumber

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age


st1 = Student("A", 6, "1")
st2 = Student("B", 7, "2")
st3 = Student("C", 8, "3")
st4 = Student("D", 9, "4")
st5 = Student("E", 10, "5")

st1.setNameAge("NewA", 17)
st2.setGroupNumber("NewGroup")

print(st1.getAge())
print(st2.getGroupNumber())
print(st3.getName())
