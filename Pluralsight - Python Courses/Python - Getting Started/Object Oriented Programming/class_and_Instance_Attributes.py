#Students class array.
students = []

#Define a class
class Student:

    #Class Attributes
    school_name = "Springfield Elementary"
    
    def __init__(self, name, student_id=332):
        #Removed the dictonary and added self referencing variables. 
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
            return self.school_name

#mark = Student("Mark")
#print(mark)

print(Student.school_name)

#Output: Springfield Elementary


