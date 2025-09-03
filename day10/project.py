def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide,
}

def calculator():
    first_num = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("What's the operation?: ")
        second_num = float(input("What's the second number?: "))
        result = operations[operation_symbol](first_num, second_num)
        
        print(f"{first_num} {operation_symbol} {second_num} = {result}")
        
        is_restart = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()

        if is_restart == 'y':
            first_num = result
        elif is_restart == 'n':
            should_continue = False
            calculator()

calculator()

