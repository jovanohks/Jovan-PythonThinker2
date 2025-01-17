## Recap 1: For Loop
# Task: write a separate 'for' loop to print the following
# numbers:**
# 1. from 0 - 20
# 2. from 1 to 30
# 3. from 2 to 24 (in even numbers)
# for i in range(21):
#     print(i)
# for i in range(1,31):
#     print(i)
# for i in range(2,25,2):
    # print(i)

## Task 1: Introduction to while loop
# **Task: Using a separate 'while' loop, print each of the
# following:**
# 1. from 0 to 20
# 2. from 1 to 30
# 3. from 2 to 24 (in even numbers)

# 1
# i = 0
# while i <=20:
#     print(i)
#     i+=1
# i = 1
# while i <=30:
#     print(i)
#     i+=1
# i = 2
# while i <=24:
#     print(i)
#     i+=2


## Task 2: while... break
# The **break** keyword will **break** out (exit) the loop.
# When a **break** is encountered, the code in the **else** will
# not be run.

# Using a while loop:
# 1. print the numbers from 1 to 10
# 2. if the number is 5, **break** out of the loop
# i = 1
# while True:
#     print(i)
#     i+=1
#     if i >= 11:
#         break
i = 1
while True:
    print(i)
    i+=1
    if i >= 6:
        break