#Students Array.
students = []

#Define a class
class Student:
    
    def __init__(self, name, student_id=332):
            student = {"name": name, "student_id": student_id}
            student.append(student)

    def __str__(self):
        return "Student"

mark = Student("Student")

print(students) 
#Output: [{'name': 'Mark', 'student_id': 332}]

#Prior definition of __str__
print(mark)
#Output: <__main__.Student object at 0x10f934d68>

#After definition of __str__
print(mark)
#Output: <Student>