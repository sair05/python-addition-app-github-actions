import sys


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a + b


def main() -> None:
    if len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

    print(f"Result: {add(a, b)}")


if __name__ == "__main__":
    main()
