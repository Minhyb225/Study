"""
##
import math
print("enter a : b :c")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
delta=b**2 - 4*a*c
if delta > 0:
    #print("x1 = ", (-b + math.isqrt(delta))/2*a /n "x2 = ", (-b - math.isqrt(delta))/2*a)
    print(f"x1 = {((-b + math.sqrt(delta))/2*a):.2f}")
    print(f"x2 = {((-b - math.sqrt(delta))/2*a):.2f}")
elif delta == 0:
    print("x1 = x2 = ", -b/2*a)
else:
    print("The equation has no solution")
##
"""


def P_kg(z):
    return z * 0.454
def Mi_km(y):
    return y * 1.60
def F_C(x):
    return (x - 32) * 5 / 9
Choose = "Yes"
while Choose == "Yes":
    a = int(input("What do you want to convert: \n (Fahrenheit to Celsius) type 1  \n (Miles to km) type 2 \n (Pound to kg) type 3 \n "))
    if a == 1:
        Fahrenheit = int(input("Type "))
        print(f"{Fahrenheit} Fahrenheit = {F_C(Fahrenheit)} Celsius")
    elif a == 2:
        Miles = int(input("Type "))
        print(f"{Miles} Miles = {Mi_km(Miles)} Kilometer")
    elif a == 3:
        Pound = int(input("Type "))
        print(f"{Pound} Pounds = {P_kg(Pound)} Kilogram")
    Choose = str(input("Do you want to continue:Yes-No"))
print(P_kg(3))
"""
    #(f"{F} Fahrenheit = {(F−32)×5/9} Celsius")
def Miles-km(Miles):
    return Miles * 1.609
def Pound-kg(Pound):
    return Pound * 0.454

print(Miles-km(b))
print(Pound-kg(c))
"""






