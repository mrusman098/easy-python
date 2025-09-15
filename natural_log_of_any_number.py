import math

num = float(input("Enter a number: "))
if num <= 0:
    print("Natural logarithm is not defined for zero or negative numbers.")
else:
    print("The natural logarithm of", num, "is", round(math.log(num), 2))