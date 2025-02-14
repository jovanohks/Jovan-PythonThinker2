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

## Task 2: List of 100 unique numbers
# The program you have created from the previous task will
# sometimes generate duplicate numbers. Modify your program so
# that the 100 numbers generated are all unique.

# Modify your program from the previous task to create 100 random
# unique numbers in a list.
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
# 3. Ensure that all the numbers are unique
# 4. Print the list of 100 unique numbers created

# Hint: YOU WILL NEED A WHILE LOOP

# lucky =[]
# from random import randint
# for i in range(100):
#     x = random.randint(1,1000)
#     lucky.append(randint(1,1000))
# print(lucky)

# print([randint(1, 1000) for x in range(100)])
# import numpy
# lucky =[]
# from random import randint
# while len(lucky) <= 100:
#     x= randint(1,1000)
#     if not x in lucky:
#         lucky.append(x)
    

# print(lucky)

## Task 3: Score Taker
# Imagine the list that you have created in Task 2 represent the
# score of a 100 students.

# Find the maximum, minimum and average from the list.

# 1. Using the 'max()' function, find the maximum score.
# 2. Using the 'min()' function, find the minimum score.
# 3. Using the 'sum()' and 'len()' function, calculate the
#    average score.

score =[]
from random import randint
while len(score) <= 100:
    x= randint(0,101)
    score.append(x)
print(score)
print(min(score))
print(max(score))
import numpy
print(sum(score)/len(score))