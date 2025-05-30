from art import logo
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    if n2 == 0:
        return "Infinite"
    return n1 / n2
def calculator():
    print(logo)
    operations = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : div,
    }
    num1 = int(input("What's the first number?:   "))
    isFalse = False
    while not isFalse:
        for symbol in operations:
            print(symbol)
        option = str(input(f"Pick an operation:   "))
        num2 = int(input("What's the next number?:   "))
        result = float(operations[option](num1, num2))
        print(f"{num1:.1f} {option} {num2:.1f} = {result:.1f}")

        more = str(input(f"Type 'y' to continue calculating with {result:.1f}, or type 'n' to start a new calculation:  ")).lower()

        if more == "y":
            num1 = float(result)
        elif more == "n":
            isFalse = True
            print("\n" * 30)
            calculator()
calculator()
