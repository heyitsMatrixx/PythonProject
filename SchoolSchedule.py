class Student:
    def __init__(self, name, age, grade, wanted_courses):
        self.name = name
        self.age = age
        self.grade = grade
        self.wanted_courses = wanted_courses
        if grade >= 83.33:
            self.honors = True
        else:
            self.honors = False
        
class Course:
    def __init__(self, name, max_students, req):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.req = req
    
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
        
def addStudent():
    _name = input()