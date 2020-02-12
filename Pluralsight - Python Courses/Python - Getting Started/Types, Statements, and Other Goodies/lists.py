#Create empty list
student_names = []

#Create populated list
student_names = ["Mark", "Katarina", "Jessica"]

#Getting list elements
print(student_names[0])     #Mark
print(student_names[2])     #Jessica
print(student_names[-1])    #Jessica

#Changing List Elements
student_names = ["Mark", "Katarina", "Jessica"]
student_names[0] = "James"
print(student_names[0])

#Append Function
student_names = ["Mark", "Katarina", "Jessica"]
student_names.append("Homer")   #Appends to end of list
print("Mark" in student_names)

#Number of elements in list
len(student_names)

#Delete Function
del student_names[2]

#List slicing
student_names = ["Mark", "Katarina", "Jessica"]
student_names[1:]       #Katarina, and Homer
student_names[1:-1]     #Katarina 

 

 