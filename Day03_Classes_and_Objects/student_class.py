# create a class to represent a student in a class
class Student:
    def __init__ (self, name, age, grade):
        self.name = name # name of the student
        self.age = age # age of the student
        self.grade = grade # grade of the student
    def __str__(self):
        return f"(Name: {self.name}, Age: {self.age}, Grade: {self.grade})"
    def get_status(self):
        if self.grade.upper() in ["A", "B", "C"]:
            return "Pass"
        else:
            return "Fail"
        
students = [  # list to hold student 
    Student("Lucy", 20, "A"),
    Student("John", 22, "B"),
    Student("Mike", 21, "D"),
    Student("Anna", 19, "C"),
]
for student in students:
    print(student)
    print(f"Status: {student.get_status()}")
    print("------")





    

        







