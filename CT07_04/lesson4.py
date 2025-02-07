# Lesson 4 - List Variables I

## Recap 1: While Loop
# Task: Code a New Year Countdown timer. 
# Example: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, HAPPY NEW YEAR!

# 1. The countdown timer will count one by one and stop at 1.
# 2. After 1, the program will say Happy New Year
# 3. Use the time library to pause 1 seconds between each
#    number

# ---------------------------------------------------------------
n = 10
while n !=0:
    print(f"{n},")
    n -=1
else:
    print("happy new year!")