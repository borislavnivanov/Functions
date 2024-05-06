operant = input()
n1 = int(input())
n2 = int(input())


def calculator(num1: int, num2: int, operator: str) -> int or float:
    if operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return num1 / num2
    elif operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2
    else:
        raise ValueError


try:
    result = int(calculator(n1, n2, operant))
except ValueError:
    result = 'Allowed base 10 numbers and mathematical operators only!'

print(result)
