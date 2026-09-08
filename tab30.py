num1, num2 = 10, 5
operator = '*'

match operator:
    case '+': print(num1 + num2)
    case '-': print(num1 - num2)
    case '*': print(num1 * num2)
    case '/': print(num1 / num2 if num2 != 0 else "Cannot divide by zero")
    case _: print("Invalid Operator")
