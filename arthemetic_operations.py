if __name__ == "__main__":
    #addition
    num1=float(input("Enter the first number you want to add: "))
    num2=float(input("Enter the second number you want to add: "))
    print("The sum is:", num1+num2)
    #substraction
    num3=float(input("Enter the first number you want to substract: "))
    num4=float(input("Enter the second number you want to substract: "))
    print("The substraction is:", num3-num4)
    #division
    num5=float(input("Enter the divident for division: "))
    num6=float(input("Enter the devisor for division: "))
    if num6==0:
        print("Error! Division by zero.")
    else:
        print("The division is:", num5/num6)
    #multiplication
    num7=float(input("Enter the first number you want to multiply: "))
    num8=float(input("Enter the second number you want to multiply: "))
    print("The multiplication is:", num7*num8)
