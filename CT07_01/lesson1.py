# Pseudocode challenge
# You have been tasked to design a recycling robot that sorts items into bins for glass, plastic and paper
# The robot should check each item's material and place it in the correct bin


#ask user for material of item
# figure out material of item
# if material = glass:
#   put in glass bin
# if material is plastic:
#   put in plastic bin
# if material is paper:
#   put in paper bin
# if material is not glass or plastic or paper:
#   throw away

# Sushi ->
#     Variables ->
#         amount_red plate
#         amount_blue plate 
#         amount_green plate
        
#     functions ->
#         charge_user
#             -> print  of money

# # Recap 2
# amount_red = 3
# amount_blue = 5
# amount_green = 4
# def charge_user():
#     print(amount_red+(amount_blue *2)+ (amount_green *4))
# charge_user()

# There is a total of 3 bugs in the following program.
# Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + str(student_name) + " is: " + str(average_score))

# Recap 4
score = int(input("What is the score: "))
if score > 74:
    print("A")
elif score > 59:
    print("B")
elif score > 49:
    print("C")
else:
    print("fail")