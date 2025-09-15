numbers = [10, 30, -45, 50, -5, 70]
numbers.sort(reverse=True)
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("Second largest number in the list is:", second_largest)
else:
    print("List does not have enough elements to determine the second largest number.")