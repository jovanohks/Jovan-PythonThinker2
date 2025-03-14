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

pw = input("what password do u want?")
print(len(pw))
if not((len(pw) >=8) and (pw.isalnum)  and (not pw.isalpha) and (not pw.isupper) and not (pw.islower)):
    print("password accepted")