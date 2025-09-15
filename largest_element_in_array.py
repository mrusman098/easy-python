def largest_element_in_array(array):
    if not array:
        return None  # Handle empty array case
    else:
        largest = array[0]
        for i in array:
            if i > largest:
                largest = i
        return largest
array = [1, 2, 3, 4, 5, 4, 1, 2, 3]
largest_element = largest_element_in_array(array)
print("The largest element in the array is:", largest_element)