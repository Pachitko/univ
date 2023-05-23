class Student(object):
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age


st1 = Student()
st2 = Student("B", 7, "2")
st3 = Student("C", 8, "3")
st4 = Student("D", 9, "4")
st5 = Student("E", 10, "5")

st1.setNameAge("NewA", 17)
st2.setGroupNumber("NewGroup")

print(st1.getAge())
print(st2.getGroupNumber())
print(st3.getName())
