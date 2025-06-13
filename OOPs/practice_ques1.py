"""
Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    # methods
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "Your avg score is:", sum / 3)


s1 = Student("Khushi", [99, 67, 89])
s1.get_avg()
s1.hello()

s1.name="ironman"
s1.get_avg()
