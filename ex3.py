"""
#1
L = float(input("Lenght of you fish zander (in cm) ? "))
if L >= 42:
    print("You can keep your fish")
else:
    print(f"Please return your fish back to the river, it is {42-L:.2f} cm smaller. ")

#2

Cab = input("What is your cabin class of the cruiship ? ")
if Cab == "LUX":
    print("You have upper-deck cabin with a balcony.")
elif Cab == "A":
    print("You have above the car deck, equipped with a window")
elif Cab == "B":
    print("You have windowless cabin above the car deck")
elif Cab == "C":
    print("You have windownless cabin below the car deck")
else:
    print("invalid cabin class.")

#3
gend = input("What is your biological gender?(male/female) ")
val = float(input("What is your homoglobin value ? "))
if gend == "male" and 134 <= val <= 167:
    print("normal")
elif gend == "male" and val < 134:
    print("low")
elif gend == "male" and val > 167:
    print("high")
elif gend == "female" and 117 <= val <= 155:
    print("normal")
elif gend == "female" and val < 117:
    print("low")
elif gend == "female" and val > 155:
    print("high")
# 4
y = int(input("Enter year to check leap year"))
if y % 4 == 0 and y % 100 != 0:
    print(y, " is a leap year")
elif y % 400 == 0:
    print(y, " is a leap year")
else:
    print(y, " is not a leap year")

#4.1
i = 1
while i < 1000:
    if i % 3 == 0:
        print(i)
    i = i +1

#4.2
i = int(input("enter your number that converts inches to centimeters"))
while i>0:
    print(i*2.54)
    i = int(input("enter your number that converts inches to centimeters again"))

#4.3
i = int(input("enter any number"))
a=i
while :
    i = int(input("enter any number"))
    if a>i:
        a=i
    print(a)


list = []
match_points= [9, 10, 11, 43, 5]
print(match_points[3])
print(match_points[4])
print(match_points[2])

"""
"""
shopping_list= ["apple","celery","spinach","chicken"]
print(shopping_list)
shopping_list[3]="avocado"
print(shopping_list)
shopping_list.insert(3,"4 eggs")

shopping_list.pop(0)
print(shopping_list)

#shopping_list.remove("apple")
#print(shopping_list)

for number in range(1,10,2):
    print(number)
for number in range(4):
    print("I am so cool")

number = list(range(1, 5))
print(number)

# using for
name = input("enter your :,")
for character in name:
    print(Character)



n = int(input("enter your number"))
fact=1
if n>=0:
    for i in range(1, n + 1):
        fact=fact * i
    print(f"{n}! = {fact}")
else:
    print("thanks and bye")

number = 12345.6789
print(f"The number is {number:.5f}")

list = []
number = input("Enter the number: ")

while number != " ":
    list.append(number)
    number = input("Enter the number: ")
list.sort(reverse=True)
print("5 greatest numbers are:")
for i in range(5):
    print(list[i])


"""
list = []
print ("Enter the names of five cities:")

for i in range(5):
    name_city = input("Name of a city:")
    list.append(name_city)
for i in list:
    print(list)