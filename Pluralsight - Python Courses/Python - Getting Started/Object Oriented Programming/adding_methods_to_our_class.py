#Students Array.
students = []

#Define a class
class Student:
    #Self does not need to be passed, it allows the class to call methods from within itself. Example: self.add_student()
    def add_student(self, name, student_id=332):
            student = {"name": name, "student_id": student_id}
            student.append(student)


student = Student ()
student.add_student("Mark")
print(students) 

#Output: [{'name': 'Mark', 'student_id': 332}]