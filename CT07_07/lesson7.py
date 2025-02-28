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

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]

# 1. Find the midpoint of the list.
# 2. Split the list into 2 halves using slicing.
# 3. Print both halves.
# hello = (len(fruits)//2)
# print(fruits[:hello],fruits[hello:])

## Task 5: Identifying Common Elements in Lists
# You have been given 2 lists of fruits. However, there might be
# duplicates. Your job is to identify and print the common fruits
# between them.

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
# common = []
# 1. Create an empty list named 'common'
# 2. Using 'for' loops, append common elements into 'common'
# 3. Print the common elements
# for i in list1:
#     if i in list2:
#         common.append(i)
# print(common)

## Task 6: Merging Lists Unique Items
# You have been given 2 lists of fruits that contains duplicates.
# Your task is to merge the 2 lists into a new list that contain
# no duplicates.

# list1 = ["Apple", "Banana", "Cherry", "Cherry"]
# list2 = ["Cherry", "Durian", "Durian", "Figs"]
# unique=[]
# 1. Create an empty list named 'unique'
# 2. Using 'for' loops, append unique elements into 'unique'
# 3. Print the unique elements
# for i in list1+list2:
#     if i not in unique:
#         unique.append(i)
# for i in list2:
#     if i not in unique:
#         unique.append(i)
# print(unique)

## Task 7: Merging Lists with Conditions
# You have been given the index number of 2 groups of students.
# However, only students with even index number is allowed
# to come into the room. Create a Python script that will
# merge the 2 lists, including only the elements that are
# even from both.

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# even=[]
# 1. Create an empty list named 'even'
# 2. Using 'for' loops, append even elements into 'even'
# 3. Print the new list
# nums=list1+list2
# for i in nums:
#     if i %2 == 0:
#         even.append(i)
# print(even) 


## Task 8: Nested List Splitting
# You are given a nested list of 3 groups of students that
# are each seated in a pair. However, you want to unpack
# the nested lists in order to have a list of all students.

nested_list = [[1, 2], [3, 4], [5, 6]]

# 1. Create an empty list named 'flat_list'
# 2. Loop through each sublist and append each element to the
#    flat_list
# 3. Print the flattened list.
