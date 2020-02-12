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


#Define a class that inherits Student
class HighSchoolStudent(Student):

    #Override the school_name attribute
    school_name = "Springfield High School"

    #Override the get_school_name method.
    def get_school_name(self):
        return " This is a High School student"

    #Inherite method and modify the results.
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"


#Without method override
james = HighSchoolStudent("james")
print(james.get_name_capitalize())
#Output: James
 

#With method override
james = HighSchoolStudent("james")
print(james.get_name_capitalize())
#Output: This is a High School student
 