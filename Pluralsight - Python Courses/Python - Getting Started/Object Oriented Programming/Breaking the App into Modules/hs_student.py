from student import Student

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
