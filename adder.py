def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a + b


def main() -> None:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Result: {add(a, b)}")


if __name__ == "__main__":
    main()
