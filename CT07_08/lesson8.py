print("Hello from lesson 8")

#Q1
import random
health=100
num_of_battles = 0
print("Hero starts on his adventure with Health: 100")
while True:
    minushealth = random.randint(1,15)
    health = health - minushealth
    if health <=0:
        break
    else:
        print(f"After fighting monsters, his Health is now: {health}")
        num_of_battles +=1
print(f"He fought {num_of_battles} battles, and died.")





#Q2
order = [] # list  to store food user wants
userwant="" #a variable to store the food that user wants to add to order
numitems = 1 #count the number of item that for loop will print
while True:
    userwant= input("What would you like to order? ") #ask user for what food to add to order
    if userwant == "end":
        break #if user type end, end the program
    else:
        order.append(userwant) #append what user has ordered to the stuff that user want
print("You have ordered the following:")
for items in order:
    print(f"{numitems}. {items}") #print the index of items plus 1 since index start from 0 , and tell user what he has ordered
    numitems +=1 # increment 
    







