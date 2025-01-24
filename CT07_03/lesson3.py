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

savings = 0
while savings <100:
    x = float(input("how much did you save?"))
    savings = savings +x
    print(f"you have {savings}")
print("good job!")