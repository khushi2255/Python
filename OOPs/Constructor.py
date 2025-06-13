class Student:
    # Default Constructors
    def __init__(self):
        pass

    # Parameterized Constructors
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Adding new student in Database..")


s1 = Student("khushi", 90)
print(s1.name, s1.marks)


s2 = Student("Aryan", 87)
print(s2.name, s2.marks)
