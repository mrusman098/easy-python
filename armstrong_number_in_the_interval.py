lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
for num in range(lower, upper + 1):
    num_str = str(num)
    order = len(num_str)
    sum = 0
    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
    if num == sum:
        print(num, "is an Armstrong number")