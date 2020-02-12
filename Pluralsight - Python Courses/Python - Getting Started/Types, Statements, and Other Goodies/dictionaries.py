#Python Dictionaries Example 
student = {
    "name": "Mark",         #Key = "Name", Value = "Mark"
    "student_id": "15163",
    "feedback": None
}

#List of Dictionaries
all_students = [
    {"name": "Mark", "student_id": 15163},
    {"name": "Katarina", "student_id": 63112},
    {"name": "Jessica", "student_id": 30021}
]

#Retriving Dictionary Data
student["Name"] #Will return "Mark"

#Key Errors
student["last_name"] #Will return KeyError

#Avoid KeyErrors
student.get("last_name", "Unknown") #Will return "Unknown"

#Will return all the keys in the dictionary
student.keys()

#Will return all of the values.
student.values() 

#Change Value of a key pair
student["name"] = "James"

#Delete the key value pair completely from the dictionary
del student ["name"]

