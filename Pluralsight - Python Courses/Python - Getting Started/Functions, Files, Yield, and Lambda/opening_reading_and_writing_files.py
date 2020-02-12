students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase - student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase
    print(students_titlecase)

def add_student(name):
    student = {"name": name, "student_id": student_id}
    students.append(name)

#
def save_file(student):
    try: 
        """
            The Second variable determines the mode of open
            w - writing; overwrites the entire file
            r - reading: reads a text file
            a - appending to a new or existing file
            rb - reading a binary file
            wb - writing to a binary file
        """
        f = open("students.txt", "a")
        #Writes the file, the return carraige creates new lines for each student.
        f.write(student + "\n")
        #Tell the OS to close the applicaiton and release the lock. 
        f.close
    except Exception:
        print("Could not save file")

#
def read_file():
    try: 
        f = open("students.txt", "r")
        #Reads each line and adds them to the variable. 
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


#
read_file()
print_students_titlecase()




student_list = get_students_titlecase()

student_name = input ("Enter studet name: ")
student_id = input("Enter student ID: ")
 
add_student(student_name, student_id)

#
save_file(student_name)
