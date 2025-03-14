# Lesson 8 - String splitting, list joining, and
#            finding substring

## Recap 1: List Manipulation
# Given 3 lists, merge them into a single list, remove
# duplicates, and then split the list into 2 halves,
# ensuring both halves are sorted.

list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]
list5=[]
list6=[]
# 1. Merge the 3 lists and remove duplicates.
# 2. Sort the resulting list.
# 3. Split the list into 2 sorted halves.
# 4. Print the halves.
list4=sorted(set(list1+list2+list3))
print(list4)
list5.append(list4[:len(list4//2)]) 
list6.append([listlen(list4//2):])