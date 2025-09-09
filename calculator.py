import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple command-line calculator.")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("operator", choices=["+", "-", "*", "/"], help="Arithmetic operator")
    parser.add_argument("num2", type=float, help="Second number")
    args = parser.parse_args()

    if args.operator == "+":
        result = args.num1 + args.num2
    elif args.operator == "-":
        result = args.num1 - args.num2
    elif args.operator == "*":
        result = args.num1 * args.num2
    elif args.operator == "/":
        if args.num2 == 0:
            print("Error: Division by zero")
            return
        result = args.num1 / args.num2
    else:
        print("Invalid operator")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
