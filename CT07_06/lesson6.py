# Lesson 6 - 2-dimensional list

## Recap 1: List of 100 unique numbers
# **Recap 1a**:
# You are preparing for an upcoming lucky draw session at your
# school. However, there must be no repeating winning numbers.

# Task: Create a program to create 100 random unique numbers in
# a list

# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
# 3. Ensure that all the numbers are unique
# from random import randint, choice
# import random
# lucky=[]
# while len(lucky) < 100: #check
#     x = random.randint(1,1000)
#     if x not in lucky:
#         lucky.append(x)
# print(lucky)
# print(len(lucky))

# **Recap 1b**:
# You have been asked to provide some statistics based on the
# list of numbers generated.

# 1. Using max(), find the highest number from the list
# 2. Using min(), find the lowest number from the list
# 3. Using sum() and len(), find the average from the list
# 4. By importing the 'random' library and using random.choice(),
#    print out a random number from the list.
# 5. Using index(), print out the index of the printed random
#    number.
# print("the min is: "+str(min(lucky)))
# print("the max is: "+str(max(lucky)))
# print("the average is: "+str(sum(lucky) / len(lucky)))
# x=choice(lucky)
# print("random choice is: "+str(x)+" at index "+str(lucky.index(x)))

## Task 1: A list within a list 

# You are about to graduate and would like to create a database
# to keep all your friend's contact details using a 2d list.

# Sample Code (Copy + Paste the below code):
# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# 1. append contact1, contact2, and contact3 into contacts
# 2. Write a nested loop to loop through each contact and print
#    the details for each contact

# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]
# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)
# # Use better variable names :D
# for contact in contacts:
#     for info in contact:
#         print(info)


## Task 2: Student List
# You have been given a 2d list of students from a class
# consisting each student's name and their gender:

# Sample Code (Copy + Paste the below code):
students = [
    ["Olivia", "F", 67], ["Noah", "M", 82], ["Emma", "F", 91],
    ["Liam", "M", 55], ["Ava", "F", 73], ["Ethan", "M", 88],
    ["Sophia", "F", 92], ["Lucas", "M", 74], ["Mia", "F", 64],
    ["Aiden", "M", 79], ["Isabella", "F", 85], ["Jackson", "M", 68],
    ["Amelia", "F", 77], ["Logan", "M", 94], ["Lily", "F", 80]
]
### the above is a nested list. Study and discuss it before we
### move on.

# 1. Write a for loop to print out the names of each student and
#    the gender beside.
   
#    e.g. Olivia F
#         Noah M
# for nothing in students:
#     name , gender, _ = nothing
#     print(name +" "+ gender)

## Task 3: Boys and Girls
# Based on the class list given in the previous task, separate
# the class into 2 lists of boys and girls.

# 1. Create 2 more lists called boys and girls.
# 2. Loop through the 'students' list from the previous task
#    a. if the gender is a boy, add the name into the boys list
#    b. if the gender is a girl, add the name into the girls list
# 3. Write a for loop and name all the boys
# 4. Write a for loop and name all the girls
# 5. Print out how many boys and girls there are

# for nothing in students:
#     name , gender, _ = nothing
#     for gender == "M":
#         print("True")
#     for gender =="F":
#         print(name)
# male= []
# female=[]
# for nothing in students:
#     name,gender, *_ = nothing
#     if gender =="M":
#         male.append(name)
#     else:
#         female.append(name)
    

# print(male)
# print(female)

## Task 4: Gifted Education
# Based on the class list given in the previous task, select those students
# suitable to go to different boys' and girls' schools

# 1. Create 2 more lists called ACS and MGS.
# 2. Loop through the 'students' list from the previous task
#    a. if the gender is a boy, and their score is above 80, add their name into the ACS list
#    a. if the gender is a girl, and their score is above 80, add their name into the MGS list
# 3. Write a for loop and name all the boys in ACS
# 4. Write a for loop and name all the girls in MGS
# 5. Print out the average score for ACS boys
# 6. Print out the average score for MGS girls
# 7. Print out the school with the higher score. "____ has a higher average than ____"
acs=[]
acsscore = 0
mgsscore = 0
mgs=[]
for nothing in students:
    name , gender , score = nothing
    if score >80 and gender =="M":
        acs.append(name)
        acsscore += score
    elif score >80 and gender == "F":
        mgs.append(name)
        mgsscore +=score
print(acs)
print(mgs)
print("acs average score: "+str(acsscore / len(acs)))
print("mgs average score: "+str(mgsscore /len(mgs)))

if (acsscore / len(acs)) - (mgsscore /len(mgs)) >0:
    print("acs has a higher average than mgs")
else:
    print("mgs has a higher average than acs")

