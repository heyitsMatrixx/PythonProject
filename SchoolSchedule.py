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
        # req: [[59.5 (or higher | int), "Class (string)"], Honors Req (bool)]
        # use "n" if section is blank
    
    def add_students(self, student):
        if len(self.students) < self.max_students:
            if self.req[0][0] != "n" and self.grade > req[0][0]:
                self.students.append(student)
                return True
            else:
                self.students.append(student)
                return True
        return False

courses = {
    "Algebra I":Course("Algebra I", 6, [["n", "n"], False]),
    "Geometry":Course("Geometry", 5, [[59.5, "Algebra I"], False]),
    "Algebra II":Course("Algebra II", 3, [[79.5, "Geometry"], True])
}

courseNames = [
    "Algebra I", "Geometry", "Algebra II"
]

students = [
    Student("Bill", 15, 89, ["Geometry"])
]