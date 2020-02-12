 #Create populated list
student_names = ["Mark", "Katarina", "Jessica"]

#Print each element of the list
print(student_names[0])
print(student_names[1])
print(student_names[2])

#For Loop
for name in student_names:
    print("Student name is {0}".format(name))

#For Loop with Interpolation
for name in student_names:
    print(f"Student name is {name}")

#Number of iterations the loop will preform.
x = 0

#Passed range value is the number of interations the loop will preform.
for index in range(10): 
    x = x + 10      # x += 10 also works
    print("The value of X is {0}".format(index))

#Change starting iteration. 
x = 0

for index in range(5, 10): # The first value is the number in which the loop will start at. 
    x = x + 10      
    print("The value of X is {0}".format(index))

#Determine the increment value. 
x = 0
for index in range(5, 10, 2): # The third value is the number of times it increments per loop. 
    x = x + 10      
    print("The value of X is {0}".format(index))

