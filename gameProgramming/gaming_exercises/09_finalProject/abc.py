# input the intergers
# .split() the 3 intergers into seperate variables
# cast the 3 variables to intergers
# assign correct values from lest to greatest
# A < B < C

intergers = input()
a. b, c = intergers.spliy()
a = int(a)
b = int(b)
c = int(c)

print(f"a: {a} b: {b} c {c}")
if a >=b:
    a, b = b, a
if a >=b:
    b, c = c, b
if a >=b:
    b, a = a, b
print(f"a: {a} b: {b} c {c}")

# input the string variable
# determine order of A, B, and C.
# create correct string
# output string

order = input()
myString =""

for i in range(len(order)): 
    if order [i] == "A"
        myString += str(a) + " "
    elif: 

    else:

print(myString)