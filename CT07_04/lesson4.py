# Lesson 4 - List Variables I

## Recap 1: While Loop
# Task: Code a New Year Countdown timer. 
# Example: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, HAPPY NEW YEAR!

# 1. The countdown timer will count one by one and stop at 1.
# 2. After 1, the program will say Happy New Year
# 3. Use the time library to pause 1 seconds between each
#    number

# ---------------------------------------------------------------
# import time
# n = 10
# while n !=0:
#     time.sleep(1)
#     print(f"{n},")
#     n -=1
# else:
#     print("happy new year!")


# ## Task 1: List of planets
# **Task: Create a list of 8 planets in the solar system**

# **Task 1a**:
# Create a list of 8 planets in the solar system.
# (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

# **Task 1b**:
# You have conquered Mars, **rename** Mars to a name of
# your liking

# **Task 1c**:
# 1. You have decided Pluto is a planet again, **add** Pluto
#    into the list
# 2. You created an artificial planet between Earth and
#    Mars called "Lalaland". **Insert** the planet in
#    correctly into the list.

# **Task 1d**:
# You launched a war againts Jupiter and destroyed it,
# **delete** Jupiter from the list

# planets =["Mercury", "Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
# planets[3] = "hersheys"
# print(planets[3])
# planets.append("Pluto")
# planets.insert(3,"Lalaland")
# print(planets)
# planets.pop(5)
# print(planets)

# Task 2
# 1. Write a for loop and print out all the names of the
#    planets
# 2. If name == "Earth", print "<planet name> : this is
#    my home"
# 3. If name == "Mars" (or changed name), print
#    "<planet name> : I conquered this"
# 4. If name == "Lalaland", print
#    "<planet name> : I created this"

# for i in planets:
#     print(i,end=" ")
#     if i == "Earth":
#         print(": this is my home")
#     elif i =="hersheys":
#         print(": i conquered this")
#     elif i == "Lalaland":
#         print(": I created this")
#     else:
#         print("")

# for planet in planets:
#     statement = planet
#     if planet == "Earth":
#         statement += ": this is my home"
#     elif planet =="hersheys":
#         statement += ": i conquered this"
#     elif planet == "Lalaland":
#         statement += ": I created this"
#     print(statement)

## Task 3: Flight Round the Globe
# Task: Write a program to keep track of the countries you
# are visiting.

# 1. Use a while loop to ask the user what country they
#    would like to visit.
# 2. Add the country into a list
# 3. If the user types "end", exit the loop
# 4. Print all the countries in the list in this format.
#    "I would like to visit Germany"
#    "I would like to visit Japan"
#    ...

# countries =[]
# while True:
#     ans = str(input("what country do u want to visit?"))
#     if ans == "end":
#         break
#     countries.append(ans)
# for i in countries:
#     print(f"I wound like to visit {i}")


## Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each food item into the menu list
# 3. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, we don't have that."
items =[]
while True:
    ans = str(input("what food do you want to add?"))
    if ans == "end":
        break
    items.append(ans)
    
# order = input("what do u want?")
# if order in items:
#     print("yes we sell that")
# else:
#     print("sorry,we dont have that.")




order =[]
while True:
    ans = str(input("what do u want to order"))
    if ans == "end":
        break
    elif  not ans in items:
        print("sorry we dont have that")
    elif ans in items:
        order.append(ans)
for i in countries:
    print(f"you want")
