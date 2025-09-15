def count_occurrence(input_list, element):
    count = 0                     # also we can use input_list.count(element) which is inbuilt function
    for item in input_list:
        if item == element:
            count += 1
    return count
my_list = [1, 2, 3, 4, 5, 2, 3, 2]
element_to_count = 2
occurrence_count = count_occurrence(my_list, element_to_count)
print(f"Element {element_to_count} occurs {occurrence_count} times in the list.")