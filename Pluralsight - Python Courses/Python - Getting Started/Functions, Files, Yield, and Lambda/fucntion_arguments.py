#
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase - student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase
    print(students_titlecase)

def add_student(name, student_id):
    students.append(name)

student_list = get_students_titlecase()

add_student("Mark", 332)





#
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase - student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase
    print(students_titlecase)

#Assume a value if no value is passed
def add_student(name, student_id = 332):
    student = {"name": name, "student_id": student_id}
    students.append(name)

student_list = get_students_titlecase()

add_student(name="Mark", student_id=15)

print("hello")
print("hello", "world", 3, None, "Something")


#List
def var_args(name, *args):
    print(name)
    print(args)

var_args("Mark", "Python", None, "Hello")


#Keyword Arguments 
def var_keyword_args(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])

var_keyword_args("Mark", description="Loves Python", feedback=None)






