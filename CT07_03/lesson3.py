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

