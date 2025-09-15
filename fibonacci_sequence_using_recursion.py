def recrusive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recrusive_fibonacci(n-1) + recrusive_fibonacci(n-2))

nterm=int(input("Enter the number of terms: "))
if nterm<=0:
    print("Please enter a positive integer")
else:
    a, b = 0, 1
    print("Fibonacci Sequence:")
    for i in range(nterm):
        print(recrusive_fibonacci(i), end=" ")