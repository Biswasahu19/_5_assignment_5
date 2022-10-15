class Student:

    name = 0
    roll_no = 0

    def setName(self, name):
        Student.name = name

    def getName(self):
        return Student.name

    def setRollNumber(self, roll_no):
        Student.roll_no = roll_no

    def getRollNumber(self):
        return Student.roll_no

obj = Student()
obj.setName("Biswa")
print(obj.getName())
obj.setRollNumber("07")
print(obj.getRollNumber())