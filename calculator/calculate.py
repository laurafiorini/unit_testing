
def calculate(num1, num2, operator):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("The given numbers must be integers.")
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 * num2
    elif operator == '*' or operator == 'x':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '**' or operator == '^':
        return num1 ** num2
    else:
        raise ValueError("The operator must be: +, -, *, x, /, ** or ^.")