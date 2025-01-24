import time
# Lesson 3 - More While Loops

## Recap 1: Riddler
# **Task: Using a while loop, code a riddler program**
# 1. Think of a riddle
# 2. Using the while loop, ask the user the riddle and
#    check the answer
# 3. While answer is not correct, repeat the question
riddleqans = ["what is 1+1?", "2"]
ans = False
while ans != True:
    x = input(riddleqans[0])
    if x == riddleqans[1]:
        break
    else:
        print("u are wrong.")


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
x = input("how many minuetes do u want to study for?")
while x !=0:
    print(x+ "minuete")
    time.sleep(60)
print("good job!")

