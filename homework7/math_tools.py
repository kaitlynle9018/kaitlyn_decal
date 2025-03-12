def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


def divide(a, b):
    """Returns the quotient of a divided by b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b