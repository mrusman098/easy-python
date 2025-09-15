def split_and_add(array, k):
    if k < 0 or k >= len(array):
        return array
    first_part = array[:k]
    second_part = array[k:]
    result = second_part + first_part
    return result
arr = [1, 2, 3, 4, 5]
k=3
result = split_and_add(arr, k)
print("Original array:", arr)
print("Array after split and add:", result)