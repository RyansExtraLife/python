#Checks for condition prior to starting the loop. 
x = 0 
while x < 10:
    print("Count is {0}".format(x))
    x += 1

x = 0 
while x < 10:
    print(f"Count is {x}")
    x += 1

#Infinite Loops
number = 10
while True:
    if number == 42:
        break
    print("Hello World")