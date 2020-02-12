#strings can be defined with three types of quotes
singleQuote = 'Hello World'
doubleQuote = "Hello World"

# A triple quote is used for multiline comments. 
"""Hello World"""

#String Functions
alphaExample = "hello"
numericExample = "123"

#Capitialize first letter of a string.
capitalize = alphaExample.capitalize() 
print(capitalize)

#Replace charecters in a string.
replace = alphaExample.replace("e", "a")
print(replace)

#Check to see if the string is made up of chars. 
alpha = alphaExample.isalpha()
print(alpha)

#Check to see if string is made up of numbers. Usefull when converting string to int.
numeric = numericExample.isdigit() 
print(numeric)

#Seperate a string using a character.
splitExample = "some,csv,values"
print(splitExample.split(","))

#String Format Function. Allows you to use variables within a string.
name = "Dave"
machine = "HAL"
"Nice to meet you {0}. I am {1}".format(name, machine)

#String Interpolation Allows you to call the variable directly. 
f"Nice to meet you {name}. I am {machine}."