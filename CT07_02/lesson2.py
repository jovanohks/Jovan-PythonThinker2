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
# i = 1
# while True:
#     print(i)
#     i+=1
#     if i >= 6:
#         break


# ## Task 3: while... else
# The else condition will run when the loop exits normally
# i.e. when the while condition is no longer true.

# **Task 3a**: Using a while loop
# 1. print the numbers from 1 to 10
# 2. once count has reached 10, use the else and print "Count
#    has reached 10"

# **Task 3b**:
# Now, modify your 'while' loop such that:
# 1. If the number is 5, **break** out of the loop
# 2. Ensure your code has an else

# Observe if the code in the **else** runs.
# i = 1
# while i <=10:
#     print(i)
#     i+=1
# else:
#     print("count has reached 10") 

# i = 1
# while i <= 10:
#     print(i)
#     i+=1
#     if i ==5:
#         break
# else:
#     print("count has reached 10")

#     ## Task 4: Ordering Pizzas with while loop
# **Task: Using what you have learned above, code a program to
# take a customer's order for pizza.
# Declare a variable called _topping_.**

# Using a while loop:
# 1. Ask the user to enter a choice of topping
# 2. For each topping entered, concatenate to the 'topping'
#    variable
# 3. exit the while loop if the user enters "end"
# 4. On program end, print out the toppings that the customer
#    has chosen.
topping = input("What topping do you want? ")
while True:
    x = input("What topping do you want? ")
    if x == "end":
        break
    else:
        topping += ", " + x  
print(f"Your toppings: {topping}")

# Your toppings: hello, hi, nothing