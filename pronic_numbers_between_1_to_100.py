def is_pronic_number(n):
    for i in range(n):
        if i * (i + 1) == n:
            return True
    return False

print("Pronic numbers between 1 and 100 are:")
for n in range(1, 11):
    if is_pronic_number(n):
        print(n, end=' | ')