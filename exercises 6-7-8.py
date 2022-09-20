#6.1
"""
import random
def dice():
    return random.randint(1,6)
while True:
    x = dice()
    if x ==6:
        print(x)
        break
    else:
        print(x)

#6.2
import random
def dice(sides):
    return random.randint(1,sides)
numSides = int(input("How many sides the dice has? "))
num = dice(numSides)
while num != numSides:
    print(num)
    num = dice(numSides)
print(numSides)

#6.3
def gallon_Lits(gallons):
    return gallons * 3.785
print("Type negative number to exit")
num_gallon = float(input("How many gallons? "))
while num_gallon >= 0:
    print(f"{num_gallon} gallons = {gallon_Lits(num_gallon):.0f} litters")
    num_gallon = float(input("How many gallons? "))
"""
#6.4
def num_list(a,b):
    sum = 0
    while a <= b:
        sum = sum + a
        a += 1
    return sum
c= int(input(" The list is began at "))
d= int(input(" The list is ended at "))
print(num_list(c,d))

