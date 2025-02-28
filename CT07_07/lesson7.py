# Lesson 7 - 2 dimensional list

## Recap 1: Student Contact Database
# Task: Create a contact database for students
# 1. Create a list variable called students
# 2. Create 3 lists called student1, student2, student3
#     each student should have the following info:
#         1. name
#         2. phone number
#         3. CCA
# 3. Add student1, student2, student3 into the students list.
# 4. Unpack the list and use loop and string concatenation to
#    print the details for each student in the following format:

#    Name: James
#    Phone number: 85726845
#    CCA: Hockey
# students=[]
# student1 = ["John", 98453126, "Hockey"]
# student2 = ["Adam", 93029102, "Soccer"]
# student3 = ["Sylvia", 87894032, "Dance"]
# student.append(student1)
# student.append(student2)
# student.append(student3)
# for student in students: # what is the "i" variable used for, stop messing up my very good variable names.
#     name , number , cca = student
#     print("Name: ",name)
#     print("Phone number: ",number)
#     print("CCA: ",cca)

    
## Task 1: Introduction to List Merging
# You are given 2 lists of fruits. Merge them into 1 list and
# print the result:

list1 = ["Apple", "Banana", "Cherry"]
list2 = ["Durian", "Elderberry", "Figs"]

# 1. Use the + operator to combine the lists.
# 2. Print the combined list. 

# Use another variable pls
print(list1+list2)

nothing = list1+list2
print(nothing)
