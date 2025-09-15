original_list = [1, 2, 3, 4, 5]
cloned_list1 = original_list[:]
print("Original List:", original_list)
print("Cloned List:", cloned_list1)

copied_list2 = list(original_list)
print("Copied List:", copied_list2)

cloned_list3 = [item for item in original_list]
print("Cloned List using list comprehension:", cloned_list3)