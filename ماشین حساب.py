import math

print("choose one of this:")

QQZ = print("Add or Sub or div or Mul or tavan or cos or sin or radikal")
UZ = input("Enter your amaliat:")
UZ = UZ.lower()
if UZ == "cos" or UZ == "sin":
    a = eval(input("Enter your number:"))
    if UZ == "sin":
        print(math.sin(a))
    elif UZ == "cos":
        print(math.cos(a))
    else:
        print("please enter a valid data")
    
else :
    a = eval(input("Enter your first number:"))
    b = eval(input("Enter your second number:"))
    if UZ == "add":
        print(a+b)
    elif UZ == "sub":
        print(a-b)
    elif UZ == "div":
        print(a/b)
    elif UZ == "mul":
        print(a*b)
    elif UZ == "tavan":
        print(a**b)
    elif UZ == "radikal":
        print(a*(1/b))
    else :
        print("please enter a valid data")
    