import time
# Lesson 3 - More While Loops

## Recap 1: Riddler
# **Task: Using a while loop, code a riddler program**
# 1. Think of a riddle
# 2. Using the while loop, ask the user the riddle and
#    check the answer
# 3. While answer is not correct, repeat the question
# # riddleqans = ["what is 1+1?", "2"]
# # ans = False
# # while ans != True:
# #     x = input(riddleqans[0])
# #     if x == riddleqans[1]:
# #         break
# #     else:
# #         print("u are wrong.")


# riddle_ans = "phone"
# user_ans = ""
# while user_ans != riddle_ans:1
#     user_ans = input("You answer me, although I never ask you questions. What am I? ")


## Task 1: Study Timer
# **Task: Write a program that acts as a study timer**
# 1. The user must input how many minutes they plan to study
# 2. Use a while loop to count down the minutes
# 3. Display "Good job!" once the timer is up

# Hint: you will need the time.sleep(). However this function
# only takes in seconds.
# You will need to write a conversion algorithm to change
# minutes to seconds.
# x = int(input("how many minuetes do u want to study for?"))
# while x !=0:
#     print(str(x)+ "minutes")
#     print(f"{x} minute")
#     time.sleep(60)
#     x -=1
# print("good job!")

## Task 2: Allowance Savings Tracker
# **Task: Write a program to track how much you save, and
# inform you when your savings is more than $100**
# 1. Create a variable called savings
# 2. Using a while loop, ask how much money you save every
#    day
# 3. While savings is less than 100, you continue to save
# 4. Exit the program when savings is more than 100 and
#    congratulate the user.

# example inputs: 5, 0, 0.50, 20.20, 1000

# savings = 0
# while savings <100:
#     savings += float(input("How much did you save? (in dollars)"))
#     print(f"You have ${savings}")
# print("Good job!")
from random import randint

## Task 3: Multiplication Quiz
# **Task: Ms Tan, your math teacher knows that you are a
# programming whiz,
# she has asked you to help code a multiplication quiz for
# the class to practice.**

# Here are her requirements:
# 1. Students have to answer 15 questions in total
# 2. Students have 3 lives (chances). i.e. they can get the
#    question wrong 3 times.
# 3. The questions will be in this format: "What is 3 x 19? ". 
# 4. The numbers for each question will be randomly generated
#    and between the range of 2 to 20.
# 5. If the student answers correctly, move on to the next
#    question
# 6. If the student answers wrongly, minus 1 life, and ask
#     the question again.
# 7. If the student has no more lives, exit and print
#     "GO AND SEE MS TAN FOR REMEDIAL"

# Time the quiz and tell them how long it took to finish the quiz in minutes and seconds, for those who passed only (e.g 1 min 40 seconds)
# If time taken < 1 minute, just print the seconds. (e.g You took 30 seconds)

import time
import math

start = time.time()

x= randint(2,20)
y = randint(2,20)
lives = 3
qnno = 1
while qnno != 16:
    if lives == 0:
        print("you finished the quiz!")
        print("GO AND SEE MS TAN FOR REMEDIAL")
        break
    ans = x * y
    z = int(input(f"Q{qnno} what is {x} * {y} "))
    if z != ans:
        lives -=1
        print("you are wrong!")
    else:
        x= randint(2,20)
        y = randint(2,20)
        qnno +=1
        print("you are right!")
if lives == 3:
    print("you got everything right!, you dont need remedial!")
if lives == 1 or lives == 2:
    print(f"you got {15+(lives-3)}/15 correct, you dont need remedial")
end = time.time()
ttaken = end - start
if ttaken < 60:
    print (f"you took {ttaken} seconds")
else:
    mins = math.floor(ttaken/60)
    secs = round((ttaken/60 - mins) * 60, 2)
    print(f"you took {mins} minuetes {secs} secconds")
    