class Student:
    college_name = "XYZ College"
    name = "anonymous"  # class attr

    def __init__(self, name, marks):
        self.name = name  # obj attr > class attr
        self.marks = marks
        print("Adding new student in Database..")


s1 = Student("khushi", 95)
print(s1.name)

print(s1.college_name)
