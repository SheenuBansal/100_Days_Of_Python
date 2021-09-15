logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


# Add Function
def add(n1, n2):
    return n1 + n2


# Subtract Function
def subtract(n1, n2):
    return n1 - n2


# Multiply Function
def multiply(n1, n2):
    return n1 * n2


# Divide Function
def divide(n1, n2):
    return n1 / n2


# Modulo Function
def modulo(n1, n2):
    return n1 % n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
}



def calculator():
    num1 = float(input("What's the First Number?\n"))

    print("Please choose an operation.")
    for symbol in operations:
        print(symbol)
    
    shud_continue= True
    while shud_continue:
        operation_symbol = input('Please choose an operation.\n')

        num2 = float(input("What's the Next Number?\n"))

        To_do_operation = operations[operation_symbol]
        answer = To_do_operation(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        next_play=input(f"Type 'y' to continue with {answer} ,'n' to start a new calculation.\n")

        if next_play=='y':
            num1=answer
        else:
            shud_continue=False

    calculator()

calculator()


