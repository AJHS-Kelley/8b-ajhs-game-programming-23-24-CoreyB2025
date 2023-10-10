# Data Types and Operators, Corey Battle Jr, v0.8

# Variable Rules
# CANNOT START WITH A NUMBER !!!!!
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORED.
# snake_case variables use_ to seperate words, all lower case
# camelCase variables do not use spaces, 1st word lower, rest upper

# String Literal Examples 
playerName = "John Doe"
emptyString = ""
spaceString = " "
playerUsername = "Bones"

# Interger Data Types
health = 100
extraLives = 5
temperature = -17

# Floating Point Data Types
pi = 3.1415678
lapTime = 3.5
velocity = -2.0
mapSize = 2.567

# Boolean Data Types
isFireType = False
weaponEquipped = True
pvpEnabled = False
multiplayerOn = False

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(5 + -2) #Addition
print(17 - 2) #Subtraction
print(3 * 3) #Multiplication
print(8 / 4) #Division
print(7 ** 2) # Exponents
print(18 % 3) #Modulus -- Divides, then returns remainder, most commonly used to determine even/odd

# Comparison Operators
# Evaluate the expression, then return True or False
print(5 > 3) # Greater Than
print(7 >= -1) # Greater Than or Equal To
print(-1 < -2) # Less Than
print( 0 <= 0) # Less Than or Equal To
print(5 == 5) # Equal To
print( -77 != 99) # Not Equal To

# Assignment Operators
myVariable = "myValue" 
myOtherVariable = (10 + 5)

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# Addition Assignment -- Add the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logican Operators
print(3 > 5,  AND,  4 < 3) # AND requires ALL expressions to be True
print( 3 > 2 and 4 < 3)
print( 3 > 2 and 4 is != 3 and favColor == "Blue" and temp == -5)
# When writing and expressions, put the value most likely to be False first!

# Logical OR -- Requires ONE expression to be True. 
print(5 > 2 or 2 < -2)
print (3 != 3 or 5 == 5)

# AND OR Combined
print("Line 81")
print(3 > 2 or 4 < 3 and 5 != 7)
# print(True and False and True)

# NOT Logical Operator
print(not (3 > 2))
print(not (not (not ( 5 != 3))))
