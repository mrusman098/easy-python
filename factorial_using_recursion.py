def recursive_factorial(n):
        if n == 1:
            return 1
        else:
            return n * recursive_factorial(n - 1)
        
num=int(input("Enter a number: "))
if num<0:
    print("Factorial is not defined for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
   
    print("Factorial of", num, "is", recursive_factorial(num))