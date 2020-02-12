#If statement equality check
number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")

#Truthy and Falsy Values
number = 5
if number:
    print("Number is defined and true") 

text = "Python"
if text:
    print("Text is defined and truthy")

#Boolean and None
python_course = True
if python_course: 
    print("This will execute")
else:
    print("This will NOT execute")

no_value_yet = None
if no_value_yet:
    print("This will NOT execute")

#Not If
number = 5
if number != 5:
    print("This will NOT execute")
else:
    print("This will execute")

python_course = True
if not python_course:
    print("This will not execute")
else:
    print("This statement will execute")


#Multiple If Conditions using "and" and "or"
number = 3
python_course = True
if number == 3 and python_course:
    print ("This will execute")

if number == 17 or python_course:
    print ("This will execute")

#Ternary If Statements
a = 1
b = 2
"bigger" if a > b else "smaller"