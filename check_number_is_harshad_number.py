def is_harshad_number(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(num, "is a Harshad number.")
else:
    print(num, "is not a Harshad number.")
