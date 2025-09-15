import math
if __name__ == "__main__":

    """
        standard quadratic equation : ax**2 + bx + c = 0
        a,b,c is real number and a=!0
        the solution for this quadratic equation is giiven by:
        (-b +-(b**2 - 4ac)**0.5) / 2a
    """
    
    a=float(input("enter the cofficieant of a: "))
    b=float(input("enter the cofficieant of b: "))
    c=float(input("enter the cofficieant of c: "))
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"The equation has two real and distinct roots: {root1} and {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"The equation has one real root: {root}")
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"The equation has no real roots. Complex roots are: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")