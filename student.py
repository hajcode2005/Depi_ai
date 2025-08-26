"""
dic.........
"""

class Student :
    _id_counter = 1

    def __init__(self,name):
        self.name = name
        Student._id_counter +=1
        self.student_id = Student._id_counter
        self.grades = {}
        self.enrolled_courses = []

    def __str__(self):
        return  f"student id :{self.student_id},name :{self.name},grade: {self.grades}"
    def __repr__(self):
        return  f"student id :{self.student_id},name :{self.name},grade: {self.grades}"
    #def __str__(self):
       # return  f"student id :{self.student_id},name :{self.name},grade: {self.grades}"
    def add_grade(self, course_id ,grade):
        self.grades[course_id] = grade
    
    def enrolled_in_course (self,course):
        self.enrolled_courses.append(course)
    