numbers = [10, 30, -45, 50, -5, 70]
largest_number = numbers[0]
for num in numbers:
    if num > largest_number:
        largest_number = num
print("Largest number in the list is:", largest_number)