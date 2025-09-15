def is_disarium(num):
    num_str = str(num)
    sum_of_powers = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return sum_of_powers == num

disarium_numbers = [num for num in range(1, 101) if is_disarium(num)]

print("Disarium numbers between 1 and 100 are:")
for num in disarium_numbers:
    print(num, end=' | ')