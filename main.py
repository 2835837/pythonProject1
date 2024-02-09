firstname=input("What is your first name?")
familyname=input("What is your family name?")
print(firstname,familyname)
print(firstname+familyname)
print(firstname+"blablabla")
print(firstname+"2")
print(firstname+str(2))
quit() # The  program is over



# EXAMPLE TWO
name="stephen easley walsh"
print(name)
print(name.title()) # Make every word's first letter a capital
print(name.capitalize()) # Makes the first letter a capital
print(name.count("e")) # how many e are there, there are 4
print(name.count("E")) # Notice that this word give 0
print(name.find("n")) # The n is at 6 (start counting from 0)
print(name.find("x")) # There is no x so it will print -1
print(name.isdigit()) # Checks is name a digit (number)(use of 123456789 Only)
print(name.isalpha()) # checks that ONLY abc...xyz is used and NOTHING ELSE
print(name.isalnum()) #Checks that only 0123456789 and abc....xyz is used AND NOTHING ELSE
print(name.islower()) # Checks for ONLY LOWER lettters are used
print(name.isupper()) # Checks for ONLY UPPER lettters are used
print(name.lower()) # changes to lower
print(name.upper()) # changes to upper
print(name.replace("a,""x")) # The letter a is replaced by the letter x

print(11//3) # 11 FLOOR DIVIDE 3 = QUOTIENT (TOP）
print(11%3)
