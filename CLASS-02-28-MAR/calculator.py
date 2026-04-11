def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def main() -> None:
    print("Simple Function Calculator")
    print("1) Add  2) Subtract  3) Multiply  4) Divide  5) Exit")
    while True:
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        if choice in ("5", "q", "exit"):
            print("Goodbye")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, try again.")
            continue
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input. Please enter numeric values.")
            continue
        try:
            if choice == "1":
                result = add(x, y)
            elif choice == "2":
                result = subtract(x, y)
            elif choice == "3":
                result = multiply(x, y)
            else:
                result = divide(x, y)
            print("Result:", result)
        except ZeroDivisionError as e:
            print(e)


if __name__ == "__main__":
    main()
