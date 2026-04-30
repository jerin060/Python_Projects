def calculate(expression):
    if "+" in expression:
        num1, num2 = expression.split("+")
        return float(num1) + float(num2)

    elif "-" in expression:
        num1, num2 = expression.split("-")
        return float(num1) - float(num2)

    elif "*" in expression:
        num1, num2 = expression.split("*")
        return float(num1) * float(num2)

    elif "/" in expression:
        num1, num2 = expression.split("/")
        num2 = float(num2)
        if num2 != 0:
            return float(num1) / num2
        else:
            return "Error! Division by zero."

    else:
        return "Invalid input!"


# Take input
expr = input("Enter calculation: ")

result = calculate(expr)
print("Result:", result)