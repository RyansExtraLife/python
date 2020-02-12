#Python built in function examples
print("Hello World")    #Prints Hello World
str(3)                  #Prints "3"
int("15")               #Prints 15

#Input allows user to input data
username = input("Enter the user's name: ")

#Python function
def add_numbers (a, b):
    return a + b

#Python function with type hinting
def add_numbers(a: int, b:int) -> int: 
	return a + b


#Example functions
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase - student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    print(students_titlecase)

def add_student(name):
    students.append(name)


#
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase - student.title()
    return students_titlecase

#
def print_students_titlecase():
    students_titlecase = get_students_titlecase
    print(students_titlecase)

def add_student(name):
    students.append(name)