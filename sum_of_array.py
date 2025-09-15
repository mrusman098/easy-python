arr = [1, 2, 3, 4, 5]
ans=sum(arr)
print("The sum of the array using built-in function is:", ans)

def sum_of_array(array):
    total = 0
    for num in array:
        total += num
    return total
array = [10, 20, 30, 40, 50]
result = sum_of_array(array)
print("The sum of the array using custom function is:", result)