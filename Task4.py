num1=float(input("Enter  first number: "))
num2=float(input("Enter second number: "))
operator=input("enter the operator like '+,-,*,/,%': ")
match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        if num2!=0:
            print(num1/num2)
        else:
            print("Error: Division by Zero not allowed")
    case "%":
        if num2!=0:
            print(num1%num2)
        else:
            print("Error: Modulo  by Zero not allowed")
    case _:
        print("invalid operator")