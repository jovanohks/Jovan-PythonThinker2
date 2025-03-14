# Lesson 8 - String splitting, list joining, and
#            finding substring

## Recap 1: List Manipulation
# Given 3 lists, merge them into a single list, remove
# duplicates, and then split the list into 2 halves,
# ensuring both halves are sorted.

# list1 = [3, 2, 1]
# list2 = [6, 5, 5]
# list3 = [9, 8, 7]

# 1. Merge the 3 lists and remove duplicates.
# 2. Sort the resulting list.
# 3. Split the list into 2 sorted halves.
# 4. Print the halves.
# list4=sorted(set(list1+list2+list3))
# print(list4)
# list5 = list4[:len(list4)//2]
# list6 = list4[len(list4)//2:]
# print(list5)
# print(list6)

## Task 1: Password Validation
# A website requires all password to:
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers

# Task:
# Write a program that will ask the user for a password, and
# check if the password fits all criteria

# You may use some of the following passwords to test your
# program:
# 1. PassW0rd => true
# 2. H3ll0W0r1d => true
# 3. BestF00d=> true
# 4. pa55Me => false

# pw = input("what password do u want? ")
# print(len(pw))
# if (len(pw) >=8) and (pw.isalnum())  and (not pw.isalpha()) and (not pw.isupper()) and not (pw.islower()):
#     print("password accepted")

#     # 8.1
# user_input = input("New password: ")

# is_8char_long = False
# has_upper = False
# has_lower = False
# has_num = False
# only_alnum = False

# if len(user_input) >= 8:
#     is_8char_long = True

# for i in user_input:
#     if i.isupper() == True:
#         has_upper = True

# for i in user_input:
#     if i.islower() == True:
#         has_lower = True

# for i in user_input:
#     if i.isdigit() == True:
#         has_num = True

# if user_input.isalnum() == True:
#     only_alnum = True

# if is_8char_long and has_upper and has_lower and has_num and only_alnum is True:
#     print("Password is valid")
# else:
#     print("Invalid password")

#2
## Task 2: Mocking Text Generator6
# Create a program that will turn regular sentences into a
# "SpongeBob Mocking" meme.

# For example, the program will turn "Hello my name is James"
# into "HeLlO mY nAmE iS jAmEs"

# 1. Using 'input()', ask the user for a sentence
# 2. Use loops to iterate through each letter of the sentence
# 3. Alternate between '.upper()' and '.lower()' for each letter
# 4. Print the result
i = input(" what do u want to input?: ")
n = 0
result =""
for x in i:
    result +=x