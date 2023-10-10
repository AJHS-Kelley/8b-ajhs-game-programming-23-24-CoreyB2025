# Control Flow,  Corey Battle Jr, v0.1
# DECLARATIONS

favColor = "Lavender"
luckyNumber = 7
myGPA = 4.2
myAge = 16
meatOnPizza = True

# if statements - Check for a condition to be True/False, do something if true. 
if favColor == "Lavender":
    print("I like your style")

if myGPA == 4.2:
    print("Congratulations on making the honor roll!")

# if-else Statement -- Check for a condition to be True/False, do something if true.
if luckyNumber >= 6:
    print("Small numbers for a small winner!")
else:
    print("Better luck next year. Your number was too small!")

# if - elif - else Statements -- Checks for multiple conditions
if myAge > 65:
    print("Congratulations on retiring!")
elif myAge > 50:
    print("Congratulations, you have earned a bonus of 1000!")
else:
    print("You are not old enough for a bonus")

if myAge > 15:
    print("You are eligible for a license")
    if myGPA >= 3.5:
        print("You qualify for a new car!")
    elif myGPA > 2.0:
        print("You qualify for  $500 off a car")
    else:
        print("You get nothing")
else:
    print("You are not yet old enough to drive.")

# When doing if - elif - else statements, check for the highest values first!!!!

# while Loop -- Think "MUSICAL CHAIRS" -- Used when you do NOT know how many items
# iteration = one complete trip through a loop
x = 0
while x < 100: 
    print(f"X is currently equal to {x}")
    x += 1

while x >= 0:
    print(f"X is currently equal to {x}")
    x -= 1

# for Loop -- Think 'Go Fish', used when you know number of iterations needed. 
for i in range(10): # i = iterable variable
    print(i)

print("EVEN OR ODD LOOP!")
for i in range(101):
    print(i)
    if i % 2 == 0:
        print("That number is even!")
    else:
        print("That number is odd")


# () Parentheses
# [] Square Brackets
# <> Angle Brackets
# {} Braces
