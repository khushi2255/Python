class Student:
    college_name = "XYZ College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("hello student,", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("khushi", 95)
s1.hello()
print(s1.get_marks())
