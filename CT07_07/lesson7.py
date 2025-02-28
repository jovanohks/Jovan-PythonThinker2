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

# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]

# 1. Use the + operator to combine the lists.
# 2. Print the combined list. 

# fruits = list1+list2
# print(fruits)

## Task 2: Ordered List Merging
# You are given 2 lists that contain the price of fruits. Now,
# merge 2 given lists and ensure the resulting list is sorted.

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]
# list3=list1+list2
# # 1. Merge the lists using the + operator.
# # 2. Use the sorted() function to sort the combined list.
# # 3. Print the sorted list.
# print(sorted(list3))

## Task 3: Splitting Lists at a Point
# You are required to divide a basket of fruits.
# Split the given list at the specified index:

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# index = 3 # <- USE THE INDEX

# 1. Use slicing to split the list at the provided index.
# 2. Print the resulting SUBLISTS. I want 2 lists! i.e a left and a right list
# print(fruits[:index],fruits[index:])



## Task 4: Splitting a List in Half
# You have been tasked to divide the basket of fruits into
# 2 equal halves. Given a list of even length, split it
# into 2 equal halves.

fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]

# 1. Find the midpoint of the list.
# 2. Split the list into 2 halves using slicing.
# 3. Print both halves.
hello = (len(fruits)//2)
print(fruits[:hello],fruits[hello:])