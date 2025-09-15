def cube_sum(n):
    if n <= 0:
        return 0
    else:
        total = n**3 + cube_sum(n-1)
        return total
n=int(input("Enter a natural number: "))
if n<=0:
    print("Please enter a valid natural number greater than 0.")
else:
    result = cube_sum(n)
    print("The sum of the cubes of the first", n, "natural numbers is:", result)