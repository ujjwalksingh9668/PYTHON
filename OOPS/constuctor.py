"""
Create a class that takes a name and marks of 3 students as arguments in constructor.
then create a method to print the average.
"""

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg marks is: ",sum/3)


s1 = Student("Ujjwal",[90,80,95])
s1.avg()
