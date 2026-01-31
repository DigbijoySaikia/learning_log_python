def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a // b


def max_value(a, b):
    return max(a, b)


def min_value(a, b):
    return min(a, b)