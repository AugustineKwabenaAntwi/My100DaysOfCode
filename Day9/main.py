class Students :
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
#in cas we have to return a grade
    def get_grade(self):
        return self.grade    

class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students)< self.max_students:
            self.students.append(student)
        else: return False    
            

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value = value + student.get_grade()

        return value / len(self.students)    


s1 = Students("kwame",19,95)
s2 = Students("Kofi",21,83)
s3 = Students("Jill",17,75)

course = Course("Science",2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())