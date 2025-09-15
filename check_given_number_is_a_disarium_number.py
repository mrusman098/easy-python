def is_disarium(num):
    num_str = str(num)
    sum_of_powers = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return sum_of_powers == num
try:
    num = int(input("Enter a number: "))
    if is_disarium(num):
        print(num, "is a Disarium number.")
    else:
        print(num, "is not a Disarium number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")