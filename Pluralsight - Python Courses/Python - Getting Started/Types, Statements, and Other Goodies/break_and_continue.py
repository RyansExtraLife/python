student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

#The for loop will stop executing when "Mark" is found.
for name in student_names:
    if name == "Mark":
            print("Found him! " + name)
            break
    print("Currently testing " + name)

#The continue key word will not run the could in th current itteration. 
for name in student_names:
    if name == "Bort":
        continue
        print("Found him! " + name)
    print("Currently testing " + name)

