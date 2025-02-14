# Lesson 5 - List Variables II

## Recap 1: Favourite Food List
# **Recap 1a**:
# Create a list of 5 foods that you like to eat

# **Recap 1b**:
# You no longer like to eat the 3rd item on your list,
# delete it

# **Recap 1c**:
# Add 1 more item into your list

# **Recap 1d**:
# Write a for loop to say all the food items in your list

# favouriteFood=["dino minosaur","wanton mee","chicken rice with wasabi","fishball noodles","fried rice"]
# favouriteFood.pop(2)
# favouriteFood.append("sushi")
# favouriteFood.remove("chicken rice with wasabi")
# del(favouriteFood[2])
# favouriteFood.insert(4,"sushi")
# for food in favouriteFood:
#     print(food)
# for i in range


## Task 1: List of 100 numbers 
# You are preparing for an upcoming lucky draw session at your
# school. You have been tasked to create a program that will pick
# 100 lucky winners.

# By importing the 'random' library and using 'random.randint()',
# create a program to create 100 random numbers in a list
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
lucky =[]
from random import randint
for i in range(1,100):
    lucky.append(randint(1,1000))
# print(lucky)

print([randint(1, 1000) for _ in range(100)])