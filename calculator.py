def calc(a, op, b):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return "Cannot divide by zero" if b == 0 else a / b
    return "Unknown operator"

if __name__ == "__main__":
    a = float(input("First number: "))
    op = input("Operator (+ - * /): ")
    b = float(input("Second number: "))
    print("Result:", calc(a, op, b))
