lower=1
upper=10
for num in range(lower, upper + 1):
    is_prime = True
    if num == 1:
        is_prime = False
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num)