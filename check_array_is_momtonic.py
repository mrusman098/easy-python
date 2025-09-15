def is_monotonic(arr):
    if not arr:
        return True
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing

arr1 = [1, 2, 2, 3]
arr2 = [1, 2, 3]
arr3 = [5, 4, 3, 2, 1]

print("Array 1 is monotonic:", is_monotonic(arr1))
print("Array 2 is monotonic:", is_monotonic(arr2))
print("Array 3 is monotonic:", is_monotonic(arr3))