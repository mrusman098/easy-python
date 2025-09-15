numbers = [10, 30, -45, 50, -5, 70]
smallest_number = numbers[0]
for num in numbers:
    if num < smallest_number:
        smallest_number = num
print("Smallest number in the list is:", smallest_number)