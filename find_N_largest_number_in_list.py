def find_n_largest_numbers(numbers, N):
    if N <= 0:
        return []
    sorted_numbers = sorted(numbers, reverse=True)
    largest_number = sorted_numbers[:N]
    return largest_number

numbers = [10, 345, 23, 67, 89, 12, 90]
N=int(input("Enter the value of N: "))
result = find_n_largest_numbers(numbers, N)
print(f"The {N} largest numbers in the list are: {result}")
