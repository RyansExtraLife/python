student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

#KeyError
try:
    last_name = student["students"]
except KeyError:
    print["Error finding last_name"]

print("This code executes!") 

#TypeError
student["last_name"] = "Kowalski"
try:
    last_name = student["last_name"]
    numberd_last_name = 3 + last_name
except KeyError:
    print["Error finding last_name"]
except TypeError:
    print("String cannot be added to type.")

print("This code executes!") 


#Unkown Error
student["last_name"] = "Kowalski"
try:
    last_name = student["last_name"]
    numberd_last_name = 3 + last_name
except KeyError:
    print["Error finding last_name"]
except TypeError:
    print("String cannot be added to type.")
except Exception:
    print ("Unkown Error")

print("This code executes!") 


#Detailed Error Messges
student["last_name"] = "Kowalski"
try:
    last_name = student["last_name"]
    numberd_last_name = 3 + last_name
except KeyError:
    print["Error finding last_name"]
except TypeError as Error:
    print("String cannot be added to type.")
    print(Error)

print("This code executes!") 
