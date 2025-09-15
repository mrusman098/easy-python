list_of_lists = [1, 2, [], 4, [], 5, [], 6]
non_empty_lists = [lst for lst in list_of_lists if lst != []]
print("List after removing empty lists:", non_empty_lists)