def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def is_right_angled(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print(f"Triangle Type: {triangle_type(a, b, c)}")
        if is_right_angled(a, b, c):
            print("It's a Right-Angled Triangle.")
        else:
            print("It's not a Right-Angled Triangle.")
    else:
        print("The sides do not form a triangle.")
        
a=int(input("enter the number1:")  )
b=int(input("enter the number2:") ) 
c=int(input("enter the number3:") )   
triangle_type(a,b,c)
is_right_angled(a,b,c)
check_triangle(a,b,c)